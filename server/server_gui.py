# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from server import ServerProgram
from admin_gui import AdminProgram

class ServuiGUI(object):
    def __init__(self):
        self.started = None
        self.serverProgram = ServerProgram()
        
    def openServer(self, MainWindow):
        host = self.host_box.text()
        port = int(self.port_box.text())
        max_client = int(self.num_client_box.text())
        if not self.started:
            self.serverProgram = ServerProgram()
            self.started = True
            QtWidgets.QMessageBox.about(MainWindow, "", "Mở thành công")
            self.serverProgram.Start(host=host, port=port, num_clients=max_client)

    def closeServer(self, MainWindow):
        if self.started:
            self.serverProgram.End()
            self.serverProgram = None
            self.started = False
            QtWidgets.QMessageBox.about(MainWindow, "", "Đóng thành công")

    def updateDatabase(self):
        adminProgram = AdminProgram()
        adminWindow = QtWidgets.QWidget()
        adminProgram.setupUi(adminWindow, self.serverProgram)
        adminWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(349, 349)

        self.WELCOME_label = QtWidgets.QLabel(MainWindow)
        self.WELCOME_label.setGeometry(QtCore.QRect(0, 20, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.WELCOME_label.setFont(font)
        self.WELCOME_label.setStyleSheet("color:rgb(85, 0, 0)")
        self.WELCOME_label.setAlignment(QtCore.Qt.AlignCenter)
        self.WELCOME_label.setObjectName("WELCOME_label")

        self.port_label = QtWidgets.QLabel(MainWindow)
        self.port_label.setGeometry(QtCore.QRect(20, 110, 50, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(15)
        self.port_label.setFont(font)
        self.port_label.setObjectName("port_label")

        self.port_box = QtWidgets.QLineEdit(MainWindow)
        self.port_box.setGeometry(QtCore.QRect(80, 110, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.port_box.setFont(font)
        self.port_box.setAlignment(QtCore.Qt.AlignCenter)
        self.port_box.setObjectName("port_box")

        self.host_label = QtWidgets.QLabel(MainWindow)
        self.host_label.setGeometry(QtCore.QRect(20, 70, 50, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(15)
        self.host_label.setFont(font)
        self.host_label.setObjectName("host_label")

        self.host_box = QtWidgets.QLineEdit(MainWindow)
        self.host_box.setGeometry(QtCore.QRect(80, 70, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.host_box.setFont(font)
        self.host_box.setAlignment(QtCore.Qt.AlignCenter)
        self.host_box.setObjectName("host_box")

        self.num_client_label = QtWidgets.QLabel(MainWindow)
        self.num_client_label.setGeometry(QtCore.QRect(20, 150, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(15)
        self.num_client_label.setFont(font)
        self.num_client_label.setObjectName("num_client_label")

        self.num_client_box = QtWidgets.QLineEdit(MainWindow)
        self.num_client_box.setGeometry(QtCore.QRect(210, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.num_client_box.setFont(font)
        self.num_client_box.setAlignment(QtCore.Qt.AlignCenter)
        self.num_client_box.setObjectName("num_client_box")

        self.opensv_button = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.openServer(MainWindow))
        self.opensv_button.setGeometry(QtCore.QRect(20, 190, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.opensv_button.setFont(font)
        icon = QtGui.QIcon.fromTheme("☺")
        self.opensv_button.setIcon(icon)
        self.opensv_button.setAutoDefault(False)
        self.opensv_button.setObjectName("opensv_button")

        self.closesv_button = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.closeServer(MainWindow))
        self.closesv_button.setGeometry(QtCore.QRect(170, 190, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.closesv_button.setFont(font)
        icon = QtGui.QIcon.fromTheme("☺")
        self.closesv_button.setIcon(icon)
        self.closesv_button.setAutoDefault(False)
        self.closesv_button.setObjectName("closesv_button")

        self.update_database_button = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.updateDatabase())
        self.update_database_button.setGeometry(QtCore.QRect(20, 260, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.update_database_button.setFont(font)
        icon = QtGui.QIcon.fromTheme("☺")
        self.update_database_button.setIcon(icon)
        self.update_database_button.setAutoDefault(False)
        self.update_database_button.setObjectName("update_database_button")

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Server"))
        self.host_label.setText(_translate("MainWindow", "Host"))
        self.port_label.setText(_translate("MainWindow", "Port"))
        self.host_box.setText(_translate("MainWindow", "127.0.0.1"))
        self.port_box.setText(_translate("MainWindow", "7878"))
        self.num_client_label.setText(_translate("MainWindow", "Số client tối đa"))
        self.num_client_box.setText(_translate("MainWindow", "10"))
        self.WELCOME_label.setText(_translate("MainWindow", "SERVER"))
        self.opensv_button.setText(_translate("MainWindow", "Mở Server"))
        self.closesv_button.setText(_translate("MainWindow", "Đóng Server"))
        self.update_database_button.setText(_translate("MainWindow", "Sửa database"))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

if __name__ == "__main__":
    import sys
    from os import environ

    def suppress_qt_warnings():
        environ["QT_DEVICE_PIXEL_RATIO"] = "0"
        environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        environ["QT_SCREEN_SCALE_FACTORS"] = "1"
        environ["QT_SCALE_FACTOR"] = "1"

    suppress_qt_warnings()
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = ServuiGUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())