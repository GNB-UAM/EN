# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(834, 629)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 811, 581))
        self.tabWidget.setObjectName("tabWidget")
        self.CaptureMode = QtWidgets.QWidget()
        self.CaptureMode.setObjectName("CaptureMode")
        self.gridLayoutWidget = QtWidgets.QWidget(self.CaptureMode)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 360, 391, 336))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.RegresionWidget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.RegresionWidget.setObjectName("RegresionWidget")
        self.formLayout = QtWidgets.QFormLayout(self.RegresionWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.Tendency = QtWidgets.QLabel(self.RegresionWidget)
        self.Tendency.setObjectName("Tendency")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Tendency)
        self.Sensor_temperature = QtWidgets.QLabel(self.RegresionWidget)
        self.Sensor_temperature.setObjectName("Sensor_temperature")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Sensor_temperature)
        self.Tendency_Edit = QtWidgets.QLineEdit(self.RegresionWidget)
        self.Tendency_Edit.setObjectName("Tendency_Edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Tendency_Edit)
        self.Sensor_temperature_Edit = QtWidgets.QLineEdit(self.RegresionWidget)
        self.Sensor_temperature_Edit.setObjectName("Sensor_temperature_Edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Sensor_temperature_Edit)
        self.gridLayout_5.addWidget(self.RegresionWidget, 0, 0, 1, 1)
        self.MartinelliWidget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.MartinelliWidget.setObjectName("MartinelliWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.MartinelliWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setSpacing(0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Execution_mode = QtWidgets.QLabel(self.MartinelliWidget)
        self.Execution_mode.setObjectName("Execution_mode")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Execution_mode)
        self.Temperature_mode = QtWidgets.QLabel(self.MartinelliWidget)
        self.Temperature_mode.setObjectName("Temperature_mode")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Temperature_mode)
        self.Maximum_temperature = QtWidgets.QLabel(self.MartinelliWidget)
        self.Maximum_temperature.setObjectName("Maximum_temperature")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Maximum_temperature)
        self.Minimum_temperature = QtWidgets.QLabel(self.MartinelliWidget)
        self.Minimum_temperature.setObjectName("Minimum_temperature")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Minimum_temperature)
        self.Execution_mode_Edit = QtWidgets.QLineEdit(self.MartinelliWidget)
        self.Execution_mode_Edit.setObjectName("Execution_mode_Edit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Execution_mode_Edit)
        self.Temperature_mode_Edit = QtWidgets.QLineEdit(self.MartinelliWidget)
        self.Temperature_mode_Edit.setObjectName("Temperature_mode_Edit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Temperature_mode_Edit)
        self.Maximum_temperature_Edit = QtWidgets.QLineEdit(self.MartinelliWidget)
        self.Maximum_temperature_Edit.setObjectName("Maximum_temperature_Edit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Maximum_temperature_Edit)
        self.Minimum_temperature_Edit = QtWidgets.QLineEdit(self.MartinelliWidget)
        self.Minimum_temperature_Edit.setObjectName("Minimum_temperature_Edit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Minimum_temperature_Edit)
        self.gridLayout_5.addWidget(self.MartinelliWidget, 1, 0, 1, 1)
        self.PIDWidget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.PIDWidget.setObjectName("PIDWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.PIDWidget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setSpacing(0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.Reference_signal_period = QtWidgets.QLabel(self.PIDWidget)
        self.Reference_signal_period.setObjectName("Reference_signal_period")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Reference_signal_period)
        self.Upper_maximum_limit = QtWidgets.QLabel(self.PIDWidget)
        self.Upper_maximum_limit.setObjectName("Upper_maximum_limit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Upper_maximum_limit)
        self.Upper_minimum_limit = QtWidgets.QLabel(self.PIDWidget)
        self.Upper_minimum_limit.setObjectName("Upper_minimum_limit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Upper_minimum_limit)
        self.Lower_maximum_limit = QtWidgets.QLabel(self.PIDWidget)
        self.Lower_maximum_limit.setObjectName("Lower_maximum_limit")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Lower_maximum_limit)
        self.Lower_minimum_limit = QtWidgets.QLabel(self.PIDWidget)
        self.Lower_minimum_limit.setObjectName("Lower_minimum_limit")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Lower_minimum_limit)
        self.Alpha_value = QtWidgets.QLabel(self.PIDWidget)
        self.Alpha_value.setObjectName("Alpha_value")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.Alpha_value)
        self.Maximum_value = QtWidgets.QLabel(self.PIDWidget)
        self.Maximum_value.setObjectName("Maximum_value")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.Maximum_value)
        self.Minimum_value = QtWidgets.QLabel(self.PIDWidget)
        self.Minimum_value.setEnabled(True)
        self.Minimum_value.setObjectName("Minimum_value")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.Minimum_value)
        self.Reference_signal_period_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.Reference_signal_period_Edit.setObjectName("Reference_signal_period_Edit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Reference_signal_period_Edit)
        self.Upper_maximum_limit_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.Upper_maximum_limit_Edit.setObjectName("Upper_maximum_limit_Edit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Upper_maximum_limit_Edit)
        self.Upper_minimum_limit_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.Upper_minimum_limit_Edit.setObjectName("Upper_minimum_limit_Edit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Upper_minimum_limit_Edit)
        self.Lower_maximum_limit_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.Lower_maximum_limit_Edit.setObjectName("Lower_maximum_limit_Edit")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Lower_maximum_limit_Edit)
        self.Lower_minimum_limit_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.Lower_minimum_limit_Edit.setObjectName("Lower_minimum_limit_Edit")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Lower_minimum_limit_Edit)
        self.Alpha_value_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.Alpha_value_Edit.setObjectName("Alpha_value_Edit")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Alpha_value_Edit)
        self.Maximum_value_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.Maximum_value_Edit.setObjectName("Maximum_value_Edit")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Maximum_value_Edit)
        self.Minimum_value_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.Minimum_value_Edit.setObjectName("Minimum_value_Edit")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Minimum_value_Edit)
        self.gridLayout_5.addWidget(self.PIDWidget, 2, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.CaptureMode)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(410, 480, 381, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.ButtonsLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.ButtonsLayout.setContentsMargins(10, 11, 10, 11)
        self.ButtonsLayout.setSpacing(10)
        self.ButtonsLayout.setObjectName("ButtonsLayout")
        self.StartButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.StartButton.setObjectName("StartButton")
        self.ButtonsLayout.addWidget(self.StartButton)
        self.LoadButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.LoadButton.setObjectName("LoadButton")
        self.ButtonsLayout.addWidget(self.LoadButton)
        self.SaveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SaveButton.setObjectName("SaveButton")
        self.ButtonsLayout.addWidget(self.SaveButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.CaptureMode)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(410, 40, 381, 433))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.PlatformLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.PlatformLayout.setContentsMargins(11, 11, 11, 11)
        self.PlatformLayout.setSpacing(0)
        self.PlatformLayout.setObjectName("PlatformLayout")
        self.PlatformLabelLayout = QtWidgets.QVBoxLayout()
        self.PlatformLabelLayout.setContentsMargins(11, 11, 11, 11)
        self.PlatformLabelLayout.setSpacing(0)
        self.PlatformLabelLayout.setObjectName("PlatformLabelLayout")
        self.Capture_sample_time = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Capture_sample_time.setObjectName("Capture_sample_time")
        self.PlatformLabelLayout.addWidget(self.Capture_sample_time)
        self.Model_TGS_sensor = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Model_TGS_sensor.setObjectName("Model_TGS_sensor")
        self.PlatformLabelLayout.addWidget(self.Model_TGS_sensor)
        self.Electrovalves_port = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Electrovalves_port.setObjectName("Electrovalves_port")
        self.PlatformLabelLayout.addWidget(self.Electrovalves_port)
        self.Model_TyH_sensor = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Model_TyH_sensor.setObjectName("Model_TyH_sensor")
        self.PlatformLabelLayout.addWidget(self.Model_TyH_sensor)
        self.Reading_TyH_port = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Reading_TyH_port.setObjectName("Reading_TyH_port")
        self.PlatformLabelLayout.addWidget(self.Reading_TyH_port)
        self.VCC = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.VCC.setObjectName("VCC")
        self.PlatformLabelLayout.addWidget(self.VCC)
        self.Frecuency_TyH_samples = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Frecuency_TyH_samples.setObjectName("Frecuency_TyH_samples")
        self.PlatformLabelLayout.addWidget(self.Frecuency_TyH_samples)
        self.Frecuency_samples = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Frecuency_samples.setObjectName("Frecuency_samples")
        self.PlatformLabelLayout.addWidget(self.Frecuency_samples)
        self.Number_samples = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Number_samples.setObjectName("Number_samples")
        self.PlatformLabelLayout.addWidget(self.Number_samples)
        self.Valves_position = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Valves_position.setObjectName("Valves_position")
        self.PlatformLabelLayout.addWidget(self.Valves_position)
        self.Storage = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Storage.setObjectName("Storage")
        self.PlatformLabelLayout.addWidget(self.Storage)
        self.Resistance = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Resistance.setObjectName("Resistance")
        self.PlatformLabelLayout.addWidget(self.Resistance)
        self.Heating_port = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Heating_port.setObjectName("Heating_port")
        self.PlatformLabelLayout.addWidget(self.Heating_port)
        self.Engines_pin = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Engines_pin.setObjectName("Engines_pin")
        self.PlatformLabelLayout.addWidget(self.Engines_pin)
        self.Reading_TGS_port = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Reading_TGS_port.setObjectName("Reading_TGS_port")
        self.PlatformLabelLayout.addWidget(self.Reading_TGS_port)
        self.PlatformLayout.addLayout(self.PlatformLabelLayout)
        self.PlatformEntriesLayout = QtWidgets.QVBoxLayout()
        self.PlatformEntriesLayout.setContentsMargins(11, 11, 11, 11)
        self.PlatformEntriesLayout.setSpacing(0)
        self.PlatformEntriesLayout.setObjectName("PlatformEntriesLayout")
        self.Capture_sample_time_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Capture_sample_time_Edit.setObjectName("Capture_sample_time_Edit")
        self.PlatformEntriesLayout.addWidget(self.Capture_sample_time_Edit)
        self.Model_TGS_sensor_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Model_TGS_sensor_Edit.setObjectName("Model_TGS_sensor_Edit")
        self.PlatformEntriesLayout.addWidget(self.Model_TGS_sensor_Edit)
        self.Electrovalves_port_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Electrovalves_port_Edit.setObjectName("Electrovalves_port_Edit")
        self.PlatformEntriesLayout.addWidget(self.Electrovalves_port_Edit)
        self.Model_TyH_sensor_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Model_TyH_sensor_Edit.setObjectName("Model_TyH_sensor_Edit")
        self.PlatformEntriesLayout.addWidget(self.Model_TyH_sensor_Edit)
        self.Reading_TyH_port_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Reading_TyH_port_Edit.setObjectName("Reading_TyH_port_Edit")
        self.PlatformEntriesLayout.addWidget(self.Reading_TyH_port_Edit)
        self.VCC_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.VCC_Edit.setObjectName("VCC_Edit")
        self.PlatformEntriesLayout.addWidget(self.VCC_Edit)
        self.Frecuency_TyH_samples_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Frecuency_TyH_samples_Edit.setObjectName("Frecuency_TyH_samples_Edit")
        self.PlatformEntriesLayout.addWidget(self.Frecuency_TyH_samples_Edit)
        self.Frecuency_samples_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Frecuency_samples_Edit.setObjectName("Frecuency_samples_Edit")
        self.PlatformEntriesLayout.addWidget(self.Frecuency_samples_Edit)
        self.Number_samples_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Number_samples_Edit.setObjectName("Number_samples_Edit")
        self.PlatformEntriesLayout.addWidget(self.Number_samples_Edit)
        self.Valves_position_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Valves_position_Edit.setObjectName("Valves_position_Edit")
        self.PlatformEntriesLayout.addWidget(self.Valves_position_Edit)
        self.Storage_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Storage_Edit.setObjectName("Storage_Edit")
        self.PlatformEntriesLayout.addWidget(self.Storage_Edit)
        self.Resistance_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Resistance_Edit.setObjectName("Resistance_Edit")
        self.PlatformEntriesLayout.addWidget(self.Resistance_Edit)
        self.Heating_port_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Heating_port_Edit.setObjectName("Heating_port_Edit")
        self.PlatformEntriesLayout.addWidget(self.Heating_port_Edit)
        self.Engines_pin_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Engines_pin_Edit.setObjectName("Engines_pin_Edit")
        self.PlatformEntriesLayout.addWidget(self.Engines_pin_Edit)
        self.Reading_TGS_port_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.Reading_TGS_port_Edit.setObjectName("Reading_TGS_port_Edit")
        self.PlatformEntriesLayout.addWidget(self.Reading_TGS_port_Edit)
        self.PlatformLayout.addLayout(self.PlatformEntriesLayout)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.CaptureMode)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 391, 351))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.ExperimentLayout = QtWidgets.QVBoxLayout(self.gridLayoutWidget_4)
        self.ExperimentLayout.setContentsMargins(11, 11, 11, 11)
        self.ExperimentLayout.setSpacing(0)
        self.ExperimentLayout.setObjectName("ExperimentLayout")
        self.Modulation = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.Modulation.setObjectName("Modulation")
        self.Modulation.addItem("")
        self.Modulation.addItem("")
        self.Modulation.addItem("")
        self.Modulation.addItem("")
        self.ExperimentLayout.addWidget(self.Modulation)
        self.PuroLayout = QtWidgets.QHBoxLayout()
        self.PuroLayout.setContentsMargins(11, 11, 11, 11)
        self.PuroLayout.setSpacing(0)
        self.PuroLayout.setObjectName("PuroLayout")
        self.PuroLabelsLayout = QtWidgets.QVBoxLayout()
        self.PuroLabelsLayout.setContentsMargins(11, 11, 11, 11)
        self.PuroLabelsLayout.setSpacing(0)
        self.PuroLabelsLayout.setObjectName("PuroLabelsLayout")
        self.Number_experiments = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.Number_experiments.setEnabled(True)
        self.Number_experiments.setObjectName("Number_experiments")
        self.PuroLabelsLayout.addWidget(self.Number_experiments)
        self.Suction = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.Suction.setObjectName("Suction")
        self.PuroLabelsLayout.addWidget(self.Suction)
        self.Random_number_samples = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.Random_number_samples.setObjectName("Random_number_samples")
        self.PuroLabelsLayout.addWidget(self.Random_number_samples)
        self.Duration_stimulus = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.Duration_stimulus.setObjectName("Duration_stimulus")
        self.PuroLabelsLayout.addWidget(self.Duration_stimulus)
        self.Initial_samples = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.Initial_samples.setObjectName("Initial_samples")
        self.PuroLabelsLayout.addWidget(self.Initial_samples)
        self.Time_between_stimulus = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.Time_between_stimulus.setObjectName("Time_between_stimulus")
        self.PuroLabelsLayout.addWidget(self.Time_between_stimulus)
        self.Name_file = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.Name_file.setObjectName("Name_file")
        self.PuroLabelsLayout.addWidget(self.Name_file)
        self.Name_folder = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.Name_folder.setObjectName("Name_folder")
        self.PuroLabelsLayout.addWidget(self.Name_folder)
        self.Sleep = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.Sleep.setObjectName("Sleep")
        self.PuroLabelsLayout.addWidget(self.Sleep)
        self.Opening_valves = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.Opening_valves.setObjectName("Opening_valves")
        self.PuroLabelsLayout.addWidget(self.Opening_valves)
        self.Experiment_version = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.Experiment_version.setObjectName("Experiment_version")
        self.PuroLabelsLayout.addWidget(self.Experiment_version)
        self.PuroLayout.addLayout(self.PuroLabelsLayout)
        self.PuroEntriesLayout = QtWidgets.QVBoxLayout()
        self.PuroEntriesLayout.setContentsMargins(11, 11, 11, 11)
        self.PuroEntriesLayout.setSpacing(0)
        self.PuroEntriesLayout.setObjectName("PuroEntriesLayout")
        self.Number_experiments_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.Number_experiments_Edit.setObjectName("Number_experiments_Edit")
        self.PuroEntriesLayout.addWidget(self.Number_experiments_Edit)
        self.Suction_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.Suction_Edit.setObjectName("Suction_Edit")
        self.PuroEntriesLayout.addWidget(self.Suction_Edit)
        self.Random_number_samples_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.Random_number_samples_Edit.setObjectName("Random_number_samples_Edit")
        self.PuroEntriesLayout.addWidget(self.Random_number_samples_Edit)
        self.Duration_stimulus_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.Duration_stimulus_Edit.setObjectName("Duration_stimulus_Edit")
        self.PuroEntriesLayout.addWidget(self.Duration_stimulus_Edit)
        self.Initial_samples_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.Initial_samples_Edit.setObjectName("Initial_samples_Edit")
        self.PuroEntriesLayout.addWidget(self.Initial_samples_Edit)
        self.Time_between_stimulus_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.Time_between_stimulus_Edit.setObjectName("Time_between_stimulus_Edit")
        self.PuroEntriesLayout.addWidget(self.Time_between_stimulus_Edit)
        self.Name_file_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.Name_file_Edit.setObjectName("Name_file_Edit")
        self.PuroEntriesLayout.addWidget(self.Name_file_Edit)
        self.Name_folder_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.Name_folder_Edit.setObjectName("Name_folder_Edit")
        self.PuroEntriesLayout.addWidget(self.Name_folder_Edit)
        self.Sleep_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.Sleep_Edit.setObjectName("Sleep_Edit")
        self.PuroEntriesLayout.addWidget(self.Sleep_Edit)
        self.Opening_valves_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.Opening_valves_Edit.setObjectName("Opening_valves_Edit")
        self.PuroEntriesLayout.addWidget(self.Opening_valves_Edit)
        self.Experiment_version_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.Experiment_version_Edit.setObjectName("Experiment_version_Edit")
        self.PuroEntriesLayout.addWidget(self.Experiment_version_Edit)
        self.PuroLayout.addLayout(self.PuroEntriesLayout)
        self.ExperimentLayout.addLayout(self.PuroLayout)
        self.tabWidget.addTab(self.CaptureMode, "")
        self.Visual_Mode = QtWidgets.QWidget()
        self.Visual_Mode.setObjectName("Visual_Mode")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Visual_Mode)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(150, 20, 641, 421))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.Visual_Mode)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 60, 111, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_2.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_2.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.verticalLayoutWidget_4)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_2.addWidget(self.checkBox_6)
        self.checkBox = QtWidgets.QCheckBox(self.Visual_Mode)
        self.checkBox.setGeometry(QtCore.QRect(10, 430, 129, 21))
        self.checkBox.setObjectName("checkBox")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.Visual_Mode)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 310, 94, 71))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_3.setContentsMargins(6, 11, 6, 11)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.Visual_Mode)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 460, 251, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(11, 11, 6, 11)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(6, 11, 6, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_5.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.Visual_Mode, "")
        self.SSHButton = QtWidgets.QPushButton(self.centralWidget)
        self.SSHButton.setGeometry(QtCore.QRect(700, 10, 111, 23))
        self.SSHButton.setObjectName("SSHButton")
        self.tabWidget.raise_()
        self.SSHButton.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 834, 20))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Tendency.setText(_translate("MainWindow", "Tendency"))
        self.Sensor_temperature.setText(_translate("MainWindow", "Sensor temperature"))
        self.Execution_mode.setText(_translate("MainWindow", "Execution mode"))
        self.Temperature_mode.setText(_translate("MainWindow", "Temperature mode"))
        self.Maximum_temperature.setText(_translate("MainWindow", "Maximum temperature"))
        self.Minimum_temperature.setText(_translate("MainWindow", "Minimum temperature"))
        self.Reference_signal_period.setText(_translate("MainWindow", "Reference signal period"))
        self.Upper_maximum_limit.setText(_translate("MainWindow", "Upper maximum limit"))
        self.Upper_minimum_limit.setText(_translate("MainWindow", "Upper minimum limit"))
        self.Lower_maximum_limit.setText(_translate("MainWindow", "Lower maximum limit"))
        self.Lower_minimum_limit.setText(_translate("MainWindow", "Lower minimum limit"))
        self.Alpha_value.setText(_translate("MainWindow", "Alpha value"))
        self.Maximum_value.setText(_translate("MainWindow", "Maximum value"))
        self.Minimum_value.setText(_translate("MainWindow", "Minimum value"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.LoadButton.setText(_translate("MainWindow", "Load"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.Capture_sample_time.setText(_translate("MainWindow", "Capture sample time"))
        self.Model_TGS_sensor.setText(_translate("MainWindow", "Model TGS sensor"))
        self.Electrovalves_port.setText(_translate("MainWindow", "Electrovalves port"))
        self.Model_TyH_sensor.setText(_translate("MainWindow", "Model TyH sensor"))
        self.Reading_TyH_port.setText(_translate("MainWindow", "Reading TyH port"))
        self.VCC.setText(_translate("MainWindow", "VCC"))
        self.Frecuency_TyH_samples.setText(_translate("MainWindow", "Frecuency TyH samples(secs.)"))
        self.Frecuency_samples.setText(_translate("MainWindow", "Frecuency samples(seconds)"))
        self.Number_samples.setText(_translate("MainWindow", "Number samples"))
        self.Valves_position.setText(_translate("MainWindow", "Valves position"))
        self.Storage.setText(_translate("MainWindow", "Storage"))
        self.Resistance.setText(_translate("MainWindow", "Resistance"))
        self.Heating_port.setText(_translate("MainWindow", "Heating port"))
        self.Engines_pin.setText(_translate("MainWindow", "Engines pin"))
        self.Reading_TGS_port.setText(_translate("MainWindow", "Reading TGS port"))
        self.Modulation.setItemText(0, _translate("MainWindow", "Puro"))
        self.Modulation.setItemText(1, _translate("MainWindow", "Regresion"))
        self.Modulation.setItemText(2, _translate("MainWindow", "PID"))
        self.Modulation.setItemText(3, _translate("MainWindow", "Martinelli"))
        self.Number_experiments.setText(_translate("MainWindow", "Number experiments"))
        self.Suction.setText(_translate("MainWindow", "Suction"))
        self.Random_number_samples.setText(_translate("MainWindow", "Random number samples"))
        self.Duration_stimulus.setText(_translate("MainWindow", "Duration stimulus"))
        self.Initial_samples.setText(_translate("MainWindow", "Initial samples"))
        self.Time_between_stimulus.setText(_translate("MainWindow", "Time between stimulus"))
        self.Name_file.setText(_translate("MainWindow", "Name file"))
        self.Name_folder.setText(_translate("MainWindow", "Name folder"))
        self.Sleep.setText(_translate("MainWindow", "Sleep"))
        self.Opening_valves.setText(_translate("MainWindow", "Opening valves"))
        self.Experiment_version.setText(_translate("MainWindow", "Experiment version"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CaptureMode), _translate("MainWindow", "Capture Mode"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Visual_Mode), _translate("MainWindow", "Visual Mode"))
        self.SSHButton.setText(_translate("MainWindow", "SSH Connection"))

