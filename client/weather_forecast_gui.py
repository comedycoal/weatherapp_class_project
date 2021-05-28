# -*- coding: utf-8 -*-

import datetime
from logging import critical
from PySide2 import QtCore, QtGui, QtWidgets
from client import ClientProgram
from view_city_weather_gui import ViewCityWeather

class WeatherWindow(object):

    def onLogout(self, MainWindow):
        MainWindow.setWindowTitle("Login")
        self.logout_button.hide()
        self.label.hide()
        self.return_button.hide()
        self.name_label.hide()
        self.function_label.hide()
        self.view_button.hide()
        self.func1_button.hide()
        self.func2_button.hide()
        self.city_box.hide()
        self.date_box.hide()
        self.date_table.hide()

    def onReturn(self):
        self.function_label.show()
        self.view_button.hide()
        self.func1_button.show()
        self.func2_button.show()
        self.city_box.hide()
        self.date_box.hide()
        self.date_table.hide()

    def onFunc1(self, MainWindow, clientProgram):
        self.function_label.hide()
        self.func1_button.hide()
        self.func2_button.hide()
        self.view_button.clicked.disconnect()
        self.view_button.clicked.connect(lambda:self.onViewCity(MainWindow, clientProgram))
        self.view_button.show()
        self.return_button.show()
        self.city_box.show()
    
    def onViewCity(self, MainWindow, clientProgram):
        city = self.city_box.text()
        if city not in self.weatherdata["city_name"]:
            QtWidgets.QMessageBox.about(MainWindow, "", "Sai tên thành phố hoặc không có dữ liệu")
        else:
            city_id = self.weatherdata["city_id"]
            state, data = clientProgram.RequestWeatherDate7DaysOf(city_id)

            if state != clientProgram.State.SUCCEEDED:
                QtWidgets.QMessageBox.about(MainWindow, "", "Lỗi kết nối tới server")
            else:
                self.viewCity(MainWindow, data)

    def viewCity(self, MainWindow, data):
        viewCityWeather = ViewCityWeather()
        viewCityWeather.setupUI(MainWindow, data)

    def onFunc2(self, MainWindow, clientProgram):
        self.function_label.hide()
        self.func1_button.hide()
        self.func2_button.hide()
        self.view_button.clicked.disconnect()
        self.view_button.clicked.connect(lambda:self.onViewDate(MainWindow, clientProgram))
        self.view_button.show()
        self.return_button.show()
        self.date_box.show()
        self.date_table.hide()
        pass

    def onViewDate(self, MainWindow, clientProgram:ClientProgram):
        day = self.date_box.text()
        if day == 'today':
            state, self.weatherdata = clientProgram.RequestWeatherDataAll(datetime.date.today().strftime('%Y/%m/%d'))
        else:
            state, self.weatherdata = clientProgram.RequestWeatherDataAll(day)
        
        if state != clientProgram.State.SUCCEEDED:
            QtWidgets.QMessageBox.about(MainWindow, "", "Lỗi kết nối tới server")
        else:
            print(self.weatherdata)
            while (self.date_table.rowCount() > 1):
                self.date_table.removeRow(1)
                
            for i in range(len(self.weatherdata)):
                self.date_table.insertRow(i+1)
                for j in range(6):
                    item = QtWidgets.QTableWidgetItem()
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    font = QtGui.QFont()
                    font.setFamily("Helvetica")
                    item.setFont(font)
                    
                    item.setText(str(self.weatherdata[i][j]))
                    self.date_table.setItem(i+1, j+1, item)
            self.date_table.show()
    
    def setupUi(self, MainWindow, clientProgram):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 502)
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather"))

        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 901, 501))
        self.label.setStyleSheet("background-color: rgb(0, 0, 107);")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.label.show()

            # self.hello_user_label = QtWidgets.QLabel(MainWindow)
            # self.hello_user_label.setGeometry(QtCore.QRect(580, 10, 311, 31))
            # font = QtGui.QFont()
            # font.setFamily("Helvetica")
            # font.setPointSize(12)
            # font.setItalic(True)
            # self.hello_user_label.setFont(font)
            # self.hello_user_label.setLayoutDirection(QtCore.Qt.LeftToRight)
            # self.hello_user_label.setStyleSheet("color: rgb(255, 255, 255)")
            # self.hello_user_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            # self.hello_user_label.setObjectName("hello_user_label")
            # self.hello_user_label.raise_()
            # self.hello_user_label.setText(_translate("MainWindow", "Hello, " + ))
        
        self.logout_button = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.onLogout(MainWindow))
        self.logout_button.setGeometry(QtCore.QRect(800, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setItalic(True)
        self.logout_button.setFont(font)
        self.logout_button.setStyleSheet("color: rgb(255, 255, 255)")
        self.logout_button.setFlat(True)
        self.logout_button.setObjectName("logout_button")
        self.logout_button.setText(_translate("MainWindow", "Log out"))
        self.logout_button.show()

        self.return_button = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.onReturn())
        self.return_button.setGeometry(QtCore.QRect(810, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setItalic(True)
        self.return_button.setFont(font)
        self.return_button.setStyleSheet("color: rgb(255, 255, 255)")
        self.return_button.setFlat(True)
        self.return_button.setObjectName("return_button")
        self.return_button.setText(_translate("MainWindow", "Return"))
        self.return_button.hide()

        self.name_label = QtWidgets.QLabel(MainWindow)
        self.name_label.setGeometry(QtCore.QRect(180, 40, 541, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("color: rgb(212, 249, 255)")
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.name_label.setText(_translate("MainWindow", "WEATHER FORECAST"))
        self.name_label.show()

        self.function_label = QtWidgets.QLabel(MainWindow)
        self.function_label.setGeometry(QtCore.QRect(230, 130, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        self.function_label.setFont(font)
        self.function_label.setStyleSheet("color: rgb(255,255,255)")
        self.function_label.setAlignment(QtCore.Qt.AlignCenter)
        self.function_label.setObjectName("function_label")
        self.function_label.setText(_translate("MainWindow", "Chọn chức năng"))
        self.function_label.show()

        self.func1_button = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.onFunc1(MainWindow, clientProgram))
        self.func1_button.setGeometry(QtCore.QRect(180, 200, 201, 211))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.func1_button.setFont(font)
        self.func1_button.setObjectName("func1_button")
        self.func1_button.setText(_translate("MainWindow", "Xem thông tin \nthời tiết của\nmột thành phố"))
        self.func1_button.hide()

        self.func2_button = QtWidgets.QPushButton(MainWindow, clicked = lambda:self.onFunc2(MainWindow, clientProgram))
        self.func2_button.setGeometry(QtCore.QRect(530, 200, 201, 211))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        self.func2_button.setFont(font)
        self.func2_button.setObjectName("func2_button")
        self.func2_button.setText(_translate("MainWindow", "Xem thông tin\nthời tiết của\ncác thành phố\ntrong một ngày"))
        self.func2_button.show()

        self.city_box = QtWidgets.QLineEdit(MainWindow)
        self.city_box.setGeometry(QtCore.QRect(60, 120, 240, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.city_box.setFont(font)
        self.city_box.setObjectName("city_box")
        self.city_box.setText(_translate("MainWindow", "Nhập thành phố (không dấu)"))
        self.city_box.hide()

        self.date_box = QtWidgets.QLineEdit(MainWindow)
        self.date_box.setGeometry(QtCore.QRect(60, 120, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.date_box.setFont(font)
        self.date_box.setObjectName("date_box")
        self.date_box.setText(_translate("MainWindow", "Nhập ngày (yyyy/mm/dd)"))
        self.date_box.hide()

        self.view_button = QtWidgets.QPushButton(MainWindow)
        self.view_button.setGeometry(QtCore.QRect(320, 120, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        font.setItalic(True)
        self.view_button.setFont(font)
        self.view_button.setObjectName("view_button")
        self.view_button.setText(_translate("MainWindow", "Xem"))
        self.view_button.clicked.connect(lambda:self.onViewCity(MainWindow, clientProgram))
        self.view_button.clicked.connect(lambda:self.onViewDate(MainWindow, clientProgram))
        self.view_button.hide()

        self.date_table = QtWidgets.QTableWidget(MainWindow)
        self.date_table.setGeometry(QtCore.QRect(60, 190, 771, 281))
        self.date_table.setMinimumSize(QtCore.QSize(771, 0))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(11)
        self.date_table.setFont(font)
        self.date_table.setRowCount(1)
        self.date_table.setColumnCount(6)
        self.date_table.setObjectName("date_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        item.setFont(font)
        self.date_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        item.setFont(font)
        self.date_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        item.setFont(font)
        self.date_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        item.setFont(font)
        self.date_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        item.setFont(font)
        self.date_table.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        item.setFont(font)
        self.date_table.setItem(0, 5, item)
        self.date_table.horizontalHeader().setVisible(False)
        self.date_table.horizontalHeader().setCascadingSectionResizes(True)
        self.date_table.horizontalHeader().setHighlightSections(False)
        self.date_table.horizontalHeader().setStretchLastSection(True)
        self.date_table.verticalHeader().setVisible(True)
        self.date_table.verticalHeader().setCascadingSectionResizes(False)
        self.date_table.verticalHeader().setHighlightSections(True)
        self.date_table.verticalHeader().setMinimumSectionSize(30)
        self.date_table.verticalHeader().setSortIndicatorShown(False)
        self.date_table.verticalHeader().setStretchLastSection(False)
        self.date_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.date_table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.date_table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.date_table.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.date_table.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.date_table.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

        __sortingEnabled = self.date_table.isSortingEnabled()
        self.date_table.setSortingEnabled(False)
        item = self.date_table.item(0, 0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.date_table.item(0, 1)
        item.setText(_translate("MainWindow", "City"))
        item = self.date_table.item(0, 2)
        item.setText(_translate("MainWindow", "Weather"))
        item = self.date_table.item(0, 3)
        item.setText(_translate("MainWindow", "Temperature"))
        item = self.date_table.item(0, 4)
        item.setText(_translate("MainWindow", "Humidity"))
        item = self.date_table.item(0, 5)
        item.setText(_translate("MainWindow", "Wind Speed"))
        self.date_table.setSortingEnabled(__sortingEnabled)
        self.date_table.hide()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = WeatherWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
