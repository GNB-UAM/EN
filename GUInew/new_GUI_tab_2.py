# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plotwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_plotwindow(object):
    def setupUi(self, plotwindow):
        plotwindow.setObjectName("plotwindow")
        plotwindow.resize(620, 334)
        self.checkBox = QtWidgets.QCheckBox(plotwindow)
        self.checkBox.setGeometry(QtCore.QRect(190, 620, 129, 21))
        self.checkBox.setObjectName("checkBox")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(plotwindow)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(20, 260, 141, 61))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_3.setContentsMargins(6, 0, 6, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SFichero = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.SFichero.setObjectName("SFichero")
        self.verticalLayout_3.addWidget(self.SFichero)
        self.RepresentarButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.RepresentarButton.setObjectName("RepresentarButton")
        self.verticalLayout_3.addWidget(self.RepresentarButton)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(plotwindow)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 131, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.checkBoxsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.checkBoxsLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBoxsLayout.setObjectName("checkBoxsLayout")
        self.VoltajecheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.VoltajecheckBox.setObjectName("VoltajecheckBox")
        self.checkBoxsLayout.addWidget(self.VoltajecheckBox)
        self.ResistenciaCheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.ResistenciaCheckBox.setObjectName("ResistenciaCheckBox")
        self.checkBoxsLayout.addWidget(self.ResistenciaCheckBox)
        self.TemperaturacheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.TemperaturacheckBox.setObjectName("TemperaturacheckBox")
        self.checkBoxsLayout.addWidget(self.TemperaturacheckBox)
        self.TemperaturaAcheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.TemperaturaAcheckBox.setObjectName("TemperaturaAcheckBox")
        self.checkBoxsLayout.addWidget(self.TemperaturaAcheckBox)
        self.HAmbientalcheckBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.HAmbientalcheckBox.setObjectName("HAmbientalcheckBox")
        self.checkBoxsLayout.addWidget(self.HAmbientalcheckBox)
        self.Texto = QtWidgets.QTextBrowser(plotwindow)
        self.Texto.setGeometry(QtCore.QRect(160, 20, 451, 301))
        self.Texto.setReadOnly(True)
        self.Texto.setObjectName("Texto")

        self.retranslateUi(plotwindow)
        QtCore.QMetaObject.connectSlotsByName(plotwindow)

    def retranslateUi(self, plotwindow):
        _translate = QtCore.QCoreApplication.translate
        plotwindow.setWindowTitle(_translate("plotwindow", "Dialog"))
        self.checkBox.setText(_translate("plotwindow", "CheckBox"))
        self.SFichero.setText(_translate("plotwindow", "Seleccionar fichero"))
        self.RepresentarButton.setText(_translate("plotwindow", "Representar"))
        self.VoltajecheckBox.setText(_translate("plotwindow", "Voltaje"))
        self.ResistenciaCheckBox.setText(_translate("plotwindow", "Resistencia"))
        self.TemperaturacheckBox.setText(_translate("plotwindow", "Temperatura"))
        self.TemperaturaAcheckBox.setText(_translate("plotwindow", "T. Ambiental"))
        self.HAmbientalcheckBox.setText(_translate("plotwindow", "H. Ambiental"))

