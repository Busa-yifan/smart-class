# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lost_detail.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui  import *
import pymysql
import CONFIG

class Ui_Dialog_lostdetail(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(1133, 824)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 1051, 701))
        self.label_2.setStyleSheet("QLabel{\n"
"background:white;;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(990, 770, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 70, 111, 41))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 140, 111, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(410, 70, 61, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 200, 111, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 270, 181, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(410, 140, 111, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(90, 350, 111, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 70, 201, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 140, 201, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(530, 140, 231, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(480, 70, 201, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 200, 571, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(260, 270, 501, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setEnabled(False)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(90, 400, 961, 311))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setEnabled(False)
        self.label_photo = QtWidgets.QLabel(Dialog)
        self.label_photo.setGeometry(QtCore.QRect(800, 60, 241, 251))
        self.label_photo.setStyleSheet("QLabel{\n"
"    background:blue;\n"
"}")
        self.label_photo.setObjectName("label_photo")

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
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_photo.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.textEdit.raise_()
        self.pushButton_2.raise_()

        pix = QPixmap('G:/tiaozhanbei/beijing4.jpg')
        self.beijing.setPixmap(pix)

        pix2 = QPixmap('G:/test/tiaozhanbeitest/test.jpg')
        self.label_photo.setPixmap(pix2.scaled(self.label_photo.width(), self.label_photo.height()))

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.4)
        self.label_2.setGraphicsEffect(op)
        self.label_2.setAutoFillBackground(True)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "返回"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">物品名字：</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">物品种类：</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">颜色：</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">拾取地点：</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">拾取人联系方式：</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">拾取时间：</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">备注补充：</span></p></body></html>"))



    def change(self,id):
        conn = pymysql.connect(host=CONFIG.host, port=3306, user='root', passwd=CONFIG.hostps, db="classkq",
                               charset='utf8');
        cursor = conn.cursor()
        sql = "select * from lost_object WHERE id = "+id
        cursor.execute(sql)
        data = cursor.fetchone()
        self.lineEdit.setText(data[1])
        self.lineEdit_2.setText(data[2])
        self.lineEdit_3.setText(data[7])
        self.lineEdit_4.setText(data[3])
        self.lineEdit_5.setText(data[4])
        self.lineEdit_6.setText(data[5])
        self.textEdit.setText(data[6])
        pix2 = QPixmap('G:/test/tiaozhanbeitest/'+data[8])
        self.label_photo.setPixmap(pix2.scaled(self.label_photo.width(), self.label_photo.height()))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog_lostdetail()
    ui.setupUi(MainWindow,2)
    MainWindow.show()
    sys.exit(app.exec_())