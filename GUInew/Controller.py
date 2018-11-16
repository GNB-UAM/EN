# -*- coding: utf-8 -*-

#import new_GUI as NG
from new_GUI import *
from new_GUI_tab import *
import sys
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtCore import *
import os
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

                self.ui.Modulation.currentIndexChanged.connect(self.seleccionar_modulacion)
                #self.ui.pushButton.clicked.connect(self.obtener_informacion_widgets)
                self.ui.StartButton.clicked.connect(self.conexion)
                self.ui.LoadButton.clicked.connect(self.cargar_datos)
                self.ui.SaveButton.clicked.connect(self.guardar_datos)
                self.ui.SSHButton.clicked.connect(self.conexion)
                self.ui.ConfPlotButton.clicked.connect(self.configurar_representacion)
                self.ui.SSHcheckBox.stateChanged.connect(self.habilitar_SSH)
                self.conexion_tab.OKButton.clicked.connect(self.SSH_obtener_parametros_conexion)
                self.conexion_tab.CheckButton.clicked.connect(self.SSH_comprobar_conexion)
                self.conexion_tab.ResetButton.clicked.connect(self.SSH_resetear_parametros_conexion)
                self.ssh_user,self.ssh_password,self.ssh_address,self.ssh_port,self.ssh_path = None,None,None,None,None

                self.reiniciar_widgets()
           
        def habilitar_SSH(self):
            self.SSHButton.setEnabled(True) if self.ui.SSHcheckBox.isChecked() == True else self.SSHButton.setEnabled(False)
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
            for widget in self.conexion_tab.SSHEntriesLayout.children():
                widget.clear()
            return

        def SSH_comprobar_conexion(self):
            response = os.system("ping -c 1 "+self.ssh_address)
            if response == 0:
                QMessageBox.information(self,"Conexion Correcta","La conexión es correcta")
            else:
                QMessageBox.warning(self,"Conexion Erronea","El destino no se encuentra")
            
            return


        def seleccionar_modulacion(self):

            selected = self.ui.Modulation.currentText()
            self.reiniciar_widgets()
            if selected == "Regresion":
                self.modulations[self.REGRESION].show()
            elif selected == "Martinelli":
                self.modulations[self.MARTINELLI].show()
            elif selected == "PID":
                self.modulations[self.PID].show()
            
            return

        def reiniciar_widgets(self):
            
            for widgets in self.modulations:
                widgets.hide()
        
            return

        def obtener_informacion_widgets(self):

            for widget_count in range(1,self.ui.ExperimentLayout.count()):
                if widget_count%2 == 0:
                    labels.append(self.ui.ExperimentLayout.itemAt(i).widget().objectName())
                else:
                    entries.append(self.ui.ExperimentLayout.itemAt(i).widget().text())
                        
            selected = self.ui.Modulation.currentText()
            if selected == "Regresion":
                for widget_count in range(1,self.ui.ExperimentLayout.count()):
                    if widget_count%2 == 0:
                        labels.append(self.ui.ExperimentLayout.itemAt(i).widget().objectName())
                    else:
                        entries.append(self.ui.ExperimentLayout.itemAt(i).widget().text())
            elif selected == "Martinelli":
                for widget_count in range(1,self.ui.ExperimentLayout.count()):
                    if widget_count%2 == 0:
                        labels.append(self.ui.ExperimentLayout.itemAt(i).widget().objectName())
                    else:
                        entries.append(self.ui.ExperimentLayout.itemAt(i).widget().text())
            elif selected == "PID":
                for widget_count in range(1,self.ui.ExperimentLayout.count()):
                    if widget_count%2 == 0:
                        labels.append(self.ui.ExperimentLayout.itemAt(i).widget().objectName())
                    else:
                        entries.append(self.ui.ExperimentLayout.itemAt(i).widget().text())
            

        def iniciar_experimento(self):
                
                diccionario = {}
                for i in range(ini,fin):
                        diccionario[self.labels[i][:2]+self.labels[i][-2:]] = self.lines[i].text()
                
                tc.tratamiento_fichero_configuracion(diccionario)

        def guardar_datos(self):
            filename = QFileDialog.getOpenFileName()
            file = open(filename[0],'w')
            file.write("Modulation: %s\n"%(self.ui.Modulation.currentIndex()+1))
            for i in range(self.ui.verticalLayout_6.count()):
                file.write("%s: %s\n"%(self.ui.verticalLayout_6.itemAt(i).widget().text(),self.ui.verticalLayout_7.itemAt(i).widget().text()))
           
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
                        file.write("%s: %s\n"%(label.text(),entry.text()))


            file.close()
            return

        def cargar_datos(self):
            self.resetear_entradas()
            filename = QFileDialog.getOpenFileName()
            file = open(filename[0],'r')
            label,entry = file.readline().split(':')
            self.ui.Modulation.setCurrentIndex(int(entry)-1)
            for line in file.readlines():
                label,entry = line.split(':')
                try:
                    self.findChild(QObject,label.replace(" ","_")+"_Edit").setText(entry)
                except:
                    QMessageBox.critical(self,"Error","Error ocurrido al cargar los datos. El identificador: %s no existe."%label)
                    return
            file.close()
            return

        def resetar_entradas(self):
            
            for entry in self.ui.PuroEntriesLayout.children():
                entry.clear()

            for widget in self.modulations:
                for entry in widget.children()[int((len(widget.children())+1)/2):]:
                    entry.clear()

            for entry in self.ui.PlatformEntriesLayout.children():
                entry.clear()

            return

        def seleccionar_ficheros(self):
            filename,plot_options = QFileDialog.getOpenFileName()[0],[]
            for pos,checkBox in enumerate(self.plot_tab.checkBoxsLayout.children()):
                if checkBox.isChecked() == True:
                    self.options.append(checkBox.text)
                    plot_options.append(pos+1)
                    checkBox.setChecked(False)
                self.plot_selected_files.append([filename,plot_options])
                self.plot_tab.texto.append("%s\n\t%s\n"%(filename,options))
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
