# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(875, 650)
        MainWindow.setMinimumSize(QtCore.QSize(875, 650))
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
        self.tendency = QtWidgets.QLabel(self.RegresionWidget)
        self.tendency.setObjectName("tendency")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tendency)
        self.sensor_temperature = QtWidgets.QLabel(self.RegresionWidget)
        self.sensor_temperature.setObjectName("sensor_temperature")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sensor_temperature)
        self.tendency_Edit = QtWidgets.QLineEdit(self.RegresionWidget)
        self.tendency_Edit.setObjectName("tendency_Edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tendency_Edit)
        self.sensor_temperature_Edit = QtWidgets.QLineEdit(self.RegresionWidget)
        self.sensor_temperature_Edit.setObjectName("sensor_temperature_Edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sensor_temperature_Edit)
        self.gridLayout_5.addWidget(self.RegresionWidget, 0, 0, 1, 1)
        self.MartinelliWidget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.MartinelliWidget.setObjectName("MartinelliWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.MartinelliWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setSpacing(0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.execution_mode = QtWidgets.QLabel(self.MartinelliWidget)
        self.execution_mode.setObjectName("execution_mode")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.execution_mode)
        self.temperature_mode = QtWidgets.QLabel(self.MartinelliWidget)
        self.temperature_mode.setObjectName("temperature_mode")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.temperature_mode)
        self.maximum_temperature = QtWidgets.QLabel(self.MartinelliWidget)
        self.maximum_temperature.setObjectName("maximum_temperature")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.maximum_temperature)
        self.minimum_temperature = QtWidgets.QLabel(self.MartinelliWidget)
        self.minimum_temperature.setObjectName("minimum_temperature")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.minimum_temperature)
        self.execution_mode_Edit = QtWidgets.QLineEdit(self.MartinelliWidget)
        self.execution_mode_Edit.setObjectName("execution_mode_Edit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.execution_mode_Edit)
        self.temperature_mode_Edit = QtWidgets.QLineEdit(self.MartinelliWidget)
        self.temperature_mode_Edit.setObjectName("temperature_mode_Edit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.temperature_mode_Edit)
        self.maximum_temperature_Edit = QtWidgets.QLineEdit(self.MartinelliWidget)
        self.maximum_temperature_Edit.setObjectName("maximum_temperature_Edit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.maximum_temperature_Edit)
        self.minimum_temperature_Edit = QtWidgets.QLineEdit(self.MartinelliWidget)
        self.minimum_temperature_Edit.setObjectName("minimum_temperature_Edit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.minimum_temperature_Edit)
        self.gridLayout_5.addWidget(self.MartinelliWidget, 1, 0, 1, 1)
        self.PIDWidget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.PIDWidget.setObjectName("PIDWidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.PIDWidget)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setSpacing(0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.reference_signal_period = QtWidgets.QLabel(self.PIDWidget)
        self.reference_signal_period.setObjectName("reference_signal_period")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.reference_signal_period)
        self.upper_maximum_limit = QtWidgets.QLabel(self.PIDWidget)
        self.upper_maximum_limit.setObjectName("upper_maximum_limit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.upper_maximum_limit)
        self.upper_minimum_limit = QtWidgets.QLabel(self.PIDWidget)
        self.upper_minimum_limit.setObjectName("upper_minimum_limit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.upper_minimum_limit)
        self.lower_maximum_limit = QtWidgets.QLabel(self.PIDWidget)
        self.lower_maximum_limit.setObjectName("lower_maximum_limit")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lower_maximum_limit)
        self.lower_minimum_limit = QtWidgets.QLabel(self.PIDWidget)
        self.lower_minimum_limit.setObjectName("lower_minimum_limit")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lower_minimum_limit)
        self.alpha_value = QtWidgets.QLabel(self.PIDWidget)
        self.alpha_value.setObjectName("alpha_value")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.alpha_value)
        self.maximum_value = QtWidgets.QLabel(self.PIDWidget)
        self.maximum_value.setObjectName("maximum_value")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.maximum_value)
        self.minimum_value = QtWidgets.QLabel(self.PIDWidget)
        self.minimum_value.setEnabled(True)
        self.minimum_value.setObjectName("minimum_value")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.minimum_value)
        self.reference_signal_period_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.reference_signal_period_Edit.setObjectName("reference_signal_period_Edit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reference_signal_period_Edit)
        self.upper_maximum_limit_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.upper_maximum_limit_Edit.setObjectName("upper_maximum_limit_Edit")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.upper_maximum_limit_Edit)
        self.upper_minimum_limit_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.upper_minimum_limit_Edit.setObjectName("upper_minimum_limit_Edit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.upper_minimum_limit_Edit)
        self.lower_maximum_limit_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.lower_maximum_limit_Edit.setObjectName("lower_maximum_limit_Edit")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lower_maximum_limit_Edit)
        self.lower_minimum_limit_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.lower_minimum_limit_Edit.setObjectName("lower_minimum_limit_Edit")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lower_minimum_limit_Edit)
        self.alpha_value_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.alpha_value_Edit.setObjectName("alpha_value_Edit")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.alpha_value_Edit)
        self.maximum_value_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.maximum_value_Edit.setObjectName("maximum_value_Edit")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.maximum_value_Edit)
        self.minimum_value_Edit = QtWidgets.QLineEdit(self.PIDWidget)
        self.minimum_value_Edit.setObjectName("minimum_value_Edit")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.minimum_value_Edit)
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
        self.capture_sample_time = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.capture_sample_time.setObjectName("capture_sample_time")
        self.PlatformLabelLayout.addWidget(self.capture_sample_time)
        self.model_tgs_sensor = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.model_tgs_sensor.setObjectName("model_tgs_sensor")
        self.PlatformLabelLayout.addWidget(self.model_tgs_sensor)
        self.electrovalves_port = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.electrovalves_port.setObjectName("electrovalves_port")
        self.PlatformLabelLayout.addWidget(self.electrovalves_port)
        self.model_tyh_sensor = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.model_tyh_sensor.setObjectName("model_tyh_sensor")
        self.PlatformLabelLayout.addWidget(self.model_tyh_sensor)
        self.reading_tyh_port = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.reading_tyh_port.setObjectName("reading_tyh_port")
        self.PlatformLabelLayout.addWidget(self.reading_tyh_port)
        self.vcc = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.vcc.setObjectName("vcc")
        self.PlatformLabelLayout.addWidget(self.vcc)
        self.frecuency_tyh_samples = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.frecuency_tyh_samples.setObjectName("frecuency_tyh_samples")
        self.PlatformLabelLayout.addWidget(self.frecuency_tyh_samples)
        self.frecuency_samples = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.frecuency_samples.setObjectName("frecuency_samples")
        self.PlatformLabelLayout.addWidget(self.frecuency_samples)
        self.number_samples = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.number_samples.setObjectName("number_samples")
        self.PlatformLabelLayout.addWidget(self.number_samples)
        self.valves_position = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.valves_position.setObjectName("valves_position")
        self.PlatformLabelLayout.addWidget(self.valves_position)
        self.storage = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.storage.setObjectName("storage")
        self.PlatformLabelLayout.addWidget(self.storage)
        self.resistance = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.resistance.setObjectName("resistance")
        self.PlatformLabelLayout.addWidget(self.resistance)
        self.heating_port = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.heating_port.setObjectName("heating_port")
        self.PlatformLabelLayout.addWidget(self.heating_port)
        self.engines_pin = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.engines_pin.setObjectName("engines_pin")
        self.PlatformLabelLayout.addWidget(self.engines_pin)
        self.reading_tgs_port = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.reading_tgs_port.setObjectName("reading_tgs_port")
        self.PlatformLabelLayout.addWidget(self.reading_tgs_port)
        self.PlatformLayout.addLayout(self.PlatformLabelLayout)
        self.PlatformEntriesLayout = QtWidgets.QVBoxLayout()
        self.PlatformEntriesLayout.setContentsMargins(11, 11, 11, 11)
        self.PlatformEntriesLayout.setSpacing(0)
        self.PlatformEntriesLayout.setObjectName("PlatformEntriesLayout")
        self.capture_sample_time_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.capture_sample_time_Edit.setObjectName("capture_sample_time_Edit")
        self.PlatformEntriesLayout.addWidget(self.capture_sample_time_Edit)
        self.model_tgs_sensor_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.model_tgs_sensor_Edit.setObjectName("model_tgs_sensor_Edit")
        self.PlatformEntriesLayout.addWidget(self.model_tgs_sensor_Edit)
        self.electrovalves_port_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.electrovalves_port_Edit.setObjectName("electrovalves_port_Edit")
        self.PlatformEntriesLayout.addWidget(self.electrovalves_port_Edit)
        self.model_tyh_sensor_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.model_tyh_sensor_Edit.setObjectName("model_tyh_sensor_Edit")
        self.PlatformEntriesLayout.addWidget(self.model_tyh_sensor_Edit)
        self.reading_tyh_port_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.reading_tyh_port_Edit.setObjectName("reading_tyh_port_Edit")
        self.PlatformEntriesLayout.addWidget(self.reading_tyh_port_Edit)
        self.vcc_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.vcc_Edit.setObjectName("vcc_Edit")
        self.PlatformEntriesLayout.addWidget(self.vcc_Edit)
        self.frecuency_tyh_samples_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.frecuency_tyh_samples_Edit.setObjectName("frecuency_tyh_samples_Edit")
        self.PlatformEntriesLayout.addWidget(self.frecuency_tyh_samples_Edit)
        self.frecuency_samples_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.frecuency_samples_Edit.setObjectName("frecuency_samples_Edit")
        self.PlatformEntriesLayout.addWidget(self.frecuency_samples_Edit)
        self.number_samples_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.number_samples_Edit.setObjectName("number_samples_Edit")
        self.PlatformEntriesLayout.addWidget(self.number_samples_Edit)
        self.valves_position_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.valves_position_Edit.setObjectName("valves_position_Edit")
        self.PlatformEntriesLayout.addWidget(self.valves_position_Edit)
        self.storage_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.storage_Edit.setObjectName("storage_Edit")
        self.PlatformEntriesLayout.addWidget(self.storage_Edit)
        self.resistance_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.resistance_Edit.setObjectName("resistance_Edit")
        self.PlatformEntriesLayout.addWidget(self.resistance_Edit)
        self.heating_port_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.heating_port_Edit.setObjectName("heating_port_Edit")
        self.PlatformEntriesLayout.addWidget(self.heating_port_Edit)
        self.engines_pin_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.engines_pin_Edit.setObjectName("engines_pin_Edit")
        self.PlatformEntriesLayout.addWidget(self.engines_pin_Edit)
        self.reading_tgs_port_Edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.reading_tgs_port_Edit.setObjectName("reading_tgs_port_Edit")
        self.PlatformEntriesLayout.addWidget(self.reading_tgs_port_Edit)
        self.PlatformLayout.addLayout(self.PlatformEntriesLayout)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.CaptureMode)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 391, 351))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.ExperimentLayout = QtWidgets.QVBoxLayout(self.gridLayoutWidget_4)
        self.ExperimentLayout.setContentsMargins(11, 11, 11, 11)
        self.ExperimentLayout.setSpacing(0)
        self.ExperimentLayout.setObjectName("ExperimentLayout")
        self.modulation = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.modulation.setObjectName("modulation")
        self.modulation.addItem("")
        self.modulation.addItem("")
        self.modulation.addItem("")
        self.modulation.addItem("")
        self.ExperimentLayout.addWidget(self.modulation)
        self.PuroLayout = QtWidgets.QHBoxLayout()
        self.PuroLayout.setContentsMargins(11, 11, 11, 11)
        self.PuroLayout.setSpacing(0)
        self.PuroLayout.setObjectName("PuroLayout")
        self.PuroLabelsLayout = QtWidgets.QVBoxLayout()
        self.PuroLabelsLayout.setContentsMargins(11, 11, 11, 11)
        self.PuroLabelsLayout.setSpacing(0)
        self.PuroLabelsLayout.setObjectName("PuroLabelsLayout")
        self.number_experiments = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.number_experiments.setEnabled(True)
        self.number_experiments.setObjectName("number_experiments")
        self.PuroLabelsLayout.addWidget(self.number_experiments)
        self.suction = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.suction.setObjectName("suction")
        self.PuroLabelsLayout.addWidget(self.suction)
        self.random_number_samples = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.random_number_samples.setObjectName("random_number_samples")
        self.PuroLabelsLayout.addWidget(self.random_number_samples)
        self.duration_stimulus = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.duration_stimulus.setObjectName("duration_stimulus")
        self.PuroLabelsLayout.addWidget(self.duration_stimulus)
        self.initial_samples = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.initial_samples.setObjectName("initial_samples")
        self.PuroLabelsLayout.addWidget(self.initial_samples)
        self.time_between_stimulus = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.time_between_stimulus.setObjectName("time_between_stimulus")
        self.PuroLabelsLayout.addWidget(self.time_between_stimulus)
        self.name_file = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.name_file.setObjectName("name_file")
        self.PuroLabelsLayout.addWidget(self.name_file)
        self.name_folder = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.name_folder.setObjectName("name_folder")
        self.PuroLabelsLayout.addWidget(self.name_folder)
        self.sleep = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.sleep.setObjectName("sleep")
        self.PuroLabelsLayout.addWidget(self.sleep)
        self.opening_valves = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.opening_valves.setObjectName("opening_valves")
        self.PuroLabelsLayout.addWidget(self.opening_valves)
        self.experiment_version = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.experiment_version.setObjectName("experiment_version")
        self.PuroLabelsLayout.addWidget(self.experiment_version)
        self.PuroLayout.addLayout(self.PuroLabelsLayout)
        self.PuroEntriesLayout = QtWidgets.QVBoxLayout()
        self.PuroEntriesLayout.setContentsMargins(11, 11, 11, 11)
        self.PuroEntriesLayout.setSpacing(0)
        self.PuroEntriesLayout.setObjectName("PuroEntriesLayout")
        self.number_experiments_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.number_experiments_Edit.setObjectName("number_experiments_Edit")
        self.PuroEntriesLayout.addWidget(self.number_experiments_Edit)
        self.suction_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.suction_Edit.setObjectName("suction_Edit")
        self.PuroEntriesLayout.addWidget(self.suction_Edit)
        self.random_number_samples_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.random_number_samples_Edit.setObjectName("random_number_samples_Edit")
        self.PuroEntriesLayout.addWidget(self.random_number_samples_Edit)
        self.duration_stimulus_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.duration_stimulus_Edit.setObjectName("duration_stimulus_Edit")
        self.PuroEntriesLayout.addWidget(self.duration_stimulus_Edit)
        self.initial_samples_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.initial_samples_Edit.setObjectName("initial_samples_Edit")
        self.PuroEntriesLayout.addWidget(self.initial_samples_Edit)
        self.time_between_stimulus_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.time_between_stimulus_Edit.setObjectName("time_between_stimulus_Edit")
        self.PuroEntriesLayout.addWidget(self.time_between_stimulus_Edit)
        self.name_file_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.name_file_Edit.setObjectName("name_file_Edit")
        self.PuroEntriesLayout.addWidget(self.name_file_Edit)
        self.name_folder_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.name_folder_Edit.setObjectName("name_folder_Edit")
        self.PuroEntriesLayout.addWidget(self.name_folder_Edit)
        self.sleep_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.sleep_Edit.setObjectName("sleep_Edit")
        self.PuroEntriesLayout.addWidget(self.sleep_Edit)
        self.opening_valves_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.opening_valves_Edit.setObjectName("opening_valves_Edit")
        self.PuroEntriesLayout.addWidget(self.opening_valves_Edit)
        self.experiment_version_Edit = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.experiment_version_Edit.setObjectName("experiment_version_Edit")
        self.PuroEntriesLayout.addWidget(self.experiment_version_Edit)
        self.PuroLayout.addLayout(self.PuroEntriesLayout)
        self.ExperimentLayout.addLayout(self.PuroLayout)
        self.tabWidget.addTab(self.CaptureMode, "")
        self.Visual_Mode = QtWidgets.QWidget()
        self.Visual_Mode.setObjectName("Visual_Mode")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Visual_Mode)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 771, 461))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        #######################################################################
        figure = Figure()
        self.canvas = FigureCanvas(figure)
        self.verticalLayout.addWidget(self.canvas)
        self.ax = figure.add_subplot(111)
        self.ax.clear()
        #######################################################################
        self.ConfPlotButton = QtWidgets.QPushButton(self.Visual_Mode)
        self.ConfPlotButton.setGeometry(QtCore.QRect(20, 490, 181, 21))
        self.ConfPlotButton.setObjectName("ConfPlotButton")
        self.tabWidget.addTab(self.Visual_Mode, "")
        self.SSHButton = QtWidgets.QPushButton(self.centralWidget)
        self.SSHButton.setGeometry(QtCore.QRect(700, 10, 111, 23))
        self.SSHButton.setObjectName("SSHButton")
        self.SSHcheckBox = QtWidgets.QCheckBox(self.centralWidget)
        self.SSHcheckBox.setGeometry(QtCore.QRect(580, 10, 111, 31))
        self.SSHcheckBox.setObjectName("SSHcheckBox")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 875, 20))
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
        self.tendency.setText(_translate("MainWindow", "Tendency"))
        self.sensor_temperature.setText(_translate("MainWindow", "Sensor temperature"))
        self.execution_mode.setText(_translate("MainWindow", "Execution mode"))
        self.temperature_mode.setText(_translate("MainWindow", "Temperature mode"))
        self.maximum_temperature.setText(_translate("MainWindow", "Maximum temperature"))
        self.minimum_temperature.setText(_translate("MainWindow", "Minimum temperature"))
        self.reference_signal_period.setText(_translate("MainWindow", "Reference signal period"))
        self.upper_maximum_limit.setText(_translate("MainWindow", "Upper maximum limit"))
        self.upper_minimum_limit.setText(_translate("MainWindow", "Upper minimum limit"))
        self.lower_maximum_limit.setText(_translate("MainWindow", "Lower maximum limit"))
        self.lower_minimum_limit.setText(_translate("MainWindow", "Lower minimum limit"))
        self.alpha_value.setText(_translate("MainWindow", "Alpha value"))
        self.maximum_value.setText(_translate("MainWindow", "Maximum value"))
        self.minimum_value.setText(_translate("MainWindow", "Minimum value"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.LoadButton.setText(_translate("MainWindow", "Load"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))
        self.capture_sample_time.setText(_translate("MainWindow", "Capture sample time"))
        self.model_tgs_sensor.setText(_translate("MainWindow", "Model TGS sensor"))
        self.electrovalves_port.setText(_translate("MainWindow", "Electrovalves port"))
        self.model_tyh_sensor.setText(_translate("MainWindow", "Model TyH sensor"))
        self.reading_tyh_port.setText(_translate("MainWindow", "Reading TyH port"))
        self.vcc.setText(_translate("MainWindow", "VCC"))
        self.frecuency_tyh_samples.setText(_translate("MainWindow", "Frecuency TyH samples(secs.)"))
        self.frecuency_samples.setText(_translate("MainWindow", "Frecuency samples(seconds)"))
        self.number_samples.setText(_translate("MainWindow", "Number samples"))
        self.valves_position.setText(_translate("MainWindow", "Valves position"))
        self.storage.setText(_translate("MainWindow", "Storage"))
        self.resistance.setText(_translate("MainWindow", "Resistance"))
        self.heating_port.setText(_translate("MainWindow", "Heating port"))
        self.engines_pin.setText(_translate("MainWindow", "Engines pin"))
        self.reading_tgs_port.setText(_translate("MainWindow", "Reading TGS port"))
        self.modulation.setItemText(0, _translate("MainWindow", "Puro"))
        self.modulation.setItemText(1, _translate("MainWindow", "Regresion"))
        self.modulation.setItemText(2, _translate("MainWindow", "PID"))
        self.modulation.setItemText(3, _translate("MainWindow", "Martinelli"))
        self.number_experiments.setText(_translate("MainWindow", "Number experiments"))
        self.suction.setText(_translate("MainWindow", "Suction"))
        self.random_number_samples.setText(_translate("MainWindow", "Random number samples"))
        self.duration_stimulus.setText(_translate("MainWindow", "Duration stimulus"))
        self.initial_samples.setText(_translate("MainWindow", "Initial samples"))
        self.time_between_stimulus.setText(_translate("MainWindow", "Time between stimulus"))
        self.name_file.setText(_translate("MainWindow", "Name file"))
        self.name_folder.setText(_translate("MainWindow", "Name folder"))
        self.sleep.setText(_translate("MainWindow", "Sleep"))
        self.opening_valves.setText(_translate("MainWindow", "Opening valves"))
        self.experiment_version.setText(_translate("MainWindow", "Experiment version"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CaptureMode), _translate("MainWindow", "Capture Mode"))
        self.ConfPlotButton.setText(_translate("MainWindow", "Configurar representacion"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Visual_Mode), _translate("MainWindow", "Visual Mode"))
        self.SSHButton.setText(_translate("MainWindow", "SSH Connection"))
        self.SSHcheckBox.setText(_translate("MainWindow", "Habilitar SSH"))

