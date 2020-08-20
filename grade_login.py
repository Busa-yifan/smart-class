# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grade_login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui  import *
import pymysql
import CONFIG


class Ui_Dialog_grade_login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1133, 824)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 180, 1021, 451))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(440, 310, 350, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(350, 310, 91, 41))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(350, 400, 91, 41))
        self.label_3.setObjectName("label_3")
        self.label_4= QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(800, 310, 200, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(800, 400, 200, 41))
        self.label_5.setObjectName("label_5")
        self.label_grade = QtWidgets.QLabel(Dialog)
        self.label_grade.setGeometry(QtCore.QRect(280, 20, 600, 750))
        self.label_grade.setObjectName("label_grade")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 400, 350, 41))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(500, 500, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(990, 770, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 785, 93, 28))
        self.pushButton_3.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.beijing = QtWidgets.QLabel(Dialog)
        self.beijing.setGeometry(QtCore.QRect(0, 0, 1197, 850))
        self.beijing.setText("")
        self.beijing.setObjectName("beijing")
        self.beijing.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_grade.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_3.setVisible(False)
        self.label_grade.setVisible(False)
        self.pushButton.raise_()
        self.pushButton_2.raise_()





        pix = QPixmap('G:/tiaozhanbei/beijing4.jpg')
        self.beijing.setPixmap(pix)

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.4)
        self.label_2.setGraphicsEffect(op)
        self.label_2.setAutoFillBackground(True)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setFont(QFont("Microsoft YaHei"))
        self.label.setFont(QFont("Microsoft YaHei"))
        self.label_3.setFont(QFont("Microsoft YaHei"))
        self.label_4.setFont(QFont("Microsoft YaHei"))
        self.label_5.setFont(QFont("Microsoft YaHei"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">学号：</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">密码：</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "登录"))
        self.pushButton_2.setText(_translate("Dialog", "返回"))
        self.pushButton_3.setText(_translate("Dialog", "退出"))
        self.label_grade.setText("我是成绩单")

        self.pushButton.clicked.connect(self.login)
        self.pushButton_3.clicked.connect(self.closegrade)




    def login(self):
        _translate = QtCore.QCoreApplication.translate

        number = self.lineEdit.text()
        password = self.lineEdit_2.text()

        conn = pymysql.connect(host=CONFIG.host, port=3306, user='root', passwd=CONFIG.hostps, db="classkq",
                               charset='utf8');
        cursor = conn.cursor()
        sql = "select * from student WHERE number = '"+number+"'"
        cursor.execute(sql)
        data = cursor.fetchone()
        if(data):#如果学号存在
            self.label_4.setText('')
            if(password==data[8]):
                self.showgrade()
                self.label_5.setText('')
                print('登陆成功！')
            else:
                self.label_5.setText(_translate("Dialog","<html><head/><body><p><span style=\" font-size:20px;color:red\">密码错误！</span></p></body></html>"))
                self.lineEdit_2.setText("")
        else:
            self.label_4.setText(_translate("Dialog","<html><head/><body><p><span style=\" font-size:20px;color:red\">该学号不存在！</span></p></body></html>"))



    def showgrade(self):
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.label.setVisible(False)
        self.label_4.setVisible(False)
        self.label_5.setVisible(False)
        self.lineEdit.setVisible(False)
        self.lineEdit_2.setVisible(False)
        self.pushButton.setVisible(False)
        self.pushButton_2.setVisible(False)
        pix2 = QPixmap('G:/test/grade.jpg')
        self.label_grade.setPixmap(pix2.scaled(600,800))
        self.label_grade.setVisible(True)
        self.pushButton_3.raise_()
        self.pushButton_3.setVisible(True)


    def closegrade(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.label_2.setVisible(True)
        self.label_3.setVisible(True)
        self.label.setVisible(True)
        self.label_4.setVisible(True)
        self.label_5.setVisible(True)
        self.lineEdit.setVisible(True)
        self.lineEdit_2.setVisible(True)
        self.pushButton.setVisible(True)
        self.pushButton_2.setVisible(True)
        self.label_grade.setVisible(False)
        self.pushButton_3.setVisible(False)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog_grade_login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())