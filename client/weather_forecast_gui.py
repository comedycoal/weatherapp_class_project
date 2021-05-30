# -*- coding: utf-8 -*-
import os.path
from pathlib import Path
import datetime
from logging import critical
from PySide2 import QtCore, QtGui, QtWidgets
from client import ClientProgram

PIC_PATH = os.path.join(Path(__file__).parent.absolute(),"pic")

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
        self.weather_layout_background.hide()
        self.day1_pic.hide()
        self.day2_pic.hide()
        self.day3_pic.hide()
        self.day4_pic.hide()
        self.day5_pic.hide()
        self.day6_pic.hide()
        self.day7_pic.hide()
        self.temperature1.hide()
        self.temperature2.hide()
        self.temperature3.hide()
        self.temperature4.hide()
        self.temperature5.hide()
        self.temperature6.hide()
        self.temperature7.hide()
        self.wind1.hide()
        self.wind2.hide()
        self.wind3.hide()
        self.wind4.hide()
        self.wind5.hide()
        self.wind6.hide()
        self.wind7.hide()
        self.humidity1.hide()
        self.humidity2.hide()
        self.humidity3.hide()
        self.humidity4.hide()
        self.humidity5.hide()
        self.humidity6.hide()
        self.humidity7.hide()
        self.date1.hide()
        self.date2.hide()
        self.date3.hide()
        self.date4.hide()
        self.date5.hide()
        self.date6.hide()
        self.date7.hide()

    def onReturn(self):
        self.function_label.show()
        self.view_button.hide()
        self.func1_button.show()
        self.func2_button.show()
        self.city_box.hide()
        self.date_box.hide()
        self.date_table.hide()
        self.weather_layout_background.hide()
        self.day1_pic.hide()
        self.day2_pic.hide()
        self.day3_pic.hide()
        self.day4_pic.hide()
        self.day5_pic.hide()
        self.day6_pic.hide()
        self.day7_pic.hide()
        self.temperature1.hide()
        self.temperature2.hide()
        self.temperature3.hide()
        self.temperature4.hide()
        self.temperature5.hide()
        self.temperature6.hide()
        self.temperature7.hide()
        self.wind1.hide()
        self.wind2.hide()
        self.wind3.hide()
        self.wind4.hide()
        self.wind5.hide()
        self.wind6.hide()
        self.wind7.hide()
        self.humidity1.hide()
        self.humidity2.hide()
        self.humidity3.hide()
        self.humidity4.hide()
        self.humidity5.hide()
        self.humidity6.hide()
        self.humidity7.hide()
        self.date1.hide()
        self.date2.hide()
        self.date3.hide()
        self.date4.hide()
        self.date5.hide()
        self.date6.hide()
        self.date7.hide()

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
        city_name = self.city_box.text()
        if self.weatherdata == None:
            QtWidgets.QMessageBox.about(MainWindow, "", "Chưa có dữ liệu, vui lòng chọn chức năng còn lại trước")
            self.onReturn()
        else:
            city_id = None
            for data in self.weatherdata:
                if data[1] == city_name:
                    city_id = data[0]
            if city_id == None:
                QtWidgets.QMessageBox.about(MainWindow, "", "Sai tên thành phố hoặc không có dữ liệu về thành phố")
            else:
                state, data = clientProgram.RequestWeatherDate7DaysOf(city_id)
                if state != clientProgram.State.SUCCEEDED:
                    QtWidgets.QMessageBox.about(MainWindow, "", "Lỗi kết nối tới server")
                else:
                    self.viewCity(MainWindow, data)

    def showWidgets(self):
        self.weather_layout_background.show()
        self.day1_pic.show()
        self.day2_pic.show()
        self.day3_pic.show()
        self.day4_pic.show()
        self.day5_pic.show()
        self.day6_pic.show()
        self.day7_pic.show()
        self.temperature1.show()
        self.temperature2.show()
        self.temperature3.show()
        self.temperature4.show()
        self.temperature5.show()
        self.temperature6.show()
        self.temperature7.show()
        self.wind1.show()
        self.wind2.show()
        self.wind3.show()
        self.wind4.show()
        self.wind5.show()
        self.wind6.show()
        self.wind7.show()
        self.humidity1.show()
        self.humidity2.show()
        self.humidity3.show()
        self.humidity4.show()
        self.humidity5.show()
        self.humidity6.show()
        self.humidity7.show()
        self.date1.show()
        self.date2.show()
        self.date3.show()
        self.date4.show()
        self.date5.show()
        self.date6.show()
        self.date7.show()

    def updateForecast(self, data):

        city_name = data[0]
        weather_by_date_dict = data[1]
        print(weather_by_date_dict)
        weather = ["Sunny", "Cloudy", "Sunny + Cloudy", "Rainy", "Stormy", "Lightning"]
        weatherPic = ["Sunny.png", "Cloudy.png", "SunnyCloudy.png", "Rainy.png", "Stormy.png", "Lightning.png"]
        dataPic = []

        listkeys = sorted(weather_by_date_dict)
        listvals = [weather_by_date_dict[x] for x in listkeys]
        for item in listvals:
            for i in range(6):
                if item[0] == weather[i]:
                    dataPic.append(weatherPic[i])
                    break
            else:
                dataPic.append('ukn.png')
            

        _translate = QtCore.QCoreApplication.translate

        self.day1_pic.setPixmap(QtGui.QPixmap(os.path.join(PIC_PATH, dataPic[0])))
        self.temperature1.setText(_translate("MainWindow", str(listvals[0][1]) + chr(176) + "C"))
        self.wind1.setText(_translate("MainWindow", "Wind: " + str(listvals[0][2])))
        self.humidity1.setText(_translate("MainWindow", "Humid: " + str(listvals[0][3])))
        self.date1.setText(_translate("MainWindow", listkeys[0]))

        self.day2_pic.setPixmap(QtGui.QPixmap(os.path.join(PIC_PATH, dataPic[1])))
        self.temperature2.setText(_translate("MainWindow", str(listvals[1][1]) + chr(176) + "C"))
        self.wind2.setText(_translate("MainWindow", "Wind: " + str(listvals[1][2])))
        self.humidity2.setText(_translate("MainWindow", "Humid: " + str(listvals[1][3])))
        self.date2.setText(_translate("MainWindow", listkeys[1]))

        self.day3_pic.setPixmap(QtGui.QPixmap(os.path.join(PIC_PATH, dataPic[2])))
        self.temperature3.setText(_translate("MainWindow", str(listvals[2][1]) + chr(176) + "C"))
        self.wind3.setText(_translate("MainWindow", "Wind: " + str(listvals[2][2])))
        self.humidity3.setText(_translate("MainWindow", "Humid: " + str(listvals[2][3])))
        self.date3.setText(_translate("MainWindow", listkeys[2]))

        self.day4_pic.setPixmap(QtGui.QPixmap(os.path.join(PIC_PATH, dataPic[3])))
        self.temperature4.setText(_translate("MainWindow", str(listvals[3][1]) + chr(176) + "C"))
        self.wind4.setText(_translate("MainWindow", "Wind: " + str(listvals[3][2])))
        self.humidity4.setText(_translate("MainWindow", "Humid: " + str(listvals[3][3])))
        self.date4.setText(_translate("MainWindow", listkeys[3]))

        self.day5_pic.setPixmap(QtGui.QPixmap(os.path.join(PIC_PATH, dataPic[4])))
        self.temperature5.setText(_translate("MainWindow", str(listvals[4][1]) + chr(176) + "C"))
        self.wind5.setText(_translate("MainWindow", "Wind: " + str(listvals[4][2])))
        self.humidity5.setText(_translate("MainWindow", "Humid: " + str(listvals[4][3])))
        self.date5.setText(_translate("MainWindow", listkeys[4]))

        self.day6_pic.setPixmap(QtGui.QPixmap(os.path.join(PIC_PATH, dataPic[5])))
        self.temperature6.setText(_translate("MainWindow", str(listvals[5][1]) + chr(176) + "C"))
        self.wind6.setText(_translate("MainWindow", "Wind: " + str(listvals[5][2])))
        self.humidity6.setText(_translate("MainWindow", "Humid: " + str(listvals[5][3])))
        self.date6.setText(_translate("MainWindow", listkeys[5]))

        self.day7_pic.setPixmap(QtGui.QPixmap(os.path.join(PIC_PATH, dataPic[6])))
        self.temperature7.setText(_translate("MainWindow", str(listvals[6][1]) + chr(176) + "C"))
        self.wind7.setText(_translate("MainWindow", "Wind: " + str(listvals[6][2])))
        self.humidity7.setText(_translate("MainWindow", "Humid: " + str(listvals[6][3])))
        self.date7.setText(_translate("MainWindow", listkeys[6]))

    def viewCity(self, MainWindow, data):
        # viewCityWeather = ViewCityWeather()
        # viewCityWeather.setupUI(MainWindow, data)
        self.weather_layout_background = QtWidgets.QLabel(MainWindow)
        self.weather_layout_background.setGeometry(QtCore.QRect(30, 200, 841, 261))
        self.weather_layout_background.setStyleSheet("background-color: rgb(0, 0, 127)")
        self.weather_layout_background.setText("")
        self.weather_layout_background.setObjectName("weather_layout_background")

        self.day1_pic = QtWidgets.QLabel(MainWindow)
        self.day1_pic.setGeometry(QtCore.QRect(40, 210, 101, 81))
        self.day1_pic.setText("")
        self.day1_pic.setScaledContents(True)
        self.day1_pic.setObjectName("day1_pic")

        self.temperature1 = QtWidgets.QLabel(MainWindow)
        self.temperature1.setGeometry(QtCore.QRect(40, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.temperature1.setFont(font)
        self.temperature1.setStyleSheet("color: rgb(255, 103, 118)")
        self.temperature1.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature1.setObjectName("temperature1")

        self.humidity1 = QtWidgets.QLabel(MainWindow)
        self.humidity1.setGeometry(QtCore.QRect(40, 340, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.humidity1.setFont(font)
        self.humidity1.setStyleSheet("color: rgb(142, 172, 255)")
        self.humidity1.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity1.setObjectName("humidity1")

        self.wind1 = QtWidgets.QLabel(MainWindow)
        self.wind1.setGeometry(QtCore.QRect(40, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wind1.setFont(font)
        self.wind1.setStyleSheet("color: rgb(247, 255, 211)")
        self.wind1.setAlignment(QtCore.Qt.AlignCenter)
        self.wind1.setObjectName("wind1")

        self.date1 = QtWidgets.QLabel(MainWindow)
        self.date1.setGeometry(QtCore.QRect(40, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date1.setFont(font)
        self.date1.setStyleSheet("color: rgb(43, 255, 78)")
        self.date1.setAlignment(QtCore.Qt.AlignCenter)
        self.date1.setObjectName("date1")

        self.wind2 = QtWidgets.QLabel(MainWindow)
        self.wind2.setGeometry(QtCore.QRect(160, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wind2.setFont(font)
        self.wind2.setStyleSheet("color: rgb(247, 255, 211)")
        self.wind2.setAlignment(QtCore.Qt.AlignCenter)
        self.wind2.setObjectName("wind2")

        self.day2_pic = QtWidgets.QLabel(MainWindow)
        self.day2_pic.setGeometry(QtCore.QRect(160, 210, 101, 81))
        self.day2_pic.setText("")
        self.day2_pic.setScaledContents(True)
        self.day2_pic.setObjectName("day2_pic")

        self.temperature2 = QtWidgets.QLabel(MainWindow)
        self.temperature2.setGeometry(QtCore.QRect(160, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.temperature2.setFont(font)
        self.temperature2.setStyleSheet("color: rgb(255, 103, 118)")
        self.temperature2.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature2.setObjectName("temperature2")

        self.date2 = QtWidgets.QLabel(MainWindow)
        self.date2.setGeometry(QtCore.QRect(160, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date2.setFont(font)
        self.date2.setStyleSheet("color: rgb(43, 255, 78)")
        self.date2.setAlignment(QtCore.Qt.AlignCenter)
        self.date2.setObjectName("date2")

        self.humidity2 = QtWidgets.QLabel(MainWindow)
        self.humidity2.setGeometry(QtCore.QRect(160, 340, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.humidity2.setFont(font)
        self.humidity2.setStyleSheet("color: rgb(142, 172, 255)")
        self.humidity2.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity2.setObjectName("humidity2")

        self.wind3 = QtWidgets.QLabel(MainWindow)
        self.wind3.setGeometry(QtCore.QRect(280, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wind3.setFont(font)
        self.wind3.setStyleSheet("color: rgb(247, 255, 211)")
        self.wind3.setAlignment(QtCore.Qt.AlignCenter)
        self.wind3.setObjectName("wind3")

        self.day3_pic = QtWidgets.QLabel(MainWindow)
        self.day3_pic.setGeometry(QtCore.QRect(280, 210, 101, 81))
        self.day3_pic.setText("")
        self.day3_pic.setScaledContents(True)
        self.day3_pic.setObjectName("day3_pic")

        self.temperature3 = QtWidgets.QLabel(MainWindow)
        self.temperature3.setGeometry(QtCore.QRect(280, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.temperature3.setFont(font)
        self.temperature3.setStyleSheet("color: rgb(255, 103, 118)")
        self.temperature3.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature3.setObjectName("temperature3")

        self.date3 = QtWidgets.QLabel(MainWindow)
        self.date3.setGeometry(QtCore.QRect(280, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date3.setFont(font)
        self.date3.setStyleSheet("color: rgb(43, 255, 78)")
        self.date3.setAlignment(QtCore.Qt.AlignCenter)
        self.date3.setObjectName("date3")

        self.humidity3 = QtWidgets.QLabel(MainWindow)
        self.humidity3.setGeometry(QtCore.QRect(280, 340, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.humidity3.setFont(font)
        self.humidity3.setStyleSheet("color: rgb(142, 172, 255)")
        self.humidity3.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity3.setObjectName("humidity3")

        self.wind4 = QtWidgets.QLabel(MainWindow)
        self.wind4.setGeometry(QtCore.QRect(400, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wind4.setFont(font)
        self.wind4.setStyleSheet("color: rgb(247, 255, 211)")
        self.wind4.setAlignment(QtCore.Qt.AlignCenter)
        self.wind4.setObjectName("wind4")

        self.day4_pic = QtWidgets.QLabel(MainWindow)
        self.day4_pic.setGeometry(QtCore.QRect(400, 210, 101, 81))
        self.day4_pic.setText("")
        self.day4_pic.setScaledContents(True)
        self.day4_pic.setObjectName("day4_pic")

        self.temperature4 = QtWidgets.QLabel(MainWindow)
        self.temperature4.setGeometry(QtCore.QRect(400, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.temperature4.setFont(font)
        self.temperature4.setStyleSheet("color: rgb(255, 103, 118)")
        self.temperature4.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature4.setObjectName("temperature4")

        self.date4 = QtWidgets.QLabel(MainWindow)
        self.date4.setGeometry(QtCore.QRect(400, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date4.setFont(font)
        self.date4.setStyleSheet("color: rgb(43, 255, 78)")
        self.date4.setAlignment(QtCore.Qt.AlignCenter)
        self.date4.setObjectName("date4")

        self.humidity4 = QtWidgets.QLabel(MainWindow)
        self.humidity4.setGeometry(QtCore.QRect(400, 340, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.humidity4.setFont(font)
        self.humidity4.setStyleSheet("color: rgb(142, 172, 255)")
        self.humidity4.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity4.setObjectName("humidity4")

        self.day5_pic = QtWidgets.QLabel(MainWindow)
        self.day5_pic.setGeometry(QtCore.QRect(520, 210, 101, 81))
        self.day5_pic.setText("")
        self.day5_pic.setScaledContents(True)
        self.day5_pic.setObjectName("day5_pic")

        self.wind5 = QtWidgets.QLabel(MainWindow)
        self.wind5.setGeometry(QtCore.QRect(520, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wind5.setFont(font)
        self.wind5.setStyleSheet("color: rgb(247, 255, 211)")
        self.wind5.setAlignment(QtCore.Qt.AlignCenter)
        self.wind5.setObjectName("wind5")

        self.date5 = QtWidgets.QLabel(MainWindow)
        self.date5.setGeometry(QtCore.QRect(520, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date5.setFont(font)
        self.date5.setStyleSheet("color: rgb(43, 255, 78)")
        self.date5.setAlignment(QtCore.Qt.AlignCenter)
        self.date5.setObjectName("date5")

        self.humidity5 = QtWidgets.QLabel(MainWindow)
        self.humidity5.setGeometry(QtCore.QRect(520, 340, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.humidity5.setFont(font)
        self.humidity5.setStyleSheet("color: rgb(142, 172, 255)")
        self.humidity5.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity5.setObjectName("humidity5")

        self.temperature5 = QtWidgets.QLabel(MainWindow)
        self.temperature5.setGeometry(QtCore.QRect(520, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.temperature5.setFont(font)
        self.temperature5.setStyleSheet("color: rgb(255, 103, 118)")
        self.temperature5.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature5.setObjectName("temperature5")

        self.wind6 = QtWidgets.QLabel(MainWindow)
        self.wind6.setGeometry(QtCore.QRect(640, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wind6.setFont(font)
        self.wind6.setStyleSheet("color: rgb(247, 255, 211)")
        self.wind6.setAlignment(QtCore.Qt.AlignCenter)
        self.wind6.setObjectName("wind6")

        self.humidity6 = QtWidgets.QLabel(MainWindow)
        self.humidity6.setGeometry(QtCore.QRect(640, 340, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.humidity6.setFont(font)
        self.humidity6.setStyleSheet("color: rgb(142, 172, 255)")
        self.humidity6.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity6.setObjectName("humidity6")

        self.date6 = QtWidgets.QLabel(MainWindow)
        self.date6.setGeometry(QtCore.QRect(640, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date6.setFont(font)
        self.date6.setStyleSheet("color: rgb(43, 255, 78)")
        self.date6.setAlignment(QtCore.Qt.AlignCenter)
        self.date6.setObjectName("date6")

        self.day6_pic = QtWidgets.QLabel(MainWindow)
        self.day6_pic.setGeometry(QtCore.QRect(640, 210, 101, 81))
        self.day6_pic.setText("")
        self.day6_pic.setScaledContents(True)
        self.day6_pic.setObjectName("day6_pic")

        self.temperature6 = QtWidgets.QLabel(MainWindow)
        self.temperature6.setGeometry(QtCore.QRect(640, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.temperature6.setFont(font)
        self.temperature6.setStyleSheet("color: rgb(255, 103, 118)")
        self.temperature6.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature6.setObjectName("temperature6")

        self.wind7 = QtWidgets.QLabel(MainWindow)
        self.wind7.setGeometry(QtCore.QRect(760, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wind7.setFont(font)
        self.wind7.setStyleSheet("color: rgb(247, 255, 211)")
        self.wind7.setAlignment(QtCore.Qt.AlignCenter)
        self.wind7.setObjectName("wind7")
        self.humidity7 = QtWidgets.QLabel(MainWindow)
        self.humidity7.setGeometry(QtCore.QRect(760, 340, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.humidity7.setFont(font)
        self.humidity7.setStyleSheet("color: rgb(142, 172, 255)")
        self.humidity7.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity7.setObjectName("humidity7")

        self.date7 = QtWidgets.QLabel(MainWindow)
        self.date7.setGeometry(QtCore.QRect(760, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date7.setFont(font)
        self.date7.setStyleSheet("color: rgb(43, 255, 78)")
        self.date7.setAlignment(QtCore.Qt.AlignCenter)
        self.date7.setObjectName("date7")

        self.day7_pic = QtWidgets.QLabel(MainWindow)
        self.day7_pic.setGeometry(QtCore.QRect(760, 210, 101, 81))
        self.day7_pic.setText("")
        self.day7_pic.setScaledContents(True)
        self.day7_pic.setObjectName("day7_pic")

        self.temperature7 = QtWidgets.QLabel(MainWindow)
        self.temperature7.setGeometry(QtCore.QRect(760, 300, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.temperature7.setFont(font)
        self.temperature7.setStyleSheet("color: rgb(255, 103, 118)")
        self.temperature7.setAlignment(QtCore.Qt.AlignCenter)
        self.temperature7.setObjectName("temperature7")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.updateForecast(data)
        self.showWidgets()

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
                    self.date_table.setItem(i+1, j, item)
            self.date_table.show()
    
    def setupUI(self, MainWindow, clientProgram):
        self.weatherdata = None
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
        self.func1_button.show()

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
        self.date_table.setColumnWidth(0, 70)
        self.date_table.setColumnWidth(1, 160)
        self.date_table.setColumnWidth(2, 120)
        self.date_table.setColumnWidth(3, 100)
        self.date_table.setColumnWidth(4, 100)
        self.date_table.setColumnWidth(5, 100)

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
    clientProgram = ClientProgram()
    ui.setupUI(MainWindow, clientProgram)
    MainWindow.show()
    sys.exit(app.exec_())