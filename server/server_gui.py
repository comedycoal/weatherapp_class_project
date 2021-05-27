# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from server import ServerProgram
from admin_gui import AdminProgram

class ServuiGUI(object):

    def openServer(self):
        # Add number of max clients using self.num_client_box

        self.serverProgram = ServerProgram()
        self.serverProgram.Open()
        pass

    def closeServer(self):
        self.serverProgram.End()
        pass

    def updateDatabase(self):
        adminProgram =  AdminProgram()
        adminWindow = QtWidgets.QWidget()
        adminProgram.setupUI(adminWindow, self.serverProgram)
        adminWindow.show()
        pass


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(349, 257)


        self.num_client_label = QtWidgets.QLabel(MainWindow)
        self.num_client_label.setGeometry(QtCore.QRect(20, 70, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.num_client_label.setFont(font)
        self.num_client_label.setObjectName("num_client_label")

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

        self.num_client_box = QtWidgets.QLineEdit(MainWindow)
        self.num_client_box.setGeometry(QtCore.QRect(210, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.num_client_box.setFont(font)
        self.num_client_box.setAlignment(QtCore.Qt.AlignCenter)
        self.num_client_box.setObjectName("num_client_box")

        self.opensv_button = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.openServer())
        self.opensv_button.setGeometry(QtCore.QRect(20, 110, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.opensv_button.setFont(font)
        icon = QtGui.QIcon.fromTheme("☺")
        self.opensv_button.setIcon(icon)
        self.opensv_button.setAutoDefault(False)
        self.opensv_button.setObjectName("opensv_button")

        self.closesv_button = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.closeServer())
        self.closesv_button.setGeometry(QtCore.QRect(170, 110, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.closesv_button.setFont(font)
        icon = QtGui.QIcon.fromTheme("☺")
        self.closesv_button.setIcon(icon)
        self.closesv_button.setAutoDefault(False)
        self.closesv_button.setObjectName("closesv_button")

        self.update_database_button = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.updateDatabase())
        self.update_database_button.setGeometry(QtCore.QRect(20, 180, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.update_database_button.setFont(font)
        icon = QtGui.QIcon.fromTheme("☺")
        self.update_database_button.setIcon(icon)
        self.update_database_button.setAutoDefault(False)
        self.update_database_button.setObjectName("update_database_button")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.num_client_label.setText(_translate("MainWindow", "Số client tối đa"))
        self.WELCOME_label.setText(_translate("MainWindow", "SERVER"))
        self.opensv_button.setText(_translate("MainWindow", "Mở Server"))
        self.closesv_button.setText(_translate("MainWindow", "Đóng Server"))
        self.update_database_button.setText(_translate("MainWindow", "Sửa database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = ServuiGUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
