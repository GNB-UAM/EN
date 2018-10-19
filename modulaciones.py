# -*- encoding: utf-8 -*- # Especificamos que nuestro archivo .py estÃ¡ codificado en UTF-8
import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import Adafruit_DHT as DHT
import time
import os
import sys
import tratamiento_cadenas as tc
from threading import Thread,currentThread,Event
from datetime import datetime, date
from scipy import stats
import queue as qu
import numpy as np
import math
import pickle
import sys
import signal

class Modulacion(object):

    SYNC,EXIT = -1,-2
    motorPin = 'P9_21'
    NM = 10 #Numero lecturas ADC
    T = 0.1 #Las NM lecturas se hacen en T segundos
    tsub = T/NM; #Subdivisiones de tiempo para las lecturas ADC
    SLEEP, SLEEP_tyh = 1,59
    Vcc = 5
    sensorTemp22 = DHT.AM2302
    Temp22 = 'P8_11'
    odorantes = {1:'Metanol',2:'Etanol',3:'Butanol',4:'Aire'}
    TyH_sensor = {1:DHT.DHT11,2:DHT.DHT22,3:DHT.AM2302}
    electrovalvulas = ['P8_10','P8_12','P8_14','P8_16']

    def __init__(self,config_experiment,**kwargs):
        super().__init__(**kwargs) #Comprobar que no falle por esto
        Modulacion.daemonizar()
        
        self.succiones = config_experiment[tc.SSUCCION]
        self.switchs = config_experiment[tc.SSWESTIM]
        self.samples_ini = config_experiment[tc.SSINICIO]
        self.cte = config_experiment[tc.SSBESTIM]
        self.name_files = config_experiment[tc.SNFILE]
        self.name_folders = config_experiment[tc.SNFOLDER]
        self.vecs_open_valves = config_experiment[tc.SVECOPVAL]
        self.vecs_anal_odort = config_experiment[tc.SVECOPODR]
        self.sleeps = config_experiment[tc.SSLEEP]
        self.time_mark = datetime.now()
        self.f,self.g,self.h,self.thiread = None,None,None,None
        self.humidity, self.temperature = None,None
        self.air_loop = False
        Modulacion.motorPin = config_experiment[tc.SMTPORT] if config_experiment[tc.SMTPORT] != '' else 'P9_21'
        Modulacion.NM = int(config_experiment[tc.SNMUETS]) if config_experiment[tc.SNMUETS] != '' else 10
        Modulacion.T = float(config_experiment[tc.SRDTIME]) if config_experiment[tc.SRDTIME] != '' else 0.1
        Modulacion.SLEEP = int(config_experiment[tc.SSLEEPM]) if config_experiment[tc.SSLEEPM] != '' else 1
        Modulacion.SLEEP_tyh = int(config_experiment[tc.SSLEEPTYH]) if config_experiment[tc.SSLEEPTYH] != '' else 59
        Modulacion.Vcc = int(config_experiment[tc.SVCC]) if config_experiment[tc.SVCC] != '' else 5
        Modulacion.Temp22 = config_experiment[tc.STEMPPORT] if config_experiment[tc.STEMPPORT] != '' else 'P8_11'
        Modulacion.electrovalvulas = config_experiment[tc.SELECPORTS] if config_experiment[tc.SELECPORTS] != [''] else ['P8_10','P8_12','P8_14','P8_16']
        Modulacion.sensorTemp22 = Modulacion.TyH_sensor[config_experiment[tc.SSENTYPE]]
        Modulacion.tsub = Modulacion.T / Modulacion.NM
        Modulacion.electrpos = config_experiment[tc.SVALPOS]
        Modulacion.capturas_iniciales = [4] if Modulacion.electrpos != 'R' else [1,2,3]
        Modulacion.queue = qu.Queue() # Creo la cola de mensaje global
        #Modulacion.event_TyH = Event() # Evento para sincronizar los hilos de captura y de escritura
        #Modulacion.event_TyH.set() # Lo ponemos a 1 para evitar un bloqueo
        Modulacion.event_write_thread = Event() 
        self.activar_GPIO_valvulas() # Puede ser un foco de problemas, puede que haya que cambiarlo

    def daemonizar(stdin='stdin.txt',stdout='stdout.txt',stderr='stderr.txt'): 
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.sderr.write("fork #1 failed: (%d) %s\n" % (e.eerno, e.streerror))
            sys.exit(1)

        #Separar entorno padre
        #os.chdir("/")
        os.umask(0)
        os.setsid()
        #Realizar segundo fork

        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.sderr.write("fork #2 failed: (%d) %s\n" % (e.eerno, e.streerror))
            sys.exit(1)

        for f in sys.stdout, sys.stderr,sys.stdin: f.flush()
        si = open("salida_in.txt", 'a+')
        so = open("salida_out.txt", 'w')
        se = open("salida_err.txt", 'w')
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        Modulacion.file_daemon = open('file_daemon.txt','w+')
        Modulacion.file_daemon.write("%d\n" % os.getpid())
        Modulacion.file_daemon.close()

    def activar_GPIO_valvulas(self):
        for elec in Modulacion.electrovalvulas:
            GPIO.setup(elec,GPIO.OUT)

    def create_files(self,nameFile,path,folder,samplesinicio):
        """
        Crea los ficheros para escribir
        Crea los ficheros necesarios para guardar todos los datos de las
        experimentaciones.
        Parametros:
        nameFile -- nombre que va a usarse para crear los ficheros que contendran los datos y 
        el resto de la informacion
        path -- ruta donde se va a guardar el fichero
        folder -- nombre de la carpeta donde va a guardarse el archivo
        
        Retorno:
        devolver -- array con los gases que van a entrar al sensor
        """
        datenow = datetime.now()

        fileString = nameFile+"_txt_" +datenow.strftime('%Y-%m-%d_%H-%M-%S')+".txt"
        fileString_data = nameFile+"_dat1_"+datenow.strftime('%Y-%m-%d_%H-%M-%S')+".dat"
        #fileString_tyh = "TyH"+nameFile+"_data_"+datenow.strftime('%Y-%m-%d_%H-%M-%S')+".data"

        ruta1 = path+"/"+self.time_mark.strftime("%Y%m%d")+"/"+folder+"/dat/" #Ruta de salida       
        if not os.path.exists(ruta1): os.makedirs(ruta1,mode=0o755)     #Si la ruta no existe, se crea
        ruta2 = path+"/"+self.time_mark.strftime("%Y%m%d")+"/"+folder+"/txt/" #Ruta de salida
        if not os.path.exists(ruta2): os.makedirs(ruta2,mode=0o755)     #Si la ruta no existe, se crea
        #ruta3 = tc.obtener_ruta(path,self.time_mark,folder,"TyH") #Ruta de salida
        #if not os.path.exists(ruta3): os.makedirs(ruta3,mode=0o755)     #Si la ruta no existe, se crea

        return ruta1.strip() + str(fileString_data),ruta2.strip() + str(fileString)#,ruta3.strip() + str(fileString_tyh)

    def file_TGS2600(self,ruta,nameFile,nameFile_data1,nameFile_tyh,vec_anal_odor,succion,heat2600,tiempo,switch,tespera,samplesinicio):
        Modulacion.queue.put([0,
            "Configuracion de la plataforma - El valor maximo de la temperatura es de 5V\n",
            "Pin del motor: %s\n"%(Modulacion.motorPin),
            "Numero de capturas ADC para una muestra: %s\n"%(Modulacion.NM),
            "Tiempo en que se realizan las NM capturas de una muestra: %s\n"%(Modulacion.T),
            "Tiempo limite de captura de una muestra: %d\n"%Modulacion.SLEEP,
            "Tiempo limite de captura de una muestra de TyH: %d\n"%(Modulacion.SLEEP_tyh),
            "Valor de VCC del circuito: %f\n"%(Modulacion.Vcc), 
            'El puerto de lectura de la humedad y temperatura es el: %s\n'%(Modulacion.Temp22),
            'Los puertos de las electrovalvulas son: %s\n'%(Modulacion.electrovalvulas),
            'Posicion de las electrovalvulas: %s\n'%(Modulacion.electrpos),
            'Sensor TGS2600\n',
            'Fecha y hora de inicio: ' + str(time.strftime("%a%d%b%Y-%HH%MM%SS", time.localtime())) + '\n',
            'Ruta del fichero: %s\n'%(ruta),
            'Nombre del fichero de datos: %s\n'%(nameFile),
            'Nombre del fichero de texto: %s\n'%(nameFile_data1),
            'Nombre del fichero de TyH: %s\n'%(nameFile_tyh),
            'Electrovalvulas (1-METANOL, 2-ETANOL, 3-BUTANOL, 4-AIRE ) \n',
            'Conmutacion entre electrovalvulas: %s\n'%(vec_anal_odor),
            'Succion motor (30-100): %d\n'%(succion),
            'Temperatura TGS2600 (1-100): %d\n'%(heat2600),
            'Duracion del experimento: %f minutos o muestras\n'%(tiempo),
            'Se ha dejado un tiempo entre captura de gases de: %d segundos'%(tespera),
            'El experimento tiene: %d muestras iniciales\n'%(samplesinicio),    
            'El tiempo de switch o conmutacion de las electrovalvulas es de: %d segundos\n'%(switch)])
        return
        
    def cerrar_electrovalvulas(self):
        for electrovalvula in Modulacion.electrovalvulas:
            GPIO.output(electrovalvula, GPIO.LOW)

    def abrir_electrovalvulas(self,electrovalvulas):
        for number_elect in electrovalvulas:
            GPIO.output(Modulacion.electrovalvulas[number_elect-1], GPIO.HIGH)

    def reset(self,heatPin):
        
        # Me sincronizo con el hilo de escritura para asegurarme de que ha tenido tiempo para escribir todo
        Modulacion.queue.put([0,"Experimento finalizado con exito. Fecha de finalizacion: %s\n"%(datetime.now())])
        Modulacion.queue.put(Modulacion.SYNC) 
        Modulacion.event_write_thread.wait() 
        
        self.cerrar_electrovalvulas()
        PWM.stop(Modulacion.motorPin)
        PWM.stop(heatPin)
        PWM.cleanup()
        fecha_fin = datetime.now()
        self.f.close()
        self.g.close()
        return

    def captura_odorante(self):
        raise Exception("subclasses must override captura_odorante()!")

    def valor_sensor(self):
        raise Exception("subclasses must override valor_sensor()!")

    def imprimir_cabecera(self):
        raise Exception("subclasses must override imprimir_cabecera()!")

    def measure_tyh(self):

        self.thread = currentThread()

        #Lectura humedad y temperatura
        while getattr(self.thread,"do_run",True):
            # Fijo bloqueo para actualizar valores de TyH
            #self.event_TyH.wait()
            tick_HT = time.time()
            self.humidity, self.temperature = DHT.read_retry(Modulacion.sensorTemp22,Modulacion.Temp22,30,1,None)
            t_HT = time.time()-tick_HT
            instante = datetime.now()
            #self.event_TyH.set() # Finalizo bloqueo una vez que he actualizado los valores
            
            #Cuanto duerme en funcion de lo que tarde en H y T
            if t_HT > Modulacion.SLEEP_tyh:
                Modulacion.queue.put([0,"Tiempo medicion H y T > SLEEP: %d\n"%(t_HT)])
            else:
                Modulacion.queue.put([0,"Tiempo medicion H y T: %d\n"%(t_HT),"Sensor DHT22: %d\n"%(Modulacion.sensorTemp22)])
                if self.humidity is not None and self.temperature is not None:
                    Modulacion.queue.put([0,'>>> %s Temp = %f, Humidity = %f \n'%(instante,self.temperature,self.humidity)])    
                else:
                    Modulacion.queue.put([0,'Failed to get reading, Try again!'])
                    
            time.sleep(Modulacion.SLEEP_tyh-(time.time()-tick_HT))

        return 0

    # Recibe una lista con un valor en la primera posición
    # 0 - Escritura en fichero global
    # 1 - Escritura en fichero de salida datos
    def hilo_escritura_datos(self):
        
        values = Modulacion.queue.get()
        while(values != Modulacion.EXIT):
            if self.f.closed == True:
                values = Modulacion.queue.get()
                continue
            elif values == Modulacion.SYNC: #CASO NECESARIO PARA SINCRONIZAR CON LA ESCRITURA DE LOS FICHEROS
                self.event_write_thread.set()
            elif values[0] == 0:
                for string in values[1:]:
                    self.g.write(string)
                    self.g.flush()
            elif values[0] == 2:
                self.f.write(values[1])
                self.f.flush()
            else:
                strf,strg,gases = values[0],values[1],values[2]
                strgasesid,strgases = '',''
                for gas in gases: # Puede haber un fallo a la hora de escribir
                    strgasesid+=str(gas)+' '
                    strgases+=Modulacion.odorantes[gas]+' '
            
                # Se selecciona hasta el caracter -1 para no escoger el último espacio
                strf+=strgasesid+strgases[:-1]+'\n'
                strg+=strgasesid+strgases[:-1]+'\n'

                self.g.write(strg)
                self.g.flush()
                self.f.write(strf)
                self.f.flush()
            values = Modulacion.queue.get()
        self.event_write_thread.set() #CASO NECESARIO CUANDO SE QUIERE MATAR AL HILO, PARA QUE EL PROGRAMA NO FINALICE SIN ACABAR CON EL HILO PRIMERO
        return 
    
    def inicializar_ficheros_puertos_hilos(self,path,succion,sw,samplesinicio,ct,nfile,nfolder,vsaodrs,arg_extra=None):
        ruta_fichero_data,ruta_fichero = Modulacion.create_files(self,nfile,path,nfolder,samplesinicio)
        self.f,self.g = os.fdopen(os.open(ruta_fichero_data, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644), 'w'),os.fdopen(os.open(ruta_fichero, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644), 'w')
        
        Modulacion.queue.put([0,'Ruta Fichero: %s\n'%(ruta_fichero),'Ruta Fichero de datos: %s\n'%(ruta_fichero_data)])
        
        # Se crea el hilo de lectura y escritura de la temperatura y humedad ambientales
        self.thread = Thread(target=self.measure_tyh,args=())
        self.thread.do_run = True
        self.thread.start()
        
        # Se arranca el motor
        PWM.start(Modulacion.motorPin,succion)

        return

    def captura_muestras(self,samplesinicio=None):
        if samplesinicio == None:
            Modulacion.queue.put([0,'Comienza la experimentacion de datos\n'])
        else:
            Modulacion.queue.put([0,'Comienza la adquisicion de %d muestras inciales\n'%(samplesinicio)])
            
        Modulacion.cerrar_electrovalvulas(self)

    def cierre_hilos(self,heatpin):
        
        PWM.start(heatpin,100)
        os.remove("file_daemon.txt")

        #Enviamos al hilo de escritura un -2, que es la senial de que finalice, y esperamos para asegurarnos de que acaba
        Modulacion.queue.put(Modulacion.EXIT)
        Modulacion.event_write_thread.wait()

        #Esperamos a que el hilo de TyH acabe
        self.thread.do_run = False
        self.thread.join()

        return
    
    def captura_aire(self,heatpin,sensorpin):
        PWM.start(heatpin,100)
        while(self.air_loop == True):
            ADC.read(sensorpin)

    def captura_datos(self,heatpin,sensorpin,*args):

        for arg in zip(self.succiones,self.switchs,self.samples_ini,self.cte,self.name_files,
            self.name_folders,self.vecs_open_valves,self.vecs_anal_odort,self.sleeps,*args):
            self.inicializar_ficheros_puertos_hilos(arg[0],arg[1],arg[2],arg[3],arg[4],arg[5],arg[6],arg[7],arg[9:])
            #self.apertura_escritura_ficheros(arg[1],arg[2],arg[3],arg[4],arg[5],arg[7],arg[9:])
            #self.inicializar_hilos_puertos(arg[0],arg[1],arg[2],arg[3],arg[4],arg[5],arg[6],arg[7],arg[9:])
            #self.capturas_muestras_iniciales(arg[2],arg[9:])
            self.captura_muestras(arg[1],arg[3],arg[6],arg[7],arg[2],arg[9:])
            self.reset(arg[8])
            if self.air_loop == True:
                self.captura_aire(heatpin,sensorpin)

        self.cierre_hilos(heatpin)
        return None
    
    def handler_signal(self,signum,frame):
        Modulacion.queue.put([0,"Se ha recibido una senial para el cambio de muestras\n"])
        self.air_loop = True if self.air_loop == False else False
        signal.signal(signal.SIGUSR1, self.handler_signal)

    def iniciar_captura_datos(self):
        signal.signal(signal.SIGUSR1, self.handler_signal)
        Thread(target=self.captura_datos).start() # Creo el hilo de captura de datos y lo inicio
        self.hilo_escritura_datos()
        return

# Puro es un caso especial de regresion, se puede quitar y ahorrar código
class Puro(Modulacion):

    Rl_2600=440
    sensorPin2600 = 'P9_38'
    heatPin2600 = ''
    path = "CAPTURAS/PURO"
    #strings nuevos = 'Valor(mV): %f, Rs(ohmios): %f, Temperatura(%5V): 100, instante_captura: %s'
    #strings = ['Valor(mV):','Rs(ohmios):','Temperatura(%5V): 100 inst_captura:']

    def __init__(self,config_experiment,**kwargs):
        super().__init__(config_experiment,config_platform,Puro.strings,**kwargs)
        Puro.Rl_2600 = int(config_experiment[tc.SRSTCE]) if config_experiment[tc.SRSTCE] != '' else 440
        Puro.sensorPin2600 = config_experiment[tc.SRDPORT] if config_experiment[tc.SRDPORT] != '' else 'P9_38'
        Puro.heatPin2600 = config_experiment[tc.SHTPORT] if config_experiment[tc.SHTPORT] != '' else ''
        Puro.path = config_experiment[tc.SSDFOLDER] if config_experiment[tc.SSDFOLDER] != '' else 'CAPTURAS/PURO'
        self.muestras = 0

    def valor_sensor(self,string,gas):
        """
        Captura muestras sin usar ninguna tecnica.
        Realiza la toma de medidas sin usar ninguna tecnica de modulacion
        Parametros:
        string -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        gas -- array que contiene los gases de la muestra que se captura
        """

        #Lectura nariz
        time_ini = time.time()
        value=0
        ADC.read(Puro.sensorPin2600) #la primera medida es erronea por el bug
        
        # Tomamos las diez muestras
        for i in range(Modulacion.NM):
            value += ADC.read(Puro.sensorPin2600)*1800
            time.sleep(Modulacion.tsub)

        # Hacemos la media
        valueTGS2600=value/Modulacion.NM
        instante_captura=datetime.now()
                
        #Se calcula el valor de la resistencia interna del sensor
        RsTGS2600=((Modulacion.Vcc*Puro.Rl_2600)/(valueTGS2600/1000.))-Puro.Rl_2600
        
        time_end = time.time()
        # Pasamos a la cola los valores que va a escribir
        Modulacion.queue.put(["%d %f %f 100 %s "%(self.muestras,valueTGS2600,RsTGS2600,instante_captura),
            "%s[%d] Valor(mV): %f Rs(ohmios): %f Temperatura(5V): 100 Instante_Captura: %s "%(string,self.muestras,valueTGS2600,RsTGS2600,instante_captura),
            gas])
        
        return (time_end - time_ini)

    def captura_odorante(self,vector_valvulas,vector_odorantes,n_muestras,string):
        """
        Capturamos tantas muestras como se indique en los argumentos
        Codigo comun para la captura de gases, que llama a la funcion de puro_TGS2600, abre y cierra las valvulas
        y mide el tiempo de captura de los gases.
        Parametros:
        vector_odorantes -- el vector de los odorantes que van a captarse en esta apertura de valvulas
        inicio -- el numero que marca el inicio de muestras que hay que coger
        fin -- el numero final de muestras que hay que coger
        string -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        """

        super().abrir_electrovalvulas(vector_valvulas)
        for count in range(n_muestras):
            value_sleep = self.valor_sensor(string,vector_odorantes)
            time.sleep(Modulacion.SLEEP - value_sleep)
            self.muestras+=1
        super().cerrar_electrovalvulas()

        return

    def file_TGS2600(self,ruta,nameFile,nameFile_data1,nameFile_tyh,vec_open_valve,succion,heat2600,tiempo,switch,tespera,samplesinicio):
        Modulacion.queue.put([0,"Algoritmo temperatura constante\n"])
        super().file_TGS2600(ruta,nameFile,nameFile_data1,nameFile_tyh,vec_open_valve,succion,heat2600,tiempo,switch,tespera,samplesinicio)
        Modulacion.queue.put([0,"Valor de la resistencia de carga: %d\n"%(Puro.Rl_2600)])
    
    def inicializar_ficheros_puertos_hilos(self,switch,samplesinicio,ct,nfile,nfolder,vsovs,vsaodrs,arg_extra=None):
        super().inicializar_ficheros_puertos_hilos(Puro.path,switch,samplesinicio,ct,nfile,nfolder,vsaodrs)
        PWM.start(Puro.heatPin2600,100)
        Modulacion.queue.put([0,"%d %d %d %d"%(switch,samplesinicio,ct,len(vsaodrs))])
        ADC.setup()
        self.file_TGS2600(Puro.path+"/"+self.time_mark.strftime("%Y%m%d")+"/"+nfolder+"/",nfile+".txt",
            nfile+".dat","TyH"+nfile+".data",vsaodrs,suc,5,float(samplesinicio + (ct*(len(vsovs)+1)) + (len(vsovs)*sw)),sw,ct,samplesinicio)

    def captura_muestras(self,sw,ct,vsovs,vsaodrs,samplesinicio,args_extra=None):
        
        # Captura muestras iniciales
        super().captura_muestras(samplesinicio)
        self.captura_odorante(Modulacion.capturas_iniciales,[4],samplesinicio,"Muestras_iniciales") 
        
        # Captura muestras para experimentacion
        super().captura_muestras()
        
        switch = sw if isinstance(sw,list) else [sw]*len(vsovs)
        for sw,vsov,vsaodr in zip(switch,vsovs,vsaodrs):
            self.captura_odorante(Modulacion.capturas_iniciales,[4],ct,"Muestra_entre_gases")
            self.captura_odorante(vsov,vsaodr,sw,"Muestra_gases")

        self.captura_odorante(Modulacion.capturas_iniciales,[4],ct,"Muestra_entre_gases")

    def reset(self,sle,arg_extra=None):
        super().reset(Puro.heatPin2600)
        self.muestras = 0
        time.sleep(sle)
        
    def captura_datos(self):
        super().captura_datos(Puro.heatPin2600,Puro.sensorPin2600)
        return Puro.path

class Regresion(Modulacion):

    Rl_2600=440
    sensorPin2600 = 'P9_40'
    heatPin2600 = 'P9_22'
    path = "CAPTURAS/REGRESION"
    strings = ['Valor(mV):','Rs(ohmios):','Temperatura(%5V):','inst_captura: ','slope:','intercept:','r_value:','p_value:','std_err1:']

    def __init__(self,config_experiment,**kwargs):
        super().__init__(config_experiment,**kwargs)
        self.tendencia = config_experiment[tc.STEND]
        self.heat = config_experiment[tc.SHTSENSOR]
        self.x=[]
        self.concentTGS2600=[]
        self.muestras = 0
        Regresion.Rl_2600 = int(config_experiment[tc.SRSTCE]) if config_experiment[tc.SRSTCE] != '' else 440
        Regresion.sensorPin2600 = config_experiment[tc.SRDPORT] if config_experiment[tc.SRDPORT] != '' else 'P9_40'
        Regresion.heatPin2600 = config_experiment[tc.SHTPORT] if config_experiment[tc.SHTPORT] != '' else 'P9_22'
        Regresion.path = config_experiment[tc.SSDFOLDER] if config_experiment[tc.SSDFOLDER] != '' else 'CAPTURAS/REGRESION'
            
    def valor_sensor(self,temperature_TGS2600,string,opcion,gas,samplesinicio,tendencia):
        """
        Captura muestras usando la tecnica de la regresion lineal
        Realiza la toma de medidas usando como tecnica de modulacion la regresion lineal 
        de la temperatura en funcion de la muestra obtenida en el sensor. 
        Parametros:
        count -- contador que indica las muestras que hemos tomado
        temperature_TGS2600 -- temperatura inicial a la que calentamos el sensor
        string -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        opcion -- 1 para las SAMPLESINICIO muestras, 2 para capturas tantas muestras como hayamos indicado
        gas -- array que contiene los gases de la muestra que se captura
        """
        time_ini = time.time()
        if opcion == 1:
            PWM.set_duty_cycle(Regresion.heatPin2600, temperature_TGS2600)

        value=0
        ADC.read(Regresion.sensorPin2600) #la primera medida es erronea por el bug

            
        for i in range(Modulacion.NM):
            value += ADC.read(Regresion.sensorPin2600)*1800
            time.sleep(Modulacion.tsub)
        
        valueTGS2600=value/Modulacion.NM
        instante_captura=datetime.now()

        slope, intercept, r_value, p_value, std_err1 = 0,0,0,0,0
        #Adaptacion temperatura
        if opcion == 2:
            # Solo usa una ventana de tantos datos como samples inicio tenga
            slope, intercept, r_value, p_value, std_err1 = stats.linregress(self.x[(self.muestras-samplesinicio):(self.muestras-1)],
                self.concentTGS2600[(self.muestras-samplesinicio):(self.muestras-1)])

            temperature_TGS2600 = temperature_TGS2600 - (slope*tendencia)

            if temperature_TGS2600 < 10.0:
                temperature_TGS2600 = 10.0
            elif temperature_TGS2600 > 90.0:
                temperature_TGS2600 = 90.0

            Modulacion.queue.put([0,"Los valores de la tendencia, el slope y la temperatura son: %f, %f y %f\n"%(tendencia,slope,temperature_TGS2600)])
            #Reset de setup PWM
            PWM.set_duty_cycle(Regresion.heatPin2600, temperature_TGS2600)

        #Se calcula el valor de la resistencia interna del sensor
        RsTGS2600=((Modulacion.Vcc*Regresion.Rl_2600)/(valueTGS2600/1000.))-Regresion.Rl_2600

        self.x.append(self.muestras)
        self.concentTGS2600.append(valueTGS2600)
        time_end = time.time()
    
        Modulacion.queue.put(["%d %f %f %f %s %f %f %f %f %f "%
                (self.muestras,valueTGS2600,RsTGS2600,temperature_TGS2600,instante_captura,slope, intercept, r_value, p_value, std_err1),
            "%s[%d] Valor(mV): %f Rs(ohmios) %f Temperatura: %f Instante Captura: %s Slope: %f Intercept: %f R_Value: %f P_Value: %f std_err1: %f "%
                (string,self.muestras,valueTGS2600,RsTGS2600,temperature_TGS2600,instante_captura,slope, intercept, r_value, p_value, std_err1),
            gas])
        return (time_end-time_ini)

    def captura_odorante(self,vector_valvulas,vector_odorantes,n_muestras,string,opcion,heat2600,samplesinicio,tendencia):

        """
        Capturamos tantas muestras como se indique en los argumentos
        Codigo comun para la captura de gases, que llama a la funcion de puro_TGS2600, abre y cierra las valvulas
        y mide el tiempo de captura de los gases.
        Parametros:
        vector_odorantes -- el vector de los odorantes que van a captarse en esta apertura de valvulas
        inicio -- el numero que marca el inicio de muestras que hay que coger
        fin -- el numero final de muestras que hay que coger
        string -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        opcion -- 1 para las SAMPLESINICIO muestras, 2 para capturas tantas muestras como hayamos indicado
        heat2600 -- temperatura inicial a la que calentamos el sensor
        """
        super().abrir_electrovalvulas(vector_valvulas)
        for count in range(n_muestras):
            value_sleep = self.valor_sensor(heat2600,string,opcion,vector_odorantes,samplesinicio,tendencia)
            time.sleep(Modulacion.SLEEP - value_sleep)
            self.muestras+=1
        super().cerrar_electrovalvulas()

    def file_TGS2600(self,ruta,nameFile,nameFile_data1,nameFile_tyh,vec_open_valve,succion,heat2600,tiempo,switch,tespera,samplesinicio,tendencia):
        Modulacion.queue.put([0,"Algoritmo temperatura variable y codificacion en amplitud\n"])
        super().file_TGS2600(ruta,nameFile,nameFile_data1,nameFile_tyh,vec_open_valve,succion,heat2600,tiempo,switch,tespera,samplesinicio)
        Modulacion.queue.put([0,"Pin PWM de calentamiento sensor: %s\n"%(self.heatPin2600),
            "Valor de la tendencia: %f\n"%(tendencia),
            "Pin ADC sensor: %s\n"%(self.sensorPin2600),
            "Valor de la resistencia de carga: %d\n"%(Regresion.Rl_2600)])

    def inicializar_ficheros_puertos_hilos(self,suc,sw,samplesinicio,ct,nfile,nfolder,vsovs,vsaodrs,arg_extra=None):
        super().inicializar_ficheros_puertos_hilos(Regresion.path,suc,sw,samplesinicio,ct,nfile,nfolder,vsaodrs)
        ADC.setup()
        PWM.start(Regresion.heatPin2600,arg_extra[0]) 
        Modulacion.queue.put([2,"%d %d %d %d"%(sw,samplesinicio,ct,len(vsaodrs))])
        self.file_TGS2600(Regresion.path+"/"+self.time_mark.strftime("%Y%m%d")+"/"+nfolder+"/",
            nfile+".txt",nfile+".dat","TyH"+nfile+".data",vsaodrs,suc,(arg_extra[0]*0.01*5),
            float(samplesinicio + (ct*(len(vsovs)+1)) + (len(vsovs)*sw)),sw,ct,samplesinicio,arg_extra[1])
       
    def captura_muestras(self,sw,ct,vsovs,vsaodrs,samplesinicio,args_extra=None):
        
        #Captura muestras iniciales
        super().captura_muestras(samplesinicio)
        self.captura_odorante(Modulacion.capturas_iniciales,[4],samplesinicio,"Muestras_iniciales",1,args_extra[0],samplesinicio,args_extra[1])

        #Captura muestras para experimentacion
        super().captura_muestras()

        switch = sw if isinstance(sw,list) else [sw]*len(vsovs)
        for sw,vsov,vsaodr in zip(switch,vsovs,vsaodrs):
            self.captura_odorante(Modulacion.capturas_iniciales,[4],ct,"Muestra_entre_gases",2,args_extra[0],samplesinicio,args_extra[1])
            self.captura_odorante(vsov,vsaodr,sw,"Muestra_gases",2,args_extra[0],samplesinicio,args_extra[1])

        self.captura_odorante(Modulacion.capturas_iniciales,[4],ct,"Muestra_entre_gases",2,args_extra[0],samplesinicio,args_extra[1])

    def reset(self,sle,arg_extra=None):
        super().reset(Regresion.heatPin2600)
        self.x,self.concentTGS2600,self.muestras=[],[],0
        time.sleep(sle)

    def captura_datos(self):
        super().captura_datos(Regresion.heatPin2600,Regresion.sensorPin2600,self.heat,self.tendencia)
        return Regresion.path

class MPID(Modulacion): #ModulationPID

    Rl_2600=440
    sensorPin2600 = 'P9_40'
    heatPin2600 = 'P9_22'
    path = "CAPTURAS/MPID"
    #strings = ['Target(mV):','Valor(mV):','Rs(ohmios):','Temperatura(%5V):','Temperatura_PID(%5V):','inst_captura: ']

    #'Muestra PID['+str(contador)+']\n>>Target: '+str(subtarget)+'V >> Valor:'+str(value)+'V >> Rs: '+str(RStgs2600)+' Temperatura: '+str(temp)+' '+' TemperaturaPID: '+str(temperaturaPID)+' '+str(captura)+'\n'

    def __init__(self,config_experiment,**kwargs):
        super().__init__(config_experiment,config_elems,MPID.strings,**kwargs)
        self.periods = config_experiment[tc.SPIDPERIOD]
        self.heat = config_experiment[tc.SHTSENSOR]
        self.Kp = list(np.array(config_experiment[tc.SALPHA])*0.6)
        self.Kd = list(np.array(self.periods)*0.125)
        self.Ki = list(np.array(self.periods)*0.5)
        self.temperature_Max_Upper_Bound = config_experiment[tc.SMAXLIMITUPPERBOUND]
        self.temperature_Min_Upper_Bound = config_experiment[tc.SMINLIMITUPPERBOUND]
        self.temperature_Max_Lower_Bound = config_experiment[tc.SMAXLIMITLOWERBOUND]
        self.temperature_Min_Lower_Bound = config_experiment[tc.SMINLIMITLOWERBOUND]
        self.max_peak_value = config_experiment[tc.SMAXPKVAL]
        self.min_peak_value = config_experiment[tc.SMINPKVAL]
        self.target = None # Target que hay que seguir
        self.max_value,self.min_value = 0,0 # Valores máximos y mínimos capturados por el sensor
        self.max_PID_temp,self.min_PID_temp = 0,0 # Valores máximos y mínimos de la temperatura del sensor
        self.errorControl = 0.05
        self.muestras = 0

        MPID.Rl_2600 = int(config_experiment[tc.SRSTCE]) if config_experiment[tc.SRSTCE] != '' else 440
        MPID.sensorPin2600 = config_experiment[tc.SRDPORT] if config_experiment[tc.SRDPORT] != '' else 'P9_40'
        MPID.heatPin2600 = config_experiment[tc.SHTPORT] if config_experiment[tc.SHTPORT] != '' else 'P9_22'
        MPID.path = config_experiment[tc.SSDFOLDER] if config_experiment[tc.SSDFOLDER] != '' else 'CAPTURAS/MPID'

        self.lastError,self.addError,self.temp = 0,0,0

    def crear_target(self,Vmax, Vmin, periodo):

        A = (Vmax - Vmin)/2.0
        B = (2*math.pi)/periodo

        signal = []

        for x in range(periodo+1):
            signal.append(round(((A*math.sin(B*x))+(A+Vmin)),3))

        self.target = signal[0:periodo]

        return

    def recalcular_target(self,temperature_Max_Upper_Bound,temperature_Min_Upper_Bound,temperature_Max_Lower_Bound,temperature_Min_Lower_Bound,period):

        max_bound,min_bound = 0,0
        if (self.max_value - self.min_value) < 150.0:
            if (self.max_value > self.min_value):
                if self.max_PID_temp > temperature_Max_Upper_Bound:
                    max_bound = math.ceil(self.max_value*0.9)
                elif self.max_PID_temp < temperature_Min_Upper_Bound:
                    max_bound = math.ceil(self.max_value*1.1)
                else:
                    max_bound = math.ceil(self.max_value)
                
                if self.min_PID_temp > temperature_Max_Lower_Bound:
                    min_bound = math.ceil(max_bound*0.1)
                elif self.min_PID_temp < temperature_Min_Lower_Bound:
                    min_bound = math.ceil(self.min_value + max_bound*0.05)
                else:
                    min_bound = math.ceil(max_bound*0.5)
            else:
                max_bound,min_bound = math.ceil(self.min_value),math.ceil(self.min_value*0.3)

            if min_bound < 100.0:
                min_bound = 100.0
                if max_bound <= (min_bound*1.25):
                    max_bound = max_bound*1.25
        else:
            if self.min_PID_temp > temperature_Max_Lower_Bound:
                min_bound = math.ceil(min(self.target)*0.95)
            elif self.min_PID_temp < temperature_Min_Lower_Bound:
                min_bound = math.ceil(min(self.target)*1.05)
            else:
                min_bound = self.min_value

            if (max(self.target) - self.max_value) > 0:
                max_bound = math.ceil(self.max_value)
            elif self.max_PID_temp > temperature_Max_Upper_Bound:
                max_bound = math.ceil(max(self.target)*0.98)
            elif self.max_PID_temp < temperature_Min_Upper_Bound:
                max_bound = math.ceil(max(self.target)*1.02)

        if max_bound < min_bound:
            max_bound,min_bound = min_bound,max_bound
        
        if max_bound > 1800.0:
            max_bound = 1800.0
        if min_bound < 0.0:
            min_bound = 1800.0*0.01

        self.crear_target(max_bound,min_bound,period)

        return

    def PID_controller(self, Kp, Kd, Ki, target_point, sensor_point, lastError, addError):

        error = round((target_point - sensor_point),3)
        deltaTime = 1.0
        deltaError = error - lastError

        ep = error
        ed = deltaError/deltaTime
        ei = addError + (error*deltaTime)

        output = Kp *(ep+(Kd*ed) + ((1/Ki)*ei))

        return output,error,ei

    def calculate_min_max_value(self, subtarget, valueTGS2600, func, variable, tempPID, selftempPID):

        if subtarget == func(self.target):
            e = subtarget*self.errorControl
            selftempPID = tempPID
            if not(valueTGS2600 >= (subtarget-e) and valueTGS2600 <= (subtarget+e)):
                variable = valueTGS2600
            else:
                variable = func(self.target)

        return selftempPID,variable

    def valor_sensor(self,string, gas, subtarget, Kp, Kd, Ki, temperaturaMaxUpperBound, temperaturaMinLowerBound):
        """
        Captura muestras usando la tecnica de Martinelli
        Realiza la toma de medidas usando como tecnica la descrita por Martinelli
        Parametros:
        stringA -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        stringB -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        gas -- array que contiene los gases de la muestra que se captura
        """

        #Lectura nariz
        time_ini = time.time()
        value=0
        ADC.read(Puro.sensorPin2600) #la primera medida es erronea por el bug
        
        # Tomamos las diez muestras
        for i in range(Modulacion.NM):
            value += ADC.read(MPID.sensorPin2600)*1800
            time.sleep(Modulacion.tsub)

        # Hacemos la media
        valueTGS2600=value/Modulacion.NM
        instante_captura=datetime.now()

        output,error,ei = self.PID_controller(Kp,Kd,Ki,subtarget,valueTGS2600,self.lastError,self.addError)
        
        t1 = (output - max(self.target))*(((temperaturaMinLowerBound - temperaturaMaxUpperBound)/-max(self.target)))+temperaturaMaxUpperBound if error < -0.5 or error > 0.5 else 0

        if (self.temp < temperaturaMaxUpperBound or self.temp == temperaturaMaxUpperBound) and (error < 0):
            temperaturaPID = self.temp - t1 if t1 > 0 else self.temp + t1
        elif ((self.temp > temperaturaMaxUpperBound) and (error < 0)) or ((self.temp < temperaturaMaxUpperBound) and (error > 0)):
            temperaturaPID = self.temp + t1
        else:
            temperaturaPID = self.temp

        if temperaturaPID > temperaturaMaxUpperBound:
            temperaturaPID = temperaturaMaxUpperBound
        elif temperaturaPID < temperaturaMinLowerBound:
            temperaturaPID = temperaturaMinLowerBound

        PWM.set_duty_cycle(MPID.heatPin2600, temperaturaPID)
        RSTGS = ((Modulacion.Vcc*MPID.Rl_2600)/(valueTGS2600/1000.0)) - MPID.Rl_2600

        time_end = time.time()
        Modulacion.queue.put(["%d %f %f %f %f %s "%
                (self.muestras,subtarget,valueTGS2600,RSTGS,self.temp,temperaturaPID,instante_captura),
            "%s[%d] Target(mV): %f Valor(mV): %f Rs(ohmios) %f Temperatura(%5V): %f Temperatura_PID(%5V): %f Instante Captura: %s"%
                (string,self.muestras,valueTGS2600,RSTGS,self.temp,temperaturaPID,instante_captura,instante_captura),
            gas])

        self.lastError, self.addError, self.temp = error,ei,temperaturaPID
        return [time_end - time_ini,valueTGS2600]

    def captura_odorante(self,vector_valvulas,vector_odorantes,n_muestras,string,periodo, Kp, Kd, Ki, 
        temperature_Max_Upper_Bound,temperature_Min_Upper_Bound,temperature_Max_Lower_Bound,temperature_Min_Lower_Bound):
        """
        Capturamos tantas muestras como se indique en los argumentos
        Codigo comun para la captura de gases, que llama a la funcion de puro_TGS2600, abre y cierra las valvulas
        y mide el tiempo de captura de los gases.
        Parametros:
        vector_odorantes -- el vector de los odorantes que van a captarse en esta apertura de valvulas
        inicio -- el numero que marca el inicio de muestras que hay que coger
        fin -- el numero final de muestras que hay que coger
        string -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        """

        super().abrir_electrovalvulas(vector_valvulas)
        for count in range(n_muestras):

            if self.muestras % periodo == 0 and self.muestras != 0:
                Modulacion.queue.put([0,"Se procede a recalcular el target\n"])
                self.recalcular_target(temperature_Max_Upper_Bound,temperature_Min_Upper_Bound,temperature_Max_Lower_Bound,temperature_Min_Lower_Bound,periodo)

            subtarget = self.target[self.muestras%periodo]
            ret_values = self.valor_sensor(string,vector_odorantes, subtarget, Kp, Kd, Ki, temperature_Max_Upper_Bound, temperature_Min_Lower_Bound)
            time.sleep(Modulacion.SLEEP - ret_values[0])
            
            self.max_PID_temp,self.max_value = self.calculate_min_max_value(subtarget, ret_values[1], max, self.max_value, self.temp, self.max_PID_temp)
            self.min_PID_temp,self.min_value = self.calculate_min_max_value(subtarget, ret_values[1], min, self.min_value, self.temp, self.min_PID_temp)
            self.muestras+=1

        super().cerrar_electrovalvulas()

        return 

    def file_TGS2600(self,ruta,nameFile,nameFile_data1,nameFile_tyh,vec_open_valve,succion,
        heat2600,tiempo,switch,tespera,samplesinicio,period,Kp,Ki,Kd,temperature_Max_Upper_Bound,temperature_Min_Upper_Bound,
        temperature_Max_Lower_Bound,temperature_Min_Lower_Bound,maximum_peak_value,minimum_peak_value):
        
        Modulacion.queue.put([0,"Algoritmo modulacion por PID en lazo cerrado\n"])
        super().file_TGS2600(ruta,nameFile,nameFile_data1,nameFile_tyh,vec_open_valve,succion,heat2600,tiempo,switch,tespera,samplesinicio)
        Modulacion.queue.put([0,"Pin PWM de calentamiento sensor: %s\n"%(self.heatPin2600),
            "Pin ADC sensor: %s\n"%(self.sensorPin2600),
            "Valor de la resistencia de carga: %d\n"%(MPID.Rl_2600),
            "Control Proporcional: %f\n"%(Kp),
            "Control Integral: %f\n"%(Ki),
            "Control Derivativo: %f\n"%(Kd),
            "Periodo de la senial: %d\n"%(period),
            "Limite maximo superior: %d\n"%(temperature_Max_Upper_Bound),
            "Limite minimo superior: %d\n"%(temperature_Min_Upper_Bound),
            "Limite maximo inferior: %d\n"%(temperature_Max_Lower_Bound),
            "Limite minimo inferior: %d\n"%(temperature_Min_Lower_Bound),
            "Valor pico inicial maximo: %f\n"%(maximum_peak_value),
            "Valor pico inicial minimo: %f\n"%(minimum_peak_value)])
    
    def inicializar_ficheros_puertos_hilos(self,switch,samplesinicio,ct,nfile,nfolder,vsaodrs,arg_extra=None):
        super().inicializar_ficheros_puertos_hilos(Puro.path,switch,samplesinicio,ct,nfile,nfolder,vsaodrs,arg_extra)
        PWM.start(MPID.heatPin2600,arg_extra[0])
        Modulacion.queue.put([0,"%d %d %d %d"%(switch,samplesinicio,ct,len(vsaodrs))])
        ADC.setup()
        self.file_TGS2600(MPID.path+"/"+self.time_mark.strftime("%Y%m%d")+"/"+nfolder,nfile+".txt",nfile+".dat","TyH"+nfile+".data",
            vsaodrs,suc,str(arg_extra[1]*0.01*5)+"V",float(samplesinicio + (ct*(len(vsovs)+1)) + (len(vsovs)*sw)),sw,ct,samplesinicio,
            arg_extra[0],arg_extra[2],arg_extra[3],arg_extra[4],arg_extra[5],arg_extra[6],arg_extra[7],arg_extra[8],arg_extra[9], arg_extra[10])
        self.crear_target(arg_extra[9], arg_extra[10], arg_extra[0])        

    def auxiliar_capturas_muestras_iniciales(self,samplesinicio):
        super().captura_muestras(samplesinicio)
        
        super().abrir_electrovalvulas(Modulacion.capturas_iniciales)
        heatTGS,value = np.linspace(0,100,samplesinicio),0
        for count,heat in enumerate(heatTGS):
            time_ini = time.time()
            PWM.set_duty_cycle(MPID.heatPin2600, heat)
        
            for i in range(Modulacion.NM):
                value += ADC.read(MPID.sensorPin2600)*1800
                time.sleep(Modulacion.tsub)

            # Hacemos la media
            valueTGS2600=value/Modulacion.NM
            instante_captura=datetime.now()
            RSTGS = ((Modulacion.Vcc*MPID.Rl_2600)/(valueTGS2600/1000.0)) - MPID.Rl_2600

            time.sleep(Modulacion.SLEEP - (time.time() - time_ini))
            Modulacion.queue.put(["%d %f %f %f %s "%
                (self.muestras,valueTGS2600,RsTGS2600,temperature_TGS2600,instante_captura),
            "Muestras_iniciales[%d] Valor(mV): %f Rs(ohmios) %f Temperatura(%5V): %f Instante Captura: %s "%
                (string,self.muestras,valueTGS2600,RsTGS2600,temperature_TGS2600,instante_captura),
            [4]])
            
        super().cerrar_electrovalvulas()
        return False

    def captura_muestras(self,sw,ct,vsovs,vsaodrs,args_extra=None):
        # Realizamos las capturas de las muestras iniciales
        auxiliar_capturas_muestras_iniciales(args_extra[1]) # Le pasamos las muestras iniciales
        
        # Realizamos las capturas de las muestras
        super().captura_muestras()
        
        switch = sw if isinstance(sw,list) else [sw]*len(vsovs)
        for sw,vsov,vsaodr in zip(switch,vsovs,vsaodrs):
            self.captura_odorante(Modulacion.capturas_iniciales,[4],ct,"Muestra_entre_gases",args_extra[0],args_extra[2],args_extra[3],args_extra[4],args_extra[5],args_extra[6],args_extra[7],args_extra[8])
            self.captura_odorante(vsov,vsaodr,sw,"Muestra_gases",args_extra[0],args_extra[2],args_extra[3],args_extra[4],args_extra[5],args_extra[6],args_extra[7],args_extra[8])

        self.captura_odorante(Modulacion.capturas_iniciales,[4],ct,"Muestra_entre_gases",args_extra[0],args_extra[2],args_extra[3],args_extra[4],args_extra[5],args_extra[6],args_extra[7],args_extra[8])

    def reset(self,sle,arg_extra=None):
        super().reset(MPID.heatPin2600)
        self.lastError,self.addError,self.temp = 0,0,0
        self.max_value,self.min_value = 0,0
        self.max_PID_temp,self.min_PID_temp = 0,0
        self.muestras = 0
        time.sleep(sle)
        
    def captura_datos(self):

        super().captura_datos(self.periods,self.heat,self.Kp,self.Kd,self.Ki,self.temperature_Max_Upper_Bound,
            self.temperature_Min_Upper_Bound,self.temperature_Max_Lower_Bound,self.temperature_Min_Lower_Bound,
            self.max_peak_value,self.min_peak_value)
        return MPID.path

# REVISARLO A FONDO -> COSAS COMO VSADR, PARA MARCAR LOS NOMBRES DE LAS VALVULAS QUE ABRO
class Martinelli(Modulacion):

    Rl_2600=27000
    sensorPin555 = 'P9_12'
    heatPin2600 = 'P9_14'
    path = "CAPTURAS/MARTINELLI"
    strings = ['Count: ',' t_up: ',' t_down: ',' Durancion pulso: ',' Heat(%3.3V): ',' Instante captura inicial: ',' Instante captura final: ', ' Gas(es) captados e identidicadores:']


    def __init__(self,config_experiment='',config_platform='',**kwargs):
        super().__init__(config_experiment,config_platform,Martinelli.strings,**kwargs)
        self.execution_modes = config_experiment[tc.SMMEXE]
        self.temperature_modes = config_experiment[tc.SMMTEM]
        self.Tmins = config_experiment[tc.SMTMIN]
        self.Tmaxs = config_experiment[tc.SMTMAX]
        self.thread_temp = None
        Martinelli.Rl_2600 = int(config_platform[tc.SRSTCE]) if config_platform[tc.SRSTCE] != '' else 27000
        Martinelli.sensorPin555 = config_platform[tc.SRDPORT] if config_platform[tc.SRDPORT] != '' else 'P9_12'
        Martinelli.heatPin2600 = config_platform[tc.SHTPORT] if config_platform[tc.SHTPORT] != '' else 'P9_14'
        Martinelli.path = config_platform[tc.SSDFOLDER] if config_platform[tc.SSDFOLDER] != '' else 'CAPTURAS/MARTINELLI'
        GPIO.setup(Martinelli.sensorPin555,GPIO.IN)

    def martinelli_thread_temperature(self,fd,Tmin,Tmax):

        tf = currentThread()
        value,secs,times,temperature_TGS2600,flag = 1,-1,0,Tmin-1,False
        
        while getattr(tf,"global_variable",True):
            while getattr(tf,"partial_variable",True):
                time_ini = time.time()
                if times % 8 == 0 and flag == False and times > 0: 
                    value*=-1
                flag = True
                temperature_TGS2600+=value
                secs+=1
                if temperature_TGS2600 > Tmax:
                    temperature_TGS2600 = Tmax
                if temperature_TGS2600 < Tmin:
                    temperature_TGS2600 = Tmin
                PWM.set_duty_cycle(Martinelli.heatPin2600, temperature_TGS2600)
                fd.writelines(str(times)+' '+str(secs)+' '+str(temperature_TGS2600)+' '+str(datetime.now())+'\n')
                fd.flush()              
                time.sleep(Modulacion.SLEEP - (time.time() - time_ini))

            if flag == True:
                times+=1
                flag = False
            

        fd.close()

    def adjust_temperature_TGS(self,mode_temperature,periodo,subperiodo,Tmin,Tmax):

        if mode_temperature == 1:
            if periodo == 0:
                return Tmin
            else:
                return Tmax
        else:
            if periodo == 0:
                return Tmax - (((Tmax-Tmin)/8)*(subperiodo+1))
            else:
                return Tmin + (((Tmax-Tmin)/8)*(subperiodo+1))  

    def valor_sensor(self,string, gas, mode_temperature, Tmin, Tmax):
        """
        Captura muestras usando la tecnica de Martinelli
        Realiza la toma de medidas usando como tecnica la descrita por Martinelli
        Parametros:
        stringA -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        stringB -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        gas -- array que contiene los gases de la muestra que se captura
        """
        
        count = 0
        sumatorio = 0

        #Realizamos dos tomas de 8 cada una,16 en total, variando unicamente la temperatura
        for i in range(2):
            #Cogemos 8 muestras, las escribimos en un fichero, y luego otras 8
            for j in range(8):

                #Fijamos la temperatura
                temperature_TGS2600 = self.adjust_temperature_TGS(mode_temperature,i,j,Tmin,Tmax)
                if mode_temperature != 3:
                    PWM.set_duty_cycle(self.heatPin2600, temperature_TGS2600)
                
                #Espera pulso de caida
                instante_captura_ini=datetime.now() #Lo pongo afuera para que no interfiera en la captura. 
                GPIO.wait_for_edge(self.sensorPin555, GPIO.FALLING,500000) # El numero es un timeout de 500000 milisegundos     
                ini_pulso = time.time()
                if mode_temperature == 3:
                    self.thread_temp.partial_variable = True
                
                GPIO.wait_for_edge(self.sensorPin555, GPIO.RISING,500000)
                ini_up = time.time()

                GPIO.wait_for_edge(self.sensorPin555, GPIO.FALLING,500000)      #Espera pulso de bajada
                fin_pulso = time.time()
                if mode_temperature == 3:
                    self.thread_temp.partial_variable = False
                instante_captura=datetime.now()

                time_down = ini_up - ini_pulso
                time_up = fin_pulso - ini_up        #Duracion del pulso en estado alto
                time_pulso = fin_pulso - ini_pulso      #Duracion del pulso completo

                sumatorio+=time_pulso
                Modulacion.queue.put([string,count,time_up,time_down,temperature_TGS2600,instante_captura_ini,instante_captura,gas])

                #print ('Muestra '+stringA+'['+str(count)+']\n>> t_up='+str(time_up)+'  >> t_down: '+str(time_down)+ '  >> Duracion pulso: '+str(time_pulso))
                #print ('>> Heat: '+str(temperature_TGS2600)+'  >> '+str(instante_captura)+'\n')
            
                #Se escriben los datos en el fichero
                #wline_g=str(count)+'   '+str(time_up)+'    '+str(time_down)+'      '+str(time_pulso)+'     '+str(temperature_TGS2600)+' '+str(instante_captura_ini)+'      '+str(instante_captura)
                #for elem in gas:
                #       wline_g+=' '+ str(elem) +' '+ Modulacion.odorantes[elem]
                #wline_g+='\n'
                #wline_f= stringB+'['+str(count)+'      Heat: '+str(temperature_TGS2600)+']     t_up='+str(time_up)+'   t_down: '+str(time_down)+'      Instante captura inicial: '+str(instante_captura_ini)+ '     Durancion pulso: '+str(time_pulso)+'>> '+str(instante_captura)+'\n'
                #self.g.writelines(wline_g)
                #self.g.flush()
                #self.f.writelines(wline_f)
                #self.f.flush()
                count+=1

        return sumatorio

    def captura_odorante(self,string,i,vector_odorantes,mode_execution,mode_temperature,Tmin,Tmax):

        """
        Capturamos los 16 pulsos del gas.
        Codigo comun para la captura de gases, que llama a la funcion de martinelli, abre y cierra las valvulas
        y mide el tiempo de captura de los gases.
        Parametros:
        stringA -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        stringB -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        stringC -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        i -- contador que muestra cuantos veces hemos capturado muestras
        vector_odorantes -- el vector de los odorantes que van a captarse en esta apertura de valvulas
        """

        #time_martinelli_ini = time.time()
        time_martinelli = self.valor_sensor(string,vector_odorantes,mode_temperature,Tmin,Tmax)
        #time_martinelli = time.time()-time_martinelli_ini
        instante_captura = datetime.now()
        print ('\n'+string+str(i)+' Duracion de los k=16 pulsos:'+str(time_martinelli)+' >> '+str(instante_captura)+'\n')
        wline_f = string+str(i)+' Duracion de los k=16 pulsos:'+str(time_martinelli)+' >> '+str(instante_captura)+'\n'
        #wline_k = str(i) + ' ' + str(time_martinelli) + ' ' + str(instante_captura) + '\n'
        self.f.writelines(wline_f)
        self.f.flush()
        #self.k.writelines(wline_k)
        #self.k.flush()

        if mode_execution == 1:
            return time_martinelli
        else:
            return 1

    def file_TGS2600(self,ruta,nameFile,nameFile_data1,nameFile_data2,nameFile_tyh,vec_open_valve,succion,heat2600,tiempo,switch,tespera,samplesinicio,mode_execution,mode_temperature,Tmin,Tmax):
        self.f.write('Algoritmo temperatura variable y codificacion en frecuencia\n')
        super().file_TGS2600(ruta,nameFile,nameFile_data1,nameFile_tyh,vec_open_valve,succion,heat2600,tiempo,switch,tespera,samplesinicio)
        self.f.write ('Nombre del fichero de datos 2: ' + str(nameFile_data2) + '\n')
        self.f.write('Pin PWM de calentamiento sensor: ' + str(self.heatPin2600)+ '\n')
        self.f.write('Pin ADC sensor: ' + str(self.sensorPin555) + '\n')
        self.f.write('Modo de ejecucion: ' + str(mode_execution)+'\n')
        self.f.write('Modo de cambio de temperatura: ' + str(mode_temperature)+'\n')
        self.f.write('Temperatura minima del sensor: '+str(Tmin)+'\n')
        self.f.write('Temperatura maxima del sensor: '+str(Tmax) + '\n')

    def apertura_escritura_ficheros(self,sw,samplesinicio,ct,nfile,nfolder,vsaodrs,arg_extra):
        
        super().apertura_escritura_ficheros(Martinelli.path,sw,samplesinicio,ct,nfile,nfolder,vsaodrs)
        #ruta_carpeta_2 = tc.obtener_ruta(Martinelli.path,self.time_mark,nfolder,'dat2')
        #if not os.path.exists(ruta_carpeta_2): os.makedirs(ruta_carpeta_2)     #Si la ruta no existe, se crea
        #ruta_fichero_data2 = ruta_carpeta_2.strip() + str(nfile+'_dat2_' + time.strftime("%a%d%b%Y-%HH%MM%SS",time.localtime())+".dat")    
        #self.k = open(ruta_fichero_data2, "w+")

        self.g.writelines(str(arg_extra[0]) + ' ' + str(arg_extra[1]) + ' ' + str(sw)+' '+str(samplesinicio)+' '+str(ct)+' '+str(len(vsaodrs))+' '+str(arg_extra[2])+' '+str(arg_extra[3])+'\n')

    def inicializar_hilos_puertos(self,suc,sw,samplesinicio,ct,nfile,nfolder,vsovs,vsaodrs,arg_extra):
        #Llamada al thread de medida de temperatura y humedad
        super().inicializar_hilos_puertos(suc)
        PWM.start(Martinelli.heatPin2600,arg_extra[2])#,20000,0)
        
        self.file_TGS2600(tc.obtener_ruta(Martinelli.path,self.time_mark,nfolder,''),nfile+".txt",nfile+".dat",
            str(nfile+'_dat2_' + time.strftime("%a%d%b%Y-%HH%MM%SS",time.localtime())+".dat"),"TyH"+nfile+".data",vsaodrs,
            suc,str(arg_extra[2]*0.01*5)+"V",float(samplesinicio + (ct*(len(vsovs)+1)) + (len(vsovs)*sw)),sw,ct,samplesinicio,
            arg_extra[0],arg_extra[1],arg_extra[2],arg_extra[3])

        if arg_extra[1] == 3:
            self.thread_temp = Thread(target=martinelli_thread_temperature,args=(open(obtener_ruta(Martinelli.path,self.time_mark,nfolder,
                'dat')+"temperature_martinelli"+time.strftime("%a%d%b%Y-%HH%MM%SS",time.localtime())+".dat","w"),arg_extra[2],arg_extra[3]))
            self.thread_temp.global_variable = True
            self.thread_temp.partial_variable = False
            self.thread_temp.start()

    def capturas_muestras_iniciales(self,samplesinicio,args_extra):
        super().capturas_muestras_iniciales(samplesinicio)
            
        #TOMAMOS X MUESTRAS DE INICIO
        super().abrir_electrovalvulas(Modulacion.capturas_iniciales)
        for i in range(samplesinicio):
            self.captura_odorante('Muestra_ini',i,Modulacion.capturas_iniciales,args_extra[0],args_extra[1],args_extra[2],args_extra[3])
        super().cerrar_electrovalvulas()

    def sub_captura_muestras(self,w,vsov,vsaodr,sw,mode_execution,mode_temperature,Tmin,Tmax):

        tiempo_valve = 0
        super().abrir_electrovalvulas(vsov)
        while tiempo_valve < sw: # Capturas tanto tiempo como conmutacion desees
            tiempo_valve +=self.captura_odorante('Muestra_odorante',w,vsaodr,mode_execution,mode_temperature,Tmin,Tmax)
            print ('Tiempo acumulado = '+str(tiempo_valve))
        super().cerrar_electrovalvulas()
        w+=1

        return w

    def captura_muestras(self,sw,ct,vsovs,vsaodrs,args_extra):
        super().captura_muestras()

        w = 0
        for vsov,vsaodr in zip(vsovs,vsaodrs):

            w = self.sub_captura_muestras(w,Modulacion.capturas_iniciales,Modulacion.capturas_iniciales,
                ct,args_extra[0],args_extra[1],args_extra[2],args_extra[3])

            w = self.sub_captura_muestras(w,vsov,vsaodr,sw,args_extra[0],args_extra[1],args_extra[2],args_extra[3])

            w = self.sub_captura_muestras(w,Modulacion.capturas_iniciales,Modulacion.capturas_iniciales,
                ct,args_extra[0],args_extra[1],args_extra[2],args_extra[3])

        return

    def cierre(self,sle,arg_extra):
        super().cierre(self.heatPin2600)
        self.k.close()
        if arg_extra[1] == 3:
            self.thread_temp.global_variable = False
            self.thread_temp.join()
        time.sleep(sle)

    def captura_datos(self):

        super().captura_datos(self.execution_modes,self.temperature_modes,self.Tmins,self.Tmaxs)
        super().cierre_hilo_escritura() 
        return Martinelli.path

# ----------------------------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------------------------------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------------------------------------------------------------------- #
class ImpulsosElectricos(Modulacion):

    Rl_2600=440
    sensorPin2600 = 'P9_40'
    heatPin2600 = 'P9_22'

    def __init__(self,succiones,switchs,samples_ini,cte,name_files,name_folders,vecs_open_valves,sleeps,ahora):
        Modulacion.__init__(succiones,switchs,samples_ini,cte,name_files,name_folders,vecs_open_valves,sleeps,ahora)
        self.x=[]
        self.concentTGS2600=[]
        self.muestras = 0

    def imprimir_cabecera(self,vecs,samplesinicio,ct,sw):
        time = float(samplesinicio + (ct*(len(vecs)+1)) + (len(vecs)*sw))
        print ('Algoritmo: heating voltage impulses')
        print ('Sensor: TGS2600    Pin ADC: ' + self.sensorPin2600)
        Modulacion.imprimir_cabecera(suc,sw,samplesinicio,ct,namefile,namefolder,vecs)
        #print 'Tendencia: ' +str(tendencia)
        #print 'Calentamiento promedio: ' + str(heat) + '%    TGS2600 Pin PWM : ' +self.heatPin2600 + '\n'
    
    #################################################################################################################################
    def valor_sensor(self,count,temperature_TGS2600,string,opcion,gas,samplesinicio,tendencia):
        """
        Captura muestras usando la tecnica de la regresion lineal
        Realiza la toma de medidas usando como tecnica de modulacion la regresion lineal 
        de la temperatura en funcion de la muestra obtenida en el sensor. 
        Parametros:
        count -- contador que indica las muestras que hemos tomado
        temperature_TGS2600 -- temperatura inicial a la que calentamos el sensor
        string -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        opcion -- 1 para las SAMPLESINICIO muestras, 2 para capturas tantas muestras como hayamos indicado
        gas -- array que contiene los gases de la muestra que se captura
        """
        
        if opcion == 1:
            PWM.set_duty_cycle(Regresion.heatPin2600, temperature_TGS2600)

        value=0
        queda=0
        residuo=0
        ADC.read_raw(Regresion.sensorPin2600) #la primera medida es erronea por el bug

        for i in range(Modulacion.NM):
            value += ADC.read_raw(Regresion.sensorPin2600)
            time.sleep(Modulacion.tsub)
        
        valueTGS2600=value/Modulacion.NM
        instante_captura=datetime.now()

        #Adaptacion temperatura
        if opcion == 2:
            # Solo usa una ventana de tantos datos como samples inicio tenga
            slope, intercept, r_value, p_value, std_err1 = stats.linregress(self.x[(count-samplesinicio):(count-1)],
                self.concentTGS2600[(count-samplesinicio):(count-1)])

            temperature_TGS2600 = temperature_TGS2600 - (slope*tendencia)

            if temperature_TGS2600 < 10.0:
                temperature_TGS2600 = 10.0
            elif temperature_TGS2600 > 90.0:
                temperature_TGS2600 = 90.0

            print ("Los valores de la tendencia, el slope y la temperatura son: "+str(tendencia)+", "+str(slope)+" y "+str(temperature_TGS2600))
            #Reset de setup PWM
            PWM.set_duty_cycle(Regresion.heatPin2600, temperature_TGS2600)

        #Se calcula el valor de la resistencia interna del sensor
        RsTGS2600=((Modulacion.Vc*Regresion.Rl_2600)/(valueTGS2600/1000.))-Regresion.Rl_2600

        self.x.append(count)
        self.concentTGS2600.append(valueTGS2600)

        #Escritura por pantalla de la lectura
        print (string+'['+str(count)+']\n>> Valor: '+str(valueTGS2600)+'mV >> Rs: '+str(RsTGS2600)+' >> Temperatura:'+str(temperature_TGS2600)+' >> '+str(instante_captura)+'\n')

        #Se escriben los datos en el fichero
        wline_g=str(count)+' '+str(valueTGS2600)+' '+str(RsTGS2600)+' '+str(temperature_TGS2600)+' '+str(instante_captura)
        for elem in gas:
            wline_g+=' '+ str(elem) +' '+ Modulacion.odorantes[elem]
        wline_g+='\n'
        wline_f=string+'['+str(count)+']    Valor:'+str(valueTGS2600)+'mV -- Rs: '+str(RsTGS2600)+' --Temperatura: '+str(temperature_TGS2600)+'     >>'+str(instante_captura)+' Gas(Gases) captados e identificadores:'
        for elem in gas:
            wline_f+=' '+ str(elem) +' '+ Modulacion.odorantes[elem]
        wline_f+='\n'
        Modulacion.g.write(wline_g)
        Modulacion.g.flush()
        Modulacion.f.write(wline_f)
        Modulacion.f.flush()

    def captura_odorante(self,vector_odorantes,n_muestras,string,opcion,heat2600,samplesinicio,tendencia):

        """
        Capturamos tantas muestras como se indique en los argumentos
        Codigo comun para la captura de gases, que llama a la funcion de puro_TGS2600, abre y cierra las valvulas
        y mide el tiempo de captura de los gases.
        Parametros:
        vector_odorantes -- el vector de los odorantes que van a captarse en esta apertura de valvulas
        inicio -- el numero que marca el inicio de muestras que hay que coger
        fin -- el numero final de muestras que hay que coger
        string -- cadena que indica si una muestra es inicial o no, se usa al imprimir en los ficheros
        opcion -- 1 para las SAMPLESINICIO muestras, 2 para capturas tantas muestras como hayamos indicado
        heat2600 -- temperatura inicial a la que calentamos el sensor
        """
        
        print(heat2600,"HEAT")
        Modulacion.abrir_electrovalvulas(vector_odorantes)
        for count in range(n_muestras):
            time_ini = time.time()
            self.valor_sensor(count,heat2600,string,opcion,vector_odorantes,samplesinicio,tendencia)
            time_end = time.time()
            time.sleep(Modulacion.SLEEP - (time_end - time_ini))
            self.muestras+=1
        Modulacion.cerrar_electrovalvulas()
    #################################################################################################################################

    def captura_datos(ahora,data):

        #succion,heat,switch,tendencia,samples_ini,CTE,name_file,name_folder,vecs_open_valves,sleeps = ENC.interfaz(2,sys.argv[1])
        #succion,switch,samples_ini,cte,name_file,name_folder,vecs_open_valves,sleeps,heat,tendencia = data

        for suc,he,sw,tendencia,samplesinicio,ct,nfile,nfolder,vsovs,sle in zip(self.succion,self.switch,self.samples_ini,self.cte,self.name_file,self.name_folder,self.vecs_open_valves,self.sleeps):

            self.imprimir_cabecera(vsovs,suc,sw,samplesinicio,ct,nfile,nfolder)

            ruta_fichero,ruta_fichero_data,ruta_fichero_tyh = Modulacion.create_files(self,nfile,"CAPTURAS/REGRESION/",nfolder,samplesinicio,ahora)
            self.f,self.g,self.h = Modulacion.open_files(self,ruta_fichero,ruta_fichero_data,ruta_fichero_tyh)

            print ('Ruta Fichero: ' + ruta_fichero)
            print ('Ruta Fichero de datos: '+ ruta_fichero_data)  

            #Llamada al thread de medida de temperatura y humedad
            Modulacion.crear_hilo_TyH(self)
            ADC.setup()
            
            PWM.start(self.heatPin2600,he,20000,0)
            Modulacion.motor_start(self,suc)
            Modulacion.file_TGS2600(self,vsovs,suc,he,tendencia,self.heatPin2600,ti2,sw,"Regresion","CAPTURAS/REGRESION/"+ str(ahora.year)+str(ahora.month)+str(ahora.day) + "/"+ nfolder + "/"  + str(samplesinicio) + "SAMPLESINICIO/",nfile+".txt",nfile+".dat","","TyH"+nfile+".data",f,1,ct,samplesinicio)

            print ('\n\nComienza la adquisicion. Muestras inciales: ' +str(samplesinicio)+ '\n\n')
            self.f.write('\n\nComienza la adquisicion. Muestras inciales: ' +str(samplesinicio)+ '\n\n')
            self.f.flush()
            Modulacion.cerrar_electrovalvulas()
            
            ##Calentamiento del sensor, se toman SAMPLESINICIO medidas antes de comenzar la experimentacion
            self.captura_odorante([4],samplesinicio,"Muestra Regresion ini",1,he,samplesinicio,tendencia)

            print ('\n\nComienza la experimentacion\n')
            self.f.write('\n\nComienza la experimentacion\n')
            self.f.flush()

            for i in range(len(vsovs)):

                if ct > 0:
                    self.captura_odorante([4],ct,"Muestra Regresion Bucle",2,he,samplesinicio,tendencia)

                Modulacion.imprimir_electrovalvulas(self,vsovs[i])
                self.captura_odorante(vsovs[i],sw,"Muestra Regresion",2,he,samplesinicio,tendencia)

            if ct > 0:
                self.captura_odorante([4],ct,"Muestra Regresion Bucle",2,he,samplesinicio,tendencia)

            Modulacion.motor_stop(self)
            PWM.stop(self.heatPin2600)
            PWM.cleanup()
            Modulacion.cierre(self)
            self.x=[]           
            self.concentTGS2600=[]
            self.muestras = 0
            time.sleep(sle)
        
        return 0

    def funcion_impulsos(x):
        if x < Modulacion.samples_ini:
            return 10
        if x >= Modulacion.switch and x < Modulacion.switch:
            return 10
        if x >= Modulacion.cte and x<(Modulacion.switch+Modulacion.switch):
            return -7

# Poner PID y rampa
