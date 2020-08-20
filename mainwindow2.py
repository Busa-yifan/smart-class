# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui  import *
import CONFIG
import sys
import cv2
import classCheck2
import pymysql
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1133, 824)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 90, 351, 381))
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: white\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(610, 100, 101, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 170, 121, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(610, 230, 111, 61))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(610, 300, 131, 61))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(690, 110, 161, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(690, 180, 161, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(690, 240, 181, 41))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(730, 310, 181, 41))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(610, 360, 111, 71))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(690, 370, 181, 51))
        self.label_11.setObjectName("label_11")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(50, 30, 51, 21))
        self.label_14.setObjectName("label_14")
        self.classroom_label = QtWidgets.QLabel(self.centralwidget)
        self.classroom_label.setGeometry(QtCore.QRect(110, 30, 231, 21))
        self.classroom_label.setObjectName("classroom_label")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(130, 500, 171, 41))
        self.label_12.setObjectName("label_12")
        self.lessonname_label = QtWidgets.QLabel(self.centralwidget)
        self.lessonname_label.setGeometry(QtCore.QRect(310, 500, 241, 41))
        self.lessonname_label.setObjectName("lessonname_label")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(560, 500, 101, 41))
        self.label_13.setObjectName("label_13")
        self.teachername_label = QtWidgets.QLabel(self.centralwidget)
        self.teachername_label.setGeometry(QtCore.QRect(650, 500, 191, 41))
        self.teachername_label.setObjectName("teachername_label")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(40, 60, 981, 431))
        self.label_15.setStyleSheet("QLabel\n"
"{\n"
"    border:2px solid black;background-color:white;\n"
"    \n"
"}")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 740, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 550, 901, 161))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)



        self.beijing = QtWidgets.QLabel(self.centralwidget)
        self.beijing.setGeometry(QtCore.QRect(0, 0, 1197, 900))
        self.beijing.setText("")
        self.beijing.setObjectName("beijing")




        self.label_15.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_14.raise_()
        self.classroom_label.raise_()
        self.label_12.raise_()
        self.lessonname_label.raise_()
        self.label_13.raise_()
        self.teachername_label.raise_()
        self.pushButton.raise_()
        self.tableWidget.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        pix = QPixmap('G:/tiaozhanbei/beijing4.jpg')
        self.beijing.setPixmap(pix)

        conn = pymysql.connect(host=CONFIG.host, port=3306, user='root', passwd=CONFIG.hostps, db="classkq", charset='utf8');
        cursor = conn.cursor()
        sql = "select * from student WHERE major = '软件工程' AND majorclass = '1164'"
        cursor.execute(sql)
        data = cursor.fetchall()
        datanum = 0
        stunum = len(data)
        sturow = int(stunum / 7) + 1
        for i in range(0, sturow):
            for j in range(0, 7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(data[datanum][1]))
                if (datanum == (stunum - 1)):
                    break
                else:
                    datanum += 1






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "               正在初始化摄像头"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">姓名：</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">学号：</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">专业：</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">所属学院：</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\"></span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\"></span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">状态：</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>正在初始化...</p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">教室号：</span></p></body></html>"))
        self.classroom_label.setText(_translate("MainWindow", "钟海楼03023"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">现在正在签到课程的是：</span></p></body></html>"))
        self.lessonname_label.setText(_translate("MainWindow", "离散数学"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">授课教师：</span></p></body></html>"))
        self.teachername_label.setText(_translate("MainWindow", "杨福光"))
        self.pushButton.setText(_translate("MainWindow", "查看统计详情"))

        self.teachername_label.setFont(QFont("Microsoft YaHei"))
        self.teachername_label.setStyleSheet("color:white")
        self.classroom_label.setFont(QFont("Microsoft YaHei"))
        self.classroom_label.setStyleSheet("color:white")
        self.lessonname_label.setFont(QFont("Microsoft YaHei"))
        self.lessonname_label.setStyleSheet("color:white")
        self.label_12.setFont(QFont("Microsoft YaHei"))
        self.label_12.setStyleSheet("color:white")
        self.label_14.setFont(QFont("Microsoft YaHei"))
        self.label_14.setStyleSheet("color:white")
        self.label_13.setFont(QFont("Microsoft YaHei"))
        self.label_13.setStyleSheet("color:white")


    def changeitem(self):
        print("我进来啦啦啦啦")
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("aaa"))





def showcamera(cap,ui):
    while(1):
        if (cap.isOpened()):
            # get a frame
            ret, img = cap.read()
            height, width, bytesPerComponent = img.shape
            bytesPerLine = bytesPerComponent * width
            # 变换彩色空间顺序
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
            # 转为QImage对象
            ui.image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            ui.label.setPixmap(QPixmap.fromImage(ui.image).scaled(ui.label.width(), ui.label.height()))






def showKQwindows(app):

    #app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='feng', db="classkq", charset='utf8');
    cursor = conn.cursor()
    sql = "select * from student WHERE major = '软件工程' AND majorclass = '1164'"
    cursor.execute(sql)
    data = cursor.fetchall()
    datanum = 0
    stunum = len(data)
    sturow = int(stunum / 7) + 1
    for i in range(0, sturow):
        for j in range(0, 7):
            ui.tableWidget.setItem(i, j, QTableWidgetItem(data[datanum][1]))
            if (datanum == (stunum - 1)):
                break
            else:
                datanum += 1

    MainWindow.show()
    cap = cv2.VideoCapture(0)

    threads = []
    t1 = threading.Thread(target=classCheck2.checkface, args=(cap, ui, conn))
    threads.append(t1)
    t2 = threading.Thread(target=showcamera,args=(cap, ui))
    threads.append(t2)

    for t in threads:
        t.setDaemon(False)
        t.start()


    #sys.exit(app.exec_())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())