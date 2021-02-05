# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'runUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 299, 59))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nameTitle = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.nameTitle.setFont(font)
        self.nameTitle.setObjectName("nameTitle")
        self.verticalLayout.addWidget(self.nameTitle)
        self.versionString = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.versionString.setFont(font)
        self.versionString.setObjectName("versionString")
        self.verticalLayout.addWidget(self.versionString)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 200, 731, 159))
        self.widget1.setObjectName("widget1")
        self.controlHStack = QtWidgets.QHBoxLayout(self.widget1)
        self.controlHStack.setContentsMargins(0, 0, 0, 0)
        self.controlHStack.setSpacing(10)
        self.controlHStack.setObjectName("controlHStack")
        self.controlStack = QtWidgets.QHBoxLayout()
        self.controlStack.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.controlStack.setSpacing(20)
        self.controlStack.setObjectName("controlStack")
        self.resetBtn = QtWidgets.QPushButton(self.widget1)
        self.resetBtn.setMinimumSize(QtCore.QSize(100, 100))
        self.resetBtn.setSizeIncrement(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.resetBtn.setFont(font)
        self.resetBtn.setAutoDefault(True)
        self.resetBtn.setDefault(False)
        self.resetBtn.setFlat(False)
        self.resetBtn.setObjectName("resetBtn")
        self.controlStack.addWidget(self.resetBtn)
        self.startBtn = QtWidgets.QPushButton(self.widget1)
        self.startBtn.setMinimumSize(QtCore.QSize(100, 100))
        self.startBtn.setSizeIncrement(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.startBtn.setFont(font)
        self.startBtn.setAutoDefault(True)
        self.startBtn.setDefault(False)
        self.startBtn.setFlat(False)
        self.startBtn.setObjectName("startBtn")
        self.controlStack.addWidget(self.startBtn)
        self.controlHStack.addLayout(self.controlStack)
        spacerItem = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.controlHStack.addItem(spacerItem)
        self.countStack = QtWidgets.QVBoxLayout()
        self.countStack.setSpacing(0)
        self.countStack.setObjectName("countStack")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.countStack.addWidget(self.label_3)
        self.countText = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.countText.setFont(font)
        self.countText.setAlignment(QtCore.Qt.AlignCenter)
        self.countText.setObjectName("countText")
        self.countStack.addWidget(self.countText)
        self.controlHStack.addLayout(self.countStack)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(30, 410, 451, 104))
        self.widget2.setObjectName("widget2")
        self.runSelectStack = QtWidgets.QHBoxLayout(self.widget2)
        self.runSelectStack.setContentsMargins(0, 0, 0, 0)
        self.runSelectStack.setObjectName("runSelectStack")
        self.runTextStack = QtWidgets.QVBoxLayout()
        self.runTextStack.setSpacing(10)
        self.runTextStack.setObjectName("runTextStack")
        self.runMode = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.runMode.setFont(font)
        self.runMode.setObjectName("runMode")
        self.runTextStack.addWidget(self.runMode)
        self.label_5 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.runTextStack.addWidget(self.label_5)
        self.runSelectStack.addLayout(self.runTextStack)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.runSelectStack.addItem(spacerItem1)
        self.runmodeButtonStack = QtWidgets.QHBoxLayout()
        self.runmodeButtonStack.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.runmodeButtonStack.setSpacing(20)
        self.runmodeButtonStack.setObjectName("runmodeButtonStack")
        self.normalBtn = QtWidgets.QPushButton(self.widget2)
        self.normalBtn.setMinimumSize(QtCore.QSize(100, 100))
        self.normalBtn.setSizeIncrement(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.normalBtn.setFont(font)
        self.normalBtn.setAutoDefault(True)
        self.normalBtn.setDefault(False)
        self.normalBtn.setFlat(False)
        self.normalBtn.setObjectName("normalBtn")
        self.runmodeButtonStack.addWidget(self.normalBtn)
        self.trainBtn = QtWidgets.QPushButton(self.widget2)
        self.trainBtn.setMinimumSize(QtCore.QSize(100, 100))
        self.trainBtn.setSizeIncrement(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Gotham")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.trainBtn.setFont(font)
        self.trainBtn.setAutoDefault(True)
        self.trainBtn.setDefault(False)
        self.trainBtn.setFlat(False)
        self.trainBtn.setObjectName("trainBtn")
        self.runmodeButtonStack.addWidget(self.trainBtn)
        self.runSelectStack.addLayout(self.runmodeButtonStack)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuCountVision = QtWidgets.QMenu(self.menubar)
        self.menuCountVision.setObjectName("menuCountVision")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCountVision.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameTitle.setText(_translate("MainWindow", "COUNTVISION"))
        self.versionString.setText(_translate("MainWindow", "2021.05.01"))
        self.resetBtn.setText(_translate("MainWindow", "RESET"))
        self.startBtn.setText(_translate("MainWindow", "START"))
        self.label_3.setText(_translate("MainWindow", "COUNT"))
        self.countText.setText(_translate("MainWindow", "25"))
        self.runMode.setText(_translate("MainWindow", "RUN MODE"))
        self.label_5.setText(_translate("MainWindow", "NORMAL"))
        self.normalBtn.setText(_translate("MainWindow", "NORMAL"))
        self.trainBtn.setText(_translate("MainWindow", "TRAIN"))
        self.menuCountVision.setTitle(_translate("MainWindow", "CountVision"))
