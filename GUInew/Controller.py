# -*- coding: utf-8 -*-

#import new_GUI as NG
from new_GUI import *
from new_GUI_tab import *
from new_GUI_tab_2 import *
import sys
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtCore import *
import os
import paramiko
import pickle
import numpy as np
sys.path.insert(0,'../')
import tratamiento_cadenas as tc

class Controller(QtWidgets.QMainWindow):
        
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.setWindowIcon(QtGui.QIcon('assets/logo_rthy.png'))
        self.expand=False
        self.show()

        self.window=QtWidgets.QMainWindow()
        self.conexion_tab = Ui_SSHWindow()
        self.conexion_tab.setupUi(self.window)
            
        self.plot_window = QtWidgets.QMainWindow()
        self.plot_tab = Ui_plotwindow()
        self.plot_tab.setupUi(self.plot_window)

        self.REGRESION,self.MARTINELLI,self.PID = 0,1,2
        self.modulations = [self.ui.RegresionWidget,self.ui.MartinelliWidget,self.ui.PIDWidget]

        self.ui.modulation.currentIndexChanged.connect(self.seleccionar_modulacion)
        #self.ui.pushButton.clicked.connect(self.obtener_informacion_widgets)
        self.ui.StartButton.clicked.connect(self.start)
        self.ui.LoadButton.clicked.connect(self.cargar_datos)
        self.ui.SaveButton.clicked.connect(self.guardar_datos)
        self.ui.SSHButton.clicked.connect(self.conexion)
        self.ui.ConfPlotButton.clicked.connect(self.configurar_representacion)
        self.ui.SSHcheckBox.stateChanged.connect(self.habilitar_SSH)
        self.conexion_tab.OKButton.clicked.connect(self.SSH_obtener_parametros_conexion)
        self.conexion_tab.CheckButton.clicked.connect(self.SSH_comprobar_conexion)
        self.conexion_tab.ResetButton.clicked.connect(self.SSH_resetear_parametros_conexion)
        self.plot_tab.SFichero.clicked.connect(self.seleccionar_fichero_plot)
        self.plot_tab.RepresentarButton.clicked.connect(self.representar_datos)
        self.ssh_user,self.ssh_password,self.ssh_address,self.ssh_port,self.ssh_path = None,None,None,None,''
        self.MAXSUCCION = 100
        self.MINSUCCION = 30
        self.MAXHEAT = 100
        self.MINHEAT = 1
        self.MINSWICHT = 1
        self.MINTENDENCIA = 0
        self.MINTIEMPO = 0
        self.MINSAMPLESINIO = 10
        self.files_plot = []
        self.colors = ["#FE0000","#25FD00","#00BAFE","#1400FD","#FD00CE","#FD7600","#FEF900","#2D5D0A","#83B62B","#000000","#800000","#87048F","#820624","#08EC81","#827E83","#D96B4E"]

        self.reiniciar_widgets()

    def comprobacion_datos_introducidos(mod,experiment_data_dict):
    
        #Caso base, opciones comunes
        for suc,sw,sini in zip(experiment_data_dict[tc.SUCCION],experiment_data_dict[tc.SWESTIM],experiment_data_dict[tc.SINICIO]):
            if suc > self.MAXSUCCION or suc < self.MINSUCCION or sw < self.MINSWICHT or (mod != 3 and sini < self.MINSAMPLESINIO):
                print ('PARAMETROS(S) INCORRECTO(S).\n Por favor revise los parametros introducidos y vuelva a empezar')
                exit(1)

        #Caso de regresion
        if mod == 2:
            for tend,he in zip(experiment_data_dict[tc.TEND],experiment_data_dict[tc.HTSENSOR]):
                if he < self.MINHEAT or he > self.MAXHEAT or tend < self.MINTENDENCIA:
                    print ('PARAMETROS(S) INCORRECTO(S).\n Por favor revise los parametros introducidos y vuelva a empezar')
                    exit(1)

    def start(self):
        if self.ui.SSHcheckBox.isChecked() == False and (self.ssh_address == None or self.ssh_port == None or self.ssh_user == None or self.ssh_password == None):
            QMessageBox.critical(self,"Error","Introduzca los datos para la conexion ssh.")
            return

        dict = {}
        dict[self.ui.modulation.objectName()] = str(self.ui.modulation.currentIndex()+1)
        #Cargamos valores por defecto de configuracion
        dict[VALPOS] = 'P'
        dict[SENTYPE] = 3
        dict[RDTIME] = 0.1
        dict[ELECPORTS] = ['P8_10','P8_12','P8_14','P8_16']

        #Guardamos las opciones recogidas en la interfaz
        for i in range(self.ui.PuroLabelsLayout.count()):
            if self.ui.PuroEntriesLayout.itemAt(i).widget().text()[1:-1] != '':
                dict[self.ui.PuroLabelsLayout.itemAt(i).widget().objectName()] = self.ui.PuroEntriesLayout.itemAt(i).widget().text()[1:-1]
            else:
                dict[self.ui.PuroLabelsLayout.itemAt(i).widget().objectName()] = '0*'

        for widget in self.modulations:
            if widget.isVisible() == True:
                for label,entry in zip(widget.children()[1:int((len(widget.children())+1)/2)],widget.children()[int((len(widget.children())+1)/2):]):
                    dict[label.objectName()] = entry.text()[1:-1] if entry.text()[1:-1] != '' else dict[label.objectName()] = '0*'
        
            for i in range(self.ui.PlatformLabelLayout.count()):
                dict[self.ui.PlatformLabelLayout.itemAt(i).widget().objectName()] = self.ui.PlatformEntriesLayout.itemAt(i).widget().text()[1:-1]

        try:
            #print("HOLA",dict)
            mod,dict = tc.tratamiento_fichero_configuracion(dict)
        except:
            QMessageBox.critical(self,"Error","Error ocurrido al tratar los datos. Reviselos")
            return

        #print("HOLA2")
        #exit(1)
        if self.ui.SSHcheckBox.isChecked() == False:
            self.comprobacion_datos_introducidos(mod,dict)
            modul = tipos_modulacion[mod](dict)
            path = modul.iniciar_captura_datos()
        else:
            # Realizo un Pickle -> IMPORTANTE: CUIDADO CON LOS PICKLES, NO ABRIR NINGUNO DESCONOCIDO. RIESGO PARA LA SEGURIDAD DEL ORDENADOR
            fileObject = open("pickle_dic.pkl","wb")
            pickle.dump([mod,dict],fileObject,protocol=pickle.HIGHEST_PROTOCOL)
            fileObject.close()
            t = paramiko.Transport((self.ssh_address,int(self.ssh_port)))
            t.connect(username=self.ssh_user, password=self.ssh_password)
            sftp = paramiko.SFTPClient.from_transport(t)
            sftp.put("pickle_dic.pkl",self.ssh_path+"pickle_dic.pkl")
            t.close()
            paramiko.util.log_to_file('paramilo.log')
            ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.connect(self.ssh_address,int(self.ssh_port),self.ssh_user,self.ssh_password)
            command = 'cd '+self.ssh_path+' && sudo python3 PyHuele.py --remote'
            stdin,stdout,stderr = ssh.exec_command(command)
            ssh.close()
            os.remove("pickle_dic.pkl")
                   
    def limpiar_opciones_plot(self,text):
        if text == True: 
            self.plot_tab.Texto.clear()
            self.files_plot.clear()
        for pos in range(self.plot_tab.checkBoxsLayout.count()):
            self.plot_tab.checkBoxsLayout.itemAt(pos).widget().setChecked(False)
        return

    def representar_datos(self):
        self.ui.ax.clear()
        for i,lst in enumerate(self.files_plot):
            data = np.genfromtxt(lst[0],skip_header=1,delimiter=' ').T
            for c in lst[1]: self.ui.ax.plot(data[c],color=self.colors[i%len(self.colors)])

        self.ui.canvas.draw()
        self.limpiar_opciones_plot(True)
        return
                
        def habilitar_SSH(self):
            self.ui.SSHButton.setEnabled(True) if self.ui.SSHcheckBox.isChecked() == True else self.ui.SSHButton.setEnabled(False)
            return

    def seleccionar_fichero_plot(self):

        filename = QFileDialog.getOpenFileName()[0]
        if filename == '':
            return
        columns,name = [],[]
        for i in range(self.plot_tab.checkBoxsLayout.count()):
            if self.plot_tab.checkBoxsLayout.itemAt(i).widget().isChecked() == True:
                columns.append(i+1)
                name.append(self.plot_tab.checkBoxsLayout.itemAt(i).widget().text())

        if len(columns) == 0:
            QMessageBox.critical(self,"Error","Debe seleccionar una columna para su representacion")
            return

        self.plot_tab.Texto.append("%s\n\t%s\n"%(filename,name))
        self.files_plot.append([filename,columns])
        self.limpiar_opciones_plot(False)
        return           

    def conexion(self):
        self.window.show()
         
    def configurar_representacion(self):
        self.plot_window.show()
        
    def SSH_obtener_parametros_conexion(self):
        self.ssh_user,self.ssh_password,self.ssh_address,self.ssh_port,self.ssh_path = self.conexion_tab.User_Edit.text(),self.conexion_tab.Password_Edit.text(),self.conexion_tab.Address_Edit.text(),self.conexion_tab.Port_Edit.text(),self.conexion_tab.Path_remote_Edit.text()
        return

    def SSH_resetear_parametros_conexion(self):
        self.ssh_user = self.ssh_password = self.ssh_address = self.ssh_port = self.ssh_path = None
        for i in range(self.conexion_tab.SSHEntriesLayout.count()):
            self.conexion_tab.SSHEntriesLayout.itemAt(i).widget().clear()
        return

    def SSH_comprobar_conexion(self):
        if self.ssh_address == None:
            QMessageBox.warning(self,"Conexion Erronea","Debe introducir una direccion.")
            return
        response = os.system("ping -c 1 "+self.ssh_address)
        if response == 0:
            QMessageBox.information(self,"Conexion Correcta","La conexión es correcta")
        else:
            QMessageBox.warning(self,"Conexion Erronea","El destino no se encuentra")
            
        return

    def seleccionar_modulacion(self):

        selected = self.ui.modulation.currentText()
        self.reiniciar_widgets()
        if selected == "Regresion":
            self.modulations[self.REGRESION].show()
        elif selected == "Martinelli":
            self.modulations[self.MARTINELLI].show()
        elif selected == "PID":
            self.modulations[self.PID].show()
            
        return

    def reiniciar_widgets(self):
            
        self.ui.SSHButton.setEnabled(False)
        for widgets in self.modulations:
            widgets.hide()
        
        return

    def guardar_datos(self):
        filename = QFileDialog.getSaveFileName()
        if filename[0] == '':
            return
        file = open(filename[0],'w')
        file.write("Modulation: %s\n"%(self.ui.modulation.currentIndex()+1))
        for i in range(self.ui.PuroLabelsLayout.count()):
            file.write("%s: %s"%(self.ui.PuroLabelsLayout.itemAt(i).widget().text(),self.ui.PuroEntriesLayout.itemAt(i).widget().text()))
           
        """ 
        La lista devuelta por children() tiene como 
        primer elemento un layout que no queremos. 
        Los primeros elementos, hasta la mitad, 
        son las etiquetas y los ultimos son los 
        campos para rellenar, de ahí la indexacion rara.
        """
        for widget in self.modulations:
            if widget.isVisible() == True:
                for label,entry in zip(widget.children()[1:int((len(widget.children())+1)/2)],widget.children()[int((len(widget.children())+1)/2):]):
                    file.write("%s: %s"%(label.text(),entry.text()))


        file.close()
        return

    def resetear_entradas(self):
            
        for i in range(self.ui.PuroEntriesLayout.count()):
            self.ui.PuroEntriesLayout.itemAt(i).widget().clear()

        for widget in self.modulations:
            for entry in widget.children()[int((len(widget.children())+1)/2):]:
                entry.clear()

        for i in range(self.ui.PlatformEntriesLayout.count()):
            self.ui.PlatformEntriesLayout.itemAt(i).widget().clear()

        return

    def cargar_datos(self):
        filename = QFileDialog.getOpenFileName()
        if filename[0] == '': #Caso en que no se selecciona ningun fichero
            return
        self.resetear_entradas()
        file = open(filename[0],'r')
        for line in file.readlines():
            line = re.sub('[\s]+','',line)
            line,entry = re.split(':|//',line)
            if line == '':
                continue
            if label.lower() == "modulation":
                self.ui.modulation.setCurrentIndex(int(entry)-1)
            else:
                try:
                    self.findChild(QObject,label+"_Edit").setText(entry)
                except:
                    QMessageBox.critical(self,"Error","Error ocurrido al cargar los datos. El identificador: %s no existe."%label)
                    return
        file.close()
        return

############
#   MAIN   #
############
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        myapp = Controller()
        myapp.resize(510, 0)
        myapp.show()
sys.exit(app.exec_())   
