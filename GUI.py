# -*- encoding: utf-8 -*- # Especificamos que nuestro archivo .py estÃ¡ codificado en UTF-8
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename,asksaveasfilename,askopenfilenames
from tkinter.messagebox import showerror,showinfo
import tratamiento_cadenas as tc
import os
import paramiko
import pickle
import time

class GPyHuele_View(Tk):

    values = [['number_experiments','suction','number_samples','duration_stimulation','initial_samples','time_between_stimulus',
    'name_file','name_folder','sleep','vector_open_valves','experiment_version'],
    ['tendency','heat_sensor'],
    ['martinelli_execution_mode','martinelli_temperature_mode','minimun_temperature_martinelli','maximun_temperature_martinelli'],
    ['period','upper_limit_max','upper_limit_min','lower_limit_max','lower_limit_min','alpha','max_peak_value','min_peak_value']]

    conf_values = ['reading_port','heating_port','motor_pin','resistance','sd_folder','valve_position','number_samples','sleep_time','sleep_time_th','vcc','th_reading_port','sensor_tyh_type','electrovalves_port','type_sensor','reading_time']

    modulations = ['Pure','Regresion','Martinelli','PID']
    padx,pady = 3,3

    MAXSUCCION = 100
    MINSUCCION = 30
    MAXHEAT = 100
    MINHEAT = 1
    MINSWICHT = 1
    MINTENDENCIA = 0
    MINTIEMPO = 0
    MINSAMPLESINIO = 10

    def __init__(self,*args,**kwargs):

        Tk.__init__(self,*args,**kwargs)
        #self.root = Tk()
        self.title("GPyHuele")
        self.var = StringVar(value=GPyHuele_View.modulations[0]) # Variable que muestra que tipo de modulación se escoge
        self.entries_experiment = [] # Lista donde guardamos los returns de los entries de la configuración del experimento
        self.modulation_labels = [] # Lista donde guardamos los returns de los labels de las modulaciones extras
        self.entries_platform_conf = [] # Lista donde guardamos los returns de los entries de la configuración de la plataforma
        self.tab1 = None # Frame 1 del notebook, donde guardamos las opciones del experimento
        self.notebook = None # Notebook donde se guardan las pestañas
        self.controller = None 
        self.popup = None # Popup donde guardo recogo los valores de la conexión con la nariz
        self.address = "" # Ip de la nariz
        self.port = "" # Puerto de la nariz
        self.username = "" # Nombre del usuario de la nariz
        self.password = "" # Password de la nariz
        self.path = None # Ruta donde se encuentra el programa para su ejecución
        #self.root.mainloop()

    def set_controller(self,controller):
        self.controller = controller

    def create_gui(self):

        self.notebook = Notebook(self)
        self.notebook.grid(row=1,column=0,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,sticky=NSEW)
        self.tab1 = self.create_tab_1()
        self.notebook.add(self.tab1,text = 'Experiment')
        self.notebook.add(self.create_tab_2(),text = 'Plataform')
        self.create_head_buttons()          

    def create_tab_1(self):
        
        tab1 = Frame()
        Label(tab1, text='Modulation').grid(row=0,column=0,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,sticky=W)
        combobox = Combobox(tab1,textvariable=self.var,state='readonly')
        combobox.grid(row=0,column=1,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,sticky=W)
        combobox['values'] = GPyHuele_View.modulations
        combobox.bind("<<ComboboxSelected>>", self.controller.select_execution_mode)

        for pos,value in zip(range(1,len(GPyHuele_View.values[0])+1),GPyHuele_View.values[0]):
            label = Label(tab1, text=value).grid(row=pos+1,column=0, sticky=EW,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady)
            e = Entry(tab1, width=60)
            e.grid(row=pos+1,column=1, sticky=EW,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,ipadx=GPyHuele_View.padx,ipady=GPyHuele_View.pady,columnspan=4)
            self.entries_experiment.append(e)

        return tab1

    def create_tab_2(self):
        
        tab2 = Frame()
        for pos,value in zip(range(len(GPyHuele_View.conf_values)),GPyHuele_View.conf_values):
            label = Label(tab2, text=value).grid(row=pos,column=0, sticky=EW,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady)
            e = Entry(tab2, width=60)
            e.grid(row=pos,column=1, sticky=EW,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,ipadx=GPyHuele_View.padx,ipady=GPyHuele_View.pady,columnspan=4) #Hay que dejarlo así, sino da error
            self.entries_platform_conf.append(e)

        return tab2

    def change_modulations_options(self):
        
        pos = 13
        for i in range(len(self.modulation_labels)):
            self.entries_experiment.pop().destroy()
            self.modulation_labels.pop().destroy()
        
        if self.var.get() == 'Pure':
            return
    
        for value in GPyHuele_View.values[GPyHuele_View.modulations.index(self.var.get())]:
            l = Label(self.tab1, text=value)
            l.grid(row=pos,column=0,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,sticky=W)
            self.modulation_labels.append(l)
            e = Entry(self.tab1, width=60)
            e.grid(row=pos,column=1, sticky=EW,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,ipadx=GPyHuele_View.padx,ipady=GPyHuele_View.pady,columnspan=4) #Hay que dejarlo así, sino da error
            self.entries_experiment.append(e)
            pos+=1

    def create_head_buttons(self):
        
        head = Frame(self)
        head.grid(column=0,row=0,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady)
        icons = ['connect','start','load2','save2','exit']
        for i,icon,func in zip(range(len(icons)),icons,[self.controller.open_popup_connect,self.controller.start,self.controller.load_file,self.controller.save_file,self.controller.exit_program]):
            tbicon = PhotoImage(file='icons/'+icon+'.gif')
            tbicon.zoom(1,1)
            #cmd = eval('self.'+icon) #Pongo self. para que haga referencia a la funcion
            toolbar = Button(head,image=tbicon, command=func)
            toolbar.image=tbicon
            toolbar.grid(row=0,column=i+5,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady)

    # Va correctamente
    def load(self):

        path = askopenfilename()
        if path == () or path == '': #Ver como mejorar
            return

        if self.notebook.index(self.notebook.select()) == 0:
            lst = self.entries_experiment
            rvalues = tc.leer_fichero_experimento(path)
            lstvalues = tc.values[0]
        else:
            lst = self.entries_platform_conf
            rvalues = tc.leer_fichero_conf_plataforma(path)
            lstvalues = tc.conf_values

        if rvalues == -1:
            showerror("Error", "Error en los valores que desea cargar, reviselos y vuelva a intentarlo")
            return

        for elem in lst:
            elem.delete(0, END)
        
        lst_aux,modul = [],1

        for key,value in rvalues.items():
            if key == tc.SMODULACION:
                modul = int(value)
                self.var.set(GPyHuele_View.modulations[modul-1])
                self.change_modulations_options()
            elif key in lstvalues:
                lst[lstvalues.index(key)].insert(END,value)
            else:
                lst_aux.append([key,value])
        
        # Caso de que alguna opción sea solo regresion o martinelli, puede fallar aquí
        for key,value in lst_aux:
            if key not in tc.values[modul-1]:
                showerror("Error", "Error en los valores que desea cargar, reviselos y vuelva a intentarlo")
                return
            lst[tc.values[modul-1].index(key)+11].insert(END,value)
            
        return

    # Va correctamente
    def start(self): # Starts the experiment
        
        experiment_data_dict,platform_data_dict = {},{}

        for label,entry in zip(tc.values[0]+tc.values[GPyHuele_View.modulations.index(self.var.get())],self.entries_experiment):
            #if entry.get() == '':
            #    continue
            experiment_data_dict[label]=entry.get()

        experiment_data_dict[tc.SMODULACION]=GPyHuele_View.modulations.index(self.var.get())+1

        for label,entry in zip(tc.conf_values,self.entries_platform_conf):
            #if entry.get() == '':
            #    continue
            platform_data_dict[label] = entry.get()
        
        ######
        print(platform_data_dict)
        ######

        try:
            mod,experiment_data_dict,platform_data_dict = tc.tratamiento_datos(experiment_data_dict,platform_data_dict)
        except:
            showerror("Error","Error a la hora de iniciar el experimento, revise los parámetros e intentelo de nuevo")
            return

        for suc,sw,sini in zip(experiment_data_dict[tc.SSUCCION],experiment_data_dict[tc.SSWESTIM],experiment_data_dict[tc.SSINICIO]):
            if suc > GPyHuele_View.MAXSUCCION or suc < GPyHuele_View.MINSUCCION or sw < GPyHuele_View.MINSWICHT or (mod != 3 and sini < GPyHuele_View.MINSAMPLESINIO):
                showerror("Error","Error a la hora de iniciar el experimento, revise los parámetros e intentelo de nuevo")
                return
        
        if mod == 2:
            for tend,he in zip(experiment_data_dict[tc.STEND],experiment_data_dict[tc.SHTSENSOR]):
                if he < GPyHuele_View.MINHEAT or he > GPyHuele_View.MAXHEAT or tend < GPyHuele_View.MINTENDENCIA:
                    showerror("Error","Error a la hora de iniciar el experimento, revise los parámetros e intentelo de nuevo")
                    return
        
        with open("file_aux_config_experiment.pkl","wb") as f:
            pickle.dump([tc.SMODULACION,mod],f)
            for label,entry in experiment_data_dict.items():
                pickle.dump([label,entry],f)
        #####
        print(platform_data_dict)        
        #####
        with open("file_aux_config_platform.pkl","wb") as f:
            for label,entry in platform_data_dict.items():
                pickle.dump([label,entry],f)

        return mod,experiment_data_dict,platform_data_dict

    # Va correctamente
    def save(self):
        
        if self.notebook.index(self.notebook.select()) == 0:
            labels,aux_entries = GPyHuele_View.values[0]+GPyHuele_View.values[GPyHuele_View.modulations.index(self.var.get())],self.entries_experiment #Se podrá mejorar
        else:
            labels,aux_entries = GPyHuele_View.conf_values[0],self.entries_platform_conf
            
        f = asksaveasfilename(defaultextension='.txt')
        if f == None or f == () or f == '':
            return

        f = open(f,'w')

        for label,entry in zip(labels,aux_entries):
            f.write(label+':'+entry.get()+'\n')

        f.close()
        return

    # Va correctamente
    def exit_program(self):
        self.address = ""
        self.password = ""
        self.port = ""
        self.username = ""          
        exit(1)

    def connect_enose(self):
        
        self.popup = Tk()
        self.popup.title("Connect")
        Label(self.popup, text='User').grid(row=0,column=0,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,sticky=W)
        self.username = Entry(self.popup, width=30)
        self.username.grid(row=0,column=1, sticky=EW,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,ipadx=GPyHuele_View.padx,ipady=GPyHuele_View.pady,columnspan=4)
        Label(self.popup, text='Password').grid(row=1,column=0,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,sticky=W)
        self.password = Entry(self.popup, width=30,show="*")
        self.password.grid(row=1,column=1, sticky=EW,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,ipadx=GPyHuele_View.padx,ipady=GPyHuele_View.pady,columnspan=4)
        Label(self.popup, text='Address').grid(row=2,column=0,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,sticky=W)
        self.address = Entry(self.popup, width=30)
        self.address.grid(row=2,column=1, sticky=EW,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,ipadx=GPyHuele_View.padx,ipady=GPyHuele_View.pady,columnspan=4)
        Label(self.popup, text='Port').grid(row=3,column=0,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,sticky=W)
        self.port = Entry(self.popup, width=30)
        self.port.grid(row=3,column=1, sticky=EW,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,ipadx=GPyHuele_View.padx,ipady=GPyHuele_View.pady,columnspan=4)
        Label(self.popup, text='Path').grid(row=4,column=0,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,sticky=W)
        self.path = Entry(self.popup, width=30)
        self.path.grid(row=4,column=1, sticky=EW,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady,ipadx=GPyHuele_View.padx,ipady=GPyHuele_View.pady,columnspan=4)
        Button(self.popup,command=self.controller.connect,text="Connect").grid(row=5,column=0,padx=GPyHuele_View.padx,pady=GPyHuele_View.pady)
        self.popup.mainloop()

    def get_data_conection(self):
        
        self.address = self.address.get() # Ip de la nariz
        self.port = self.port.get() # Puerto de la nariz
        self.username = self.username.get() # Nombre del usuario de la nariz
        self.password = self.password.get() # Password de la nariz
        self.path = self.path.get() # Ruta donde ejecutar el programa
        self.path = self.path+"/" if self.path[-1] != "/" and self.path != "" else self.path
        self.popup.destroy()

    def get_ssh_values(self):
        return self.address,self.port,self.username,self.password,self.path

class GPyHuele_Controller(object):

    def __init__(self,model,**kwargs):

        super().__init__(**kwargs)
        self.model = model
        self.gui = None

    def set_gui(self,gui):
        self.gui = gui

    def select_execution_mode(self,event):
        self.gui.change_modulations_options()

    def load_file(self):
        self.gui.load()

    def load_file(self):
        self.gui.load()

    def save_file(self):
        self.gui.save()

    def exit_program(self):
        self.gui.exit_program()

    def open_popup_connect(self):
        self.gui.connect_enose()

    def connect(self):
        self.gui.get_data_conection()

    def start(self):
        mod,experiment_data_dict,platform_data_dict = self.gui.start()
        hostname,port,username,password,path = self.gui.get_ssh_values()
        # Falta probar esta parte
        self.model.get_nose_data(hostname,port,username,password,path,mod,experiment_data_dict,platform_data_dict)

class GPyHuele_Model(object):

    def __init__(self,**kwargs):

        super().__init__(**kwargs)

    def get_nose_data(self,hostname,port,username,password,path,modulation,config_experiment,config_plataform):

        if hostname == None or port == None or username == None or password == None:
            #Ejecutarlo en local
            if path != None:
                os.chdir(path)
            modul = tipos_modulacion[mod](config_experiment,config_elems)
            path = modul.captura_datos()
        else:
            try:
                t = paramiko.Transport((hostname,int(port)))
                t.connect(username=username, password=password)
                sftp = paramiko.SFTPClient.from_transport(t)
                sftp.put("file_aux_config_experiment.pkl",path+"file_aux_config_experiment.pkl")
                sftp.put("file_aux_config_platform.pkl",path+"file_aux_config_platform.pkl")
                t.close()
            except:
                showerror("Error al realizar la conexion","Error al realizar la conexion, por favor, compruebe que los datos sean correctos")
                t.close()
                return

            # Guardar los datos a ficheros, copiarlos en la nariz y luego ejecutar
            paramiko.util.log_to_file('paramilo.log')
            ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.connect(hostname,int(port),username,password)
            command = 'cd '+path+' && sudo python3 PyHuele.py file_aux_config_experiment.pkl file_aux_config_platform.pkl 1 > salida.txt'
            ##### NUEVO #####
            #transport = ssh.get_transport()
            #channel = transport.open_session()
            #channel.get_pty()
            #shell = ssh.invoke_shell()
            #shell.send(command)
            #channel.set_combine_stderr(True)
            #channel.exec_command(command)
            
            ###### PRUEBA ######
            #stdin,stdout,stderr = ssh.exec_command('ls')
            #print(stdout.read())
            ####################
            stdin,stdout,stderr = ssh.exec_command(command)
            #print(stdin.read())
            print(stdout.read())
            print(stderr.read())

            #time.sleep(100)
            #channel.close()
            ssh.close()

            os.remove("file_aux_config_experiment.pkl")
            os.remove("file_aux_config_platform.pkl")

        showinfo("Exito","El experimento se ha lanzado con exito")

        return

model = GPyHuele_Model()
controller = GPyHuele_Controller(model)
view = GPyHuele_View()
view.set_controller(controller)
view.create_gui()

view.set_controller(controller)
controller.set_gui(view)
view.mainloop()
