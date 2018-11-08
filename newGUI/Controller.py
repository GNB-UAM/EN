# -*- coding: utf-8 -*-

import new_GUI as NG

class Controller(QtWidgets.QMainWindow):
	
	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self,parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowIcon(QtGui.QIcon('assets/logo_rthy.png'))
		self.expand=False
		self.show()

		self.labels,self.lines = [self.ui.Tendencia,self.ui.TempSensor,self.ui.ModoEjecucion,
			self.ui.VariacionTemperatura,self.ui.TempeaturaMaxima,self.ui.TemperaturaMinima,self.ui.PeriodoSenialReferencia,
			self.ui.LimMaximoSup,self.ui.LimMinimoSup,self.ui.LimMaximoInf,self.ui.LimMinimoInf,self.ui.Alfa,self.ui.PicoMaximo,
			self.ui.PicoMinimo],[self.ui.TendenciaEdit,self.ui.TempSensorEdit,self.ui.ModoEjecucionEdit,
			self.ui.VariacionTemperaturaEdit,self.ui.TempeaturaMaximaEdit,self.ui.TemperaturaMinimaEdit,
			self.ui.PeriodoSenialReferenciaEdit,self.ui.LimMaximoSupEdit,self.ui.LimMinimoSupEdit,self.ui.LimMaximoInfEdit,
			self.ui.LimMinimoInfEdit,self.ui.AlfaEdit,self.ui.PicoMaximoEdit,self.ui.PicoMinimoEdit]

		self.Modulation.on_Modulation_currentIndexChanged.connect(self.seleccionar_modulacion)
		self.reiniciar_valores()

	def seleccionar_modulacion(self):

		selected = self.iu.Modulation.currentText();
		if selected == "Puro":
			self.reiniciar_valores()
		elif selected == "Regresion":
			ini,fin = 0,2
		elif selected == "Martinelli":
			ini,fin = 2,6
		elif selected == "PID":
			ini,fin = 6,len(self.labels)

		for i in range(6,len(self.labels)):
			self.labels[i].show()
			self.lines[i].show()


	def reiniciar_valores(self):

		for label,line in zip(self.labels,self.lines):
			label.hide()
			line.hide()

	
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
	myapp = Interface()
	myapp.resize(510, 0)
	myapp.show()
	sys.exit(app.exec_())	
