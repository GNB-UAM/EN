# -*- coding: utf-8 -*-

#import new_GUI as NG
from new_GUI import *
import sys
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtCore import *

class Controller(QtWidgets.QMainWindow):
        
        def __init__(self, parent=None):
                QtWidgets.QMainWindow.__init__(self,parent)
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                #self.setWindowIcon(QtGui.QIcon('assets/logo_rthy.png'))
                self.expand=False
                self.show()

                self.REGRESION,self.MARTINELLI,self.PID = 0,1,2
                self.modulations = [self.ui.RegresionWidget,self.ui.MartinelliWidget,self.ui.PIDWidget]

                self.ui.Modulation.currentIndexChanged.connect(self.seleccionar_modulacion)
                self.ui.pushButton.clicked.connect(self.obtener_informacion_widgets)
                #self.ui.StartButton.clicked.connect(self.iniciar_experimento)
                self.ui.LoadButton.clicked.connect(self.cargar_datos)
                self.ui.SaveButton.clicked.connect(self.guardar_datos)
                self.ui.SSHButton.clicked.connect(self.conexion)
                self.reiniciar_widgets()
            
        def conexion(self):



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
    
############
#   MAIN   #
############
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        myapp = Controller()
        myapp.resize(510, 0)
        myapp.show()
sys.exit(app.exec_())   
