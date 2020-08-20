# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui  import *
import pymysql
import CONFIG
import cv2
import threading
import os
import time
import facecheck
import face_search
import math


class Ui_Dialog_check(object):
    def setupUi(self, Dialog,cap2):
        global cap
        cap = cap2
        Dialog.setObjectName("Dialog")
        Dialog.resize(1133, 824)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(990, 770, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 770, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 130, 351, 381))
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    background-color: white\n"
"}")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(620, 220, 121, 51))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(620, 350, 131, 61))
        self.label_5.setObjectName("label_5")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(140, 550, 171, 41))
        self.label_12.setObjectName("label_12")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(700, 290, 181, 41))
        self.label_8.setObjectName("label_8")
        self.teachername_label = QtWidgets.QLabel(Dialog)
        self.teachername_label.setGeometry(QtCore.QRect(660, 550, 191, 41))
        self.teachername_label.setObjectName("teachername_label")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(700, 230, 161, 31))
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(700, 160, 161, 31))
        self.label_6.setObjectName("label_6")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(100, 600, 901, 161))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(-80, 80, 51, 21))
        self.label_14.setObjectName("label_14")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(620, 410, 111, 71))
        self.label_10.setObjectName("label_10")
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(50, 110, 981, 431))
        self.label_15.setStyleSheet("QLabel\n"
"{\n"
"    border:2px solid black;background-color:white;\n"
"    \n"
"}")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(620, 150, 101, 51))
        self.label_2.setObjectName("label_2")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(570, 550, 101, 41))
        self.label_13.setObjectName("label_13")
        self.lessonname_label = QtWidgets.QLabel(Dialog)
        self.lessonname_label.setGeometry(QtCore.QRect(320, 550, 241, 41))
        self.lessonname_label.setObjectName("lessonname_label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(620, 280, 111, 61))
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(740, 360, 181, 41))
        self.label_9.setObjectName("label_9")
        self.classroom_label = QtWidgets.QLabel(Dialog)
        self.classroom_label.setGeometry(QtCore.QRect(80, 50, 231, 21))
        self.classroom_label.setObjectName("classroom_label")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(700, 420, 181, 51))
        self.label_11.setObjectName("label_11")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(20, 50, 51, 21))
        self.label_16.setObjectName("label_16")

        self.beijing = QtWidgets.QLabel(Dialog)
        self.beijing.setGeometry(QtCore.QRect(0, 0, 1197, 850))
        self.beijing.setText("")
        self.beijing.setObjectName("beijing")
        self.beijing.raise_()
        self.label_15.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_12.raise_()
        self.label_8.raise_()
        self.teachername_label.raise_()
        self.label_7.raise_()
        self.label_6.raise_()
        self.tableWidget.raise_()
        self.label_14.raise_()
        self.label_10.raise_()
        self.label_2.raise_()
        self.label_13.raise_()
        self.lessonname_label.raise_()
        self.label_4.raise_()
        self.label_9.raise_()
        self.classroom_label.raise_()
        self.label_11.raise_()
        self.label_16.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        pix = QPixmap('G:/tiaozhanbei/beijing4.jpg')
        self.beijing.setPixmap(pix)

        global conn
        conn = pymysql.connect(host=CONFIG.host, port=3306, user='root', passwd=CONFIG.hostps, db="classkq",
                               charset='utf8');
        cursor = conn.cursor()
        sql = "select * from student"
        cursor.execute(sql)
        data = cursor.fetchall()
        datanum = 0
        stunum = len(data)
        sturow = int(stunum / 7) + 1
        for i in range(0, sturow):
            for j in range(0, 7):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(data[datanum][1]))
                if (datanum == (stunum - 1)):
                    break
                else:
                    datanum += 1



        global threadscount
        threadscount = 0

        threads = []
        t1 = threading.Thread(target=self.checkface)
        threads.append(t1)
        t2 = threading.Thread(target=self.showcamera)
        threads.append(t2)
        for t in threads:
            t.setDaemon(False)
            t.start()




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "返回"))
        self.pushButton_2.setText(_translate("Dialog", "查看统计详情"))
        self.label.setText(_translate("Dialog", "                   摄像头"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">学号：</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">所属学院：</span></p></body></html>"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">现在正在签到课程的是：</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p></p></body></html>"))
        self.teachername_label.setText(_translate("Dialog", "杨福光"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\"></span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\"></span></p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">教室号：</span></p></body></html>"))
        self.label_10.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">状态：</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">姓名：</span></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">授课教师：</span></p></body></html>"))
        self.lessonname_label.setText(_translate("Dialog", "离散数学"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">专业：</span></p></body></html>"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p></p></body></html>"))
        self.classroom_label.setText(_translate("Dialog", "钟海楼03023"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p>正在初始化...</p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">教室号：</span></p></body></html>"))

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
        self.label_16.setFont(QFont("Microsoft YaHei"))
        self.label_16.setStyleSheet("color:white")


    def showcamera(self):
        face_cascade = cv2.CascadeClassifier('G:/test/opencvface/haarcascade_frontalface_alt2.xml')  # 加载人脸特征库
        while(1):
            if (cap.isOpened()&(threadscount==1)):
                # get a frame
                ret, img = cap.read()
                faces = face_cascade.detectMultiScale(img, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5))  # 检测人脸
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 用矩形圈出人脸
                height, width, bytesPerComponent = img.shape
                bytesPerLine = bytesPerComponent * width
                # 变换彩色空间顺序
                cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
                # 转为QImage对象
                self.image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.label.setPixmap(QPixmap.fromImage(self.image).scaled(self.label.width(), self.label.height()))



    def startthread(self):
        global threadscount
        threadscount = 1

    def stopthread(self):
        global threadscount
        threadscount = 0


    def checkface(self):

        # i = 0
        global failcount
        failcount = 0
        picpath = "G:/tiaozhanbei/baiduapi/checktest/test0"

        # cv2.imshow("capture", frame)
        time.sleep(5)
        while (1):
            if(threadscount==1):
                self.label_11.setText("开始检测！")
                # cv2.waitKey(0)
                time.sleep(1)
                ret, frame = cap.read()
                cv2.imwrite(picpath + ".jpg", frame)

                face_num = facecheck.fa_check((picpath + ".jpg"))

                if (face_num > 0):
                    self.label_11.setText("检测成功，开始拍照！")
                    time.sleep(2)
                    ret, frame = cap.read()
                    cv2.imwrite(picpath + ".jpg", frame)
                    face_num = facecheck.fa_check((picpath + ".jpg"))
                    print("总共有", face_num, "张人脸")
                    if (face_num > 0):
                        self.label_11.setText("拍照成功，开始核实身份！")
                        failcount = 0
                        self.Classqiandao(picpath + ".jpg")
                        print("下一个同学！")
                        time.sleep(5)
                        continue
                    else:
                        print("拍照失败，重新检测")
                        os.remove(picpath + ".jpg")
                        time.sleep(5)
                        continue
                else:
                    print("检测不到人脸，5秒后重新检测")
                    os.remove(picpath + ".jpg")
                    time.sleep(5)
                    continue


    def Classqiandao(self,pic1):
        classnum, score = face_search.getresult(pic1)
        #classnum是每个学生在班级中的座号，其中对应人脸库的user_id，每个班级一个人脸库组
        score = float(score)
        if ((classnum != 0) and (score >= 80)):
            print('classnum=',classnum)
            cursor = conn.cursor()
            sql = ("select * from student WHERE classnumber = '" + str(classnum) + "'")  # 这里完善后应该再加上判断班级的where
            cursor.execute(str(sql))
            data = cursor.fetchall()
            self.label_6.setText(data[0][1])
            self.label_7.setText(data[0][2])
            self.label_8.setText(data[0][5])
            self.label_9.setText(data[0][4])
            self.label_11.setText("已成功签到")

            #改变已签到学生的颜色
            sturow = math.floor(int(classnum) / 7)
            stucolumn = int(classnum) % 7 - 1

            self.tableWidget.item(sturow, stucolumn).setBackground(QBrush(QColor(0, 255, 0)))#绿色
        else:
            self.label_6.setText("")
            self.label_7.setText("")
            self.label_8.setText("")
            self.label_9.setText("")
            self.label_11.setText("不是本班学生")






if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog_check()
    ui.setupUi(MainWindow,cap)
    ui.startthread()
    MainWindow.show()
    sys.exit(app.exec_())