# -*- coding: utf-8 -*-

#import new_GUI as NG
from new_GUI import *
import sys

class Controller(QtWidgets.QMainWindow):
        
        def __init__(self, parent=None):
                QtWidgets.QMainWindow.__init__(self,parent)
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                #self.setWindowIcon(QtGui.QIcon('assets/logo_rthy.png'))
                self.expand=True
                self.show()

                self.REGRESION,self.MARTINELLI,self.PID = 0,1,2
                self.modulations = [self.ui.RegresionWidget,self.ui.MartinelliWidget,self.ui.PIDWidget]

                self.ui.Modulation.currentIndexChanged.connect(self.seleccionar_modulacion)
                self.ui.pushButton.clicked.connect(self.obtener_informacion_widgets)
                self.ui.StartButton.clicked.connect(self.iniciar_experimento)
                self.ui.LoadButton.clicked.connect(self.cargar_datos)
                self.ui.SaveButton.clicked.connect(self.guardar_datos)
                self.reiniciar_widgets()

        def guardar_datos(self):
            x=3

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



############
#   MAIN   #
############
if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        myapp = Controller()
        myapp.resize(510, 0)
        myapp.show()
sys.exit(app.exec_())   
