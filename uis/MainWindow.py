# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui',
# licensing of 'MainWindow.ui' applies.
#
# Created: Tue Mar  8 09:52:50 2022
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    # def __init__(self):

        # set app icon



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 411)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setObjectName("label_output")
        self.gridLayout.addWidget(self.label_output, 4, 0, 1, 1)
        self.pushButton_OK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.gridLayout.addWidget(self.pushButton_OK, 5, 2, 1, 1)
        self.pushButton_inputFilesFeatures = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inputFilesFeatures.setObjectName("pushButton_inputFilesFeatures")
        self.gridLayout.addWidget(self.pushButton_inputFilesFeatures, 1, 2, 1, 2)
        self.plainTextEdit_features = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_features.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.plainTextEdit_features.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.plainTextEdit_features.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_features.setOverwriteMode(False)
        self.plainTextEdit_features.setTabStopWidth(80)
        self.plainTextEdit_features.setTabStopDistance(80.0)
        self.plainTextEdit_features.setObjectName("plainTextEdit_features")
        self.gridLayout.addWidget(self.plainTextEdit_features, 1, 1, 1, 1)
        self.label_inputFeatures = QtWidgets.QLabel(self.centralwidget)
        self.label_inputFeatures.setObjectName("label_inputFeatures")
        self.gridLayout.addWidget(self.label_inputFeatures, 1, 0, 1, 1)
        self.lineEdit_outputDir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_outputDir.setObjectName("lineEdit_outputDir")
        self.gridLayout.addWidget(self.lineEdit_outputDir, 4, 1, 1, 1)
        self.label_inputLimit = QtWidgets.QLabel(self.centralwidget)
        self.label_inputLimit.setObjectName("label_inputLimit")
        self.gridLayout.addWidget(self.label_inputLimit, 3, 0, 1, 1)
        self.pushButton_Cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.gridLayout.addWidget(self.pushButton_Cancel, 5, 3, 1, 1)
        self.pushButton_inputFileLimit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inputFileLimit.setObjectName("pushButton_inputFileLimit")
        self.gridLayout.addWidget(self.pushButton_inputFileLimit, 3, 2, 1, 2)
        self.lineEdit_inputFileLimit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_inputFileLimit.setObjectName("lineEdit_inputFileLimit")
        self.gridLayout.addWidget(self.lineEdit_inputFileLimit, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(575, 27, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 2)
        self.pushButton_outputDir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_outputDir.setObjectName("pushButton_outputDir")
        self.gridLayout.addWidget(self.pushButton_outputDir, 4, 2, 1, 2)
        self.label_inputLito = QtWidgets.QLabel(self.centralwidget)
        self.label_inputLito.setObjectName("label_inputLito")
        self.gridLayout.addWidget(self.label_inputLito, 2, 0, 1, 1)
        self.lineEdit_inputFileLito = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_inputFileLito.setObjectName("lineEdit_inputFileLito")
        self.gridLayout.addWidget(self.lineEdit_inputFileLito, 2, 1, 1, 1)
        self.pushButton_inputFileLito = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inputFileLito.setObjectName("pushButton_inputFileLito")
        self.gridLayout.addWidget(self.pushButton_inputFileLito, 2, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Predictive Geology Map", None, -1))
        self.label_output.setText(QtWidgets.QApplication.translate("MainWindow", "Output Folder:", None, -1))
        self.pushButton_OK.setText(QtWidgets.QApplication.translate("MainWindow", "OK", None, -1))
        self.pushButton_inputFilesFeatures.setText(QtWidgets.QApplication.translate("MainWindow", "Selecionar Arquivos", None, -1))
        self.label_inputFeatures.setText(QtWidgets.QApplication.translate("MainWindow", "Sensoriamento (features):", None, -1))
        self.label_inputLimit.setText(QtWidgets.QApplication.translate("MainWindow", "Limite:", None, -1))
        self.pushButton_Cancel.setText(QtWidgets.QApplication.translate("MainWindow", "Cancel", None, -1))
        self.pushButton_inputFileLimit.setText(QtWidgets.QApplication.translate("MainWindow", "Selecionar Arquivo", None, -1))
        self.pushButton_outputDir.setText(QtWidgets.QApplication.translate("MainWindow", "Selecionar Pasta", None, -1))
        self.label_inputLito.setText(QtWidgets.QApplication.translate("MainWindow", "Litologia (target):", None, -1))
        self.pushButton_inputFileLito.setText(QtWidgets.QApplication.translate("MainWindow", "Selecionar Arquivo", None, -1))

