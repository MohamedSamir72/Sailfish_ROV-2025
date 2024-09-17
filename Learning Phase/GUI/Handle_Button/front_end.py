# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 1020)
        MainWindow.setMinimumSize(QtCore.QSize(840, 1020))
        MainWindow.setMaximumSize(QtCore.QSize(840, 1020))
        MainWindow.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(67, 117, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(200, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.counter = QtWidgets.QLabel(self.centralwidget)
        self.counter.setMinimumSize(QtCore.QSize(200, 50))
        self.counter.setMaximumSize(QtCore.QSize(16777215, 100))
        self.counter.setStyleSheet("color: rgb(0, 255, 0);\n"
"font: 32pt \"MS Shell Dlg 2\";")
        self.counter.setAlignment(QtCore.Qt.AlignCenter)
        self.counter.setObjectName("counter")
        self.verticalLayout.addWidget(self.counter)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 600))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.up_bt = QtWidgets.QPushButton(self.widget)
        self.up_bt.setMinimumSize(QtCore.QSize(200, 120))
        self.up_bt.setStyleSheet("background-color: rgb(14, 14, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid white;\n"
"border-radius: 20px;")
        self.up_bt.setObjectName("up_bt")
        self.verticalLayout_2.addWidget(self.up_bt)
        self.down_bt = QtWidgets.QPushButton(self.widget)
        self.down_bt.setMinimumSize(QtCore.QSize(200, 120))
        self.down_bt.setStyleSheet("background-color: rgb(14, 14, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid white;\n"
"border-radius: 20px;")
        self.down_bt.setObjectName("down_bt")
        self.verticalLayout_2.addWidget(self.down_bt)
        self.reset_bt = QtWidgets.QPushButton(self.widget)
        self.reset_bt.setMinimumSize(QtCore.QSize(200, 120))
        self.reset_bt.setStyleSheet("background-color: rgb(14, 14, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 0, 0);\n"
"border: 4px solid red;\n"
"border-radius: 20px;")
        self.reset_bt.setObjectName("reset_bt")
        self.verticalLayout_2.addWidget(self.reset_bt)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Counter"))
        self.counter.setText(_translate("MainWindow", "0"))
        self.up_bt.setText(_translate("MainWindow", "UP"))
        self.down_bt.setText(_translate("MainWindow", "DOWN"))
        self.reset_bt.setText(_translate("MainWindow", "Reset"))