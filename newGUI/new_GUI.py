# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Electronic_Nose_Interface/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 701)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(6, -1, 781, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 361, 361))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(11, 10, 11, 0)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.Modulation = QtWidgets.QComboBox(self.formLayoutWidget)
        self.Modulation.setObjectName("Modulation")
        self.Modulation.addItem("")
        self.Modulation.addItem("")
        self.Modulation.addItem("")
        self.Modulation.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Modulation)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_1)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(410, 10, 361, 538))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(11, 10, 11, 0)
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setVerticalSpacing(13)
        self.formLayout_2.setObjectName("formLayout_2")
        self.PuertoLectura = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.PuertoLectura.setObjectName("PuertoLectura")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.PuertoLectura)
        self.PuertoLecturaEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.PuertoLecturaEdit.setObjectName("PuertoLecturaEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.PuertoLecturaEdit)
        self.PuertoCalentamiento = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.PuertoCalentamiento.setObjectName("PuertoCalentamiento")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.PuertoCalentamiento)
        self.PuertoCalentamientoEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.PuertoCalentamientoEdit.setObjectName("PuertoCalentamientoEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.PuertoCalentamientoEdit)
        self.PinMotor = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.PinMotor.setObjectName("PinMotor")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.PinMotor)
        self.PinMotorEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.PinMotorEdit.setObjectName("PinMotorEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.PinMotorEdit)
        self.Resistencia = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Resistencia.setObjectName("Resistencia")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Resistencia)
        self.ResistenciaEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.ResistenciaEdit.setObjectName("ResistenciaEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ResistenciaEdit)
        self.TarjetaSD = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.TarjetaSD.setObjectName("TarjetaSD")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.TarjetaSD)
        self.TarjetaSDEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.TarjetaSDEdit.setObjectName("TarjetaSDEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.TarjetaSDEdit)
        self.PosValvulas = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.PosValvulas.setObjectName("PosValvulas")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.PosValvulas)
        self.PosValvulasEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.PosValvulasEdit.setObjectName("PosValvulasEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.PosValvulasEdit)
        self.NMuestras = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.NMuestras.setObjectName("NMuestras")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.NMuestras)
        self.NMuestrasEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.NMuestrasEdit.setObjectName("NMuestrasEdit")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.NMuestrasEdit)
        self.FrecMuestras = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FrecMuestras.setObjectName("FrecMuestras")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.FrecMuestras)
        self.FrecMuestrasEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.FrecMuestrasEdit.setObjectName("FrecMuestrasEdit")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.FrecMuestrasEdit)
        self.FrecMuestrasTyH = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.FrecMuestrasTyH.setObjectName("FrecMuestrasTyH")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.FrecMuestrasTyH)
        self.FrecMuestrasTyHEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.FrecMuestrasTyHEdit.setObjectName("FrecMuestrasTyHEdit")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.FrecMuestrasTyHEdit)
        self.VCC = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.VCC.setObjectName("VCC")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.VCC)
        self.VCCEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.VCCEdit.setObjectName("VCCEdit")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.VCCEdit)
        self.PuertoLecturaTyH = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.PuertoLecturaTyH.setObjectName("PuertoLecturaTyH")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.PuertoLecturaTyH)
        self.PuertoLecturaTyHEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.PuertoLecturaTyHEdit.setObjectName("PuertoLecturaTyHEdit")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.PuertoLecturaTyHEdit)
        self.ModeloSensorTyH = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.ModeloSensorTyH.setObjectName("ModeloSensorTyH")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.ModeloSensorTyH)
        self.PuertosElectrovalvulas = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.PuertosElectrovalvulas.setObjectName("PuertosElectrovalvulas")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.PuertosElectrovalvulas)
        self.TipoSensor = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.TipoSensor.setObjectName("TipoSensor")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.TipoSensor)
        self.TiempoLectura = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.TiempoLectura.setObjectName("TiempoLectura")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.TiempoLectura)
        self.ModeloSensorTyHEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.ModeloSensorTyHEdit.setObjectName("ModeloSensorTyHEdit")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.ModeloSensorTyHEdit)
        self.TipoSensorEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.TipoSensorEdit.setObjectName("TipoSensorEdit")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.TipoSensorEdit)
        self.PuertosElectrovalvulasEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.PuertosElectrovalvulasEdit.setObjectName("PuertosElectrovalvulasEdit")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.PuertosElectrovalvulasEdit)
        self.TiempoLecturaEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.TiempoLecturaEdit.setObjectName("TiempoLecturaEdit")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.TiempoLecturaEdit)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tab_1)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 380, 361, 411))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(11, 11, 11, 11)
        self.formLayout_3.setSpacing(6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.Tendencia = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.Tendencia.setObjectName("Tendencia")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Tendencia)
        self.TendenciaEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.TendenciaEdit.setObjectName("TendenciaEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.TendenciaEdit)
        self.TempSensor = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.TempSensor.setObjectName("TempSensor")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.TempSensor)
        self.TempSensorEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.TempSensorEdit.setObjectName("TempSensorEdit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.TempSensorEdit)
        self.ModoEjecucion = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.ModoEjecucion.setObjectName("ModoEjecucion")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.ModoEjecucion)
        self.ModoEjecucionEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.ModoEjecucionEdit.setObjectName("ModoEjecucionEdit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ModoEjecucionEdit)
        self.VariacionTemperatura = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.VariacionTemperatura.setObjectName("VariacionTemperatura")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.VariacionTemperatura)
        self.VariacionTemperaturaEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.VariacionTemperaturaEdit.setObjectName("VariacionTemperaturaEdit")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.VariacionTemperaturaEdit)
        self.TemperaturaMinima = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.TemperaturaMinima.setObjectName("TemperaturaMinima")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.TemperaturaMinima)
        self.TemperaturaMinimaEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.TemperaturaMinimaEdit.setObjectName("TemperaturaMinimaEdit")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.TemperaturaMinimaEdit)
        self.TempeaturaMaxima = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.TempeaturaMaxima.setObjectName("TempeaturaMaxima")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.TempeaturaMaxima)
        self.TempeaturaMaximaEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.TempeaturaMaximaEdit.setObjectName("TempeaturaMaximaEdit")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.TempeaturaMaximaEdit)
        self.SenialReferencia = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.SenialReferencia.setObjectName("SenialReferencia")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.SenialReferencia)
        self.LimMaximoSup = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.LimMaximoSup.setObjectName("LimMaximoSup")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.LimMaximoSup)
        self.LimMinimoSup = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.LimMinimoSup.setObjectName("LimMinimoSup")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.LimMinimoSup)
        self.LimMaximoInf = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.LimMaximoInf.setObjectName("LimMaximoInf")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.LimMaximoInf)
        self.LimMinimoInf = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.LimMinimoInf.setObjectName("LimMinimoInf")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.LimMinimoInf)
        self.Alfa = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.Alfa.setObjectName("Alfa")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.Alfa)
        self.PicoMaximo = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.PicoMaximo.setObjectName("PicoMaximo")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.PicoMaximo)
        self.PicoMinimo = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.PicoMinimo.setEnabled(True)
        self.PicoMinimo.setObjectName("PicoMinimo")
        self.formLayout_3.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.PicoMinimo)
        self.SenialReferenciaEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.SenialReferenciaEdit.setObjectName("SenialReferenciaEdit")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.SenialReferenciaEdit)
        self.LimMaximoSupEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.LimMaximoSupEdit.setObjectName("LimMaximoSupEdit")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.LimMaximoSupEdit)
        self.LimMinimoSupEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.LimMinimoSupEdit.setObjectName("LimMinimoSupEdit")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.LimMinimoSupEdit)
        self.LimMaximoInfEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.LimMaximoInfEdit.setObjectName("LimMaximoInfEdit")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.LimMaximoInfEdit)
        self.LimMinimoInfEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.LimMinimoInfEdit.setObjectName("LimMinimoInfEdit")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.LimMinimoInfEdit)
        self.AlfaEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.AlfaEdit.setObjectName("AlfaEdit")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.AlfaEdit)
        self.PicoMaximoEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.PicoMaximoEdit.setObjectName("PicoMaximoEdit")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.PicoMaximoEdit)
        self.PicoMinimoEdit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.PicoMinimoEdit.setObjectName("PicoMinimoEdit")
        self.formLayout_3.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.PicoMinimoEdit)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 0, 82, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 788, 20))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Modulation.setItemText(0, _translate("MainWindow", "Puro"))
        self.Modulation.setItemText(1, _translate("MainWindow", "Regresion"))
        self.Modulation.setItemText(2, _translate("MainWindow", "PID"))
        self.Modulation.setItemText(3, _translate("MainWindow", "Martinelli"))
        self.label.setText(_translate("MainWindow", "Número de experimentos"))
        self.label_2.setText(_translate("MainWindow", "Succion"))
        self.label_3.setText(_translate("MainWindow", "Número muestras aleatorias"))
        self.label_4.setText(_translate("MainWindow", "Duracion del estimulo"))
        self.label_5.setText(_translate("MainWindow", "Muestras iniciales"))
        self.label_6.setText(_translate("MainWindow", "Tiempo entre estímulos"))
        self.label_7.setText(_translate("MainWindow", "Nombre fichero"))
        self.label_8.setText(_translate("MainWindow", "Nombre carpeta"))
        self.label_9.setText(_translate("MainWindow", "Dormir"))
        self.label_10.setText(_translate("MainWindow", "Vector de apertura de vávulas"))
        self.label_11.setText(_translate("MainWindow", "Versión del experimento"))
        self.PuertoLectura.setText(_translate("MainWindow", "Puerto de lectura"))
        self.PuertoCalentamiento.setText(_translate("MainWindow", "Puerto de calentamiento"))
        self.PinMotor.setText(_translate("MainWindow", "Pin del motor"))
        self.Resistencia.setText(_translate("MainWindow", "Resistencia"))
        self.TarjetaSD.setText(_translate("MainWindow", "Tarjeta SD"))
        self.PosValvulas.setText(_translate("MainWindow", "Posición de las vávulas"))
        self.NMuestras.setText(_translate("MainWindow", "Número muestras"))
        self.FrecMuestras.setText(_translate("MainWindow", "Frecuencia muestras(segundos)"))
        self.FrecMuestrasTyH.setText(_translate("MainWindow", "Frecuencia muestras TyH(secs.)"))
        self.VCC.setText(_translate("MainWindow", "VCC"))
        self.PuertoLecturaTyH.setText(_translate("MainWindow", "Puerto lectura TyH"))
        self.ModeloSensorTyH.setText(_translate("MainWindow", "Modelo sensor TyH"))
        self.PuertosElectrovalvulas.setText(_translate("MainWindow", "Puertos electroválvulas"))
        self.TipoSensor.setText(_translate("MainWindow", "Tipo sensor"))
        self.TiempoLectura.setText(_translate("MainWindow", "Tiempo lectura"))
        self.Tendencia.setText(_translate("MainWindow", "Tendencia"))
        self.TempSensor.setText(_translate("MainWindow", "Tempetura sensor"))
        self.ModoEjecucion.setText(_translate("MainWindow", "Modo ejecucion"))
        self.VariacionTemperatura.setText(_translate("MainWindow", "Variación temperatura"))
        self.TemperaturaMinima.setText(_translate("MainWindow", "Temperatura mínima"))
        self.TempeaturaMaxima.setText(_translate("MainWindow", "Temperatura máxima"))
        self.SenialReferencia.setText(_translate("MainWindow", "Periodo señal referencia"))
        self.LimMaximoSup.setText(_translate("MainWindow", "Limite máximo superior"))
        self.LimMinimoSup.setText(_translate("MainWindow", "Limite mínimo superior"))
        self.LimMaximoInf.setText(_translate("MainWindow", "Limite máximo inferior"))
        self.LimMinimoInf.setText(_translate("MainWindow", "Limite mínimo inferior"))
        self.Alfa.setText(_translate("MainWindow", "Valor Alfa"))
        self.PicoMaximo.setText(_translate("MainWindow", "Valor máximo tolerable"))
        self.PicoMinimo.setText(_translate("MainWindow", "Valor mínimo tolerable"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
