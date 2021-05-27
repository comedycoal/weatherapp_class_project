# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5.sip import enableautoconversion

from client import ClientProgram
from login_window_gui import LoginWindow


class ClientUI(object):

    def __init__(self):
        self.clientProgram = ClientProgram()

    def Connect(self, MainWindow):
        ip = self.IP_box.text()
        port = self.port_box.text()
        
        state = self.clientProgram.Connect(ip, port)
        if state == False:
            QMessageBox.about(MainWindow, "", "Kết nối thành công")
            self.connect_button.hide()
            self.disconnect_button.show()

            login_window_ui = LoginWindow()
            self.loginWindow = QWidget()
            login_window_ui.setupUi(self.loginWindow, self.clientProgram)
            self.loginWindow.show()
        else:
            QMessageBox.about(MainWindow, "", "Kết nối thất bại")
    
    def Disconnect(self):
        self.clientProgram.Disconnect()
        self.disconnect_button.hide()
        self.connect_button.show()

    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(282, 214)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Client"))

        self.background_image = QtWidgets.QLabel(MainWindow)
        self.background_image.setGeometry(QtCore.QRect(0, 0, 281, 211))
        self.background_image.setStyleSheet("background-color: rgb(238, 255, 238);")
        self.background_image.setText("")
        self.background_image.setScaledContents(True)
        self.background_image.setObjectName("background_image")

        self.IP_box = QtWidgets.QLineEdit(MainWindow)
        self.IP_box.setGeometry(QtCore.QRect(40, 90, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.IP_box.setFont(font)
        self.IP_box.setStyleSheet("background-color: rgb(246, 252, 255);")
        self.IP_box.setObjectName("IP_box")
        self.IP_box.setText(_translate("MainWindow", "Nhập IP"))

        self.port_box = QtWidgets.QLineEdit(MainWindow)
        self.port_box.setGeometry(QtCore.QRect(40, 150, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.port_box.setFont(font)
        self.port_box.setStyleSheet("background-color: rgb(246, 252, 255);")
        self.port_box.setObjectName("port_box")
        self.port_box.setText(_translate("MainWindow", "Nhập port"))

        self.connect_button = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.Connect(MainWindow))
        self.connect_button.setGeometry(QtCore.QRect(160, 150, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.connect_button.setFont(font)
        self.connect_button.setStyleSheet("background-color: rgb(224, 237, 255)")
        self.connect_button.setCheckable(False)
        self.connect_button.setChecked(False)
        self.connect_button.setObjectName("connect_button")
        self.connect_button.setText(_translate("MainWindow", "Kết nối"))

        self.disconnect_button = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.Disconnect())
        self.disconnect_button.setGeometry(QtCore.QRect(160, 150, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.disconnect_button.setFont(font)
        self.disconnect_button.setStyleSheet("background-color: rgb(224, 237, 255)")
        self.disconnect_button.setCheckable(False)
        self.disconnect_button.setChecked(False)
        self.disconnect_button.setObjectName("connect_button")
        self.disconnect_button.setText(_translate("MainWindow", "Ngắt"))
        self.disconnect_button.hide()

        self.WELCOME_label = QtWidgets.QLabel(MainWindow)
        self.WELCOME_label.setGeometry(QtCore.QRect(40, 20, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.WELCOME_label.setFont(font)
        self.WELCOME_label.setStyleSheet("color: rgb(255, 24, 128);")
        self.WELCOME_label.setAlignment(QtCore.Qt.AlignCenter)
        self.WELCOME_label.setObjectName("WELCOME_label")
        self.WELCOME_label.setText(_translate("MainWindow", "WELCOME"))
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = ClientUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
