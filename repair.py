# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'repair.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui  import *
import pymysql
import CONFIG


class Ui_Dialog_repair(object):
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
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(490, 760, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(990, 770, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 70, 91, 41))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 111, 41))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 260, 111, 41))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(420, 260, 81, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(420, 170, 161, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(90, 350, 111, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 70, 171, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 170, 171, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(590, 170, 141, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 260, 171, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(500, 260, 141, 41))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(90, 400, 961, 311))
        self.textEdit.setObjectName("textEdit")

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
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.textEdit.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        pix = QPixmap('G:/tiaozhanbei/beijing4.jpg')
        self.beijing.setPixmap(pix)

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.4)
        self.label_2.setGraphicsEffect(op)
        self.label_2.setAutoFillBackground(True)

        self.pushButton.clicked.connect(self.register)
        self.pushButton_2.clicked.connect(self.cleanall)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setText(CONFIG.classroomNO)
        self.pushButton.setText(_translate("Dialog", "提交"))
        self.pushButton_2.setText(_translate("Dialog", "返回"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">教室号：</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">报修物品：</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">损坏情况：</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">数量：</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">报修物品种类：</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">详情补充：</span></p></body></html>"))



    def register(self):
        classroomNO = self.lineEdit.text()
        objectname = self.lineEdit_2.text()
        type = self.lineEdit_3.text()
        situation = self.lineEdit_5.text()
        count = self.lineEdit_6.text()
        remark = self.textEdit.toPlainText()
        conn = pymysql.connect(host=CONFIG.host, port=3306, user='root', passwd=CONFIG.hostps, db="classkq",charset='utf8');
        cursor = conn.cursor()
        sql = "INSERT INTO repair (classroomNO,objectname,type,situation,count,remark,state,time) value ('"+classroomNO+"','" + objectname + "','" + type + "','" + situation + "','" + count + "','" + remark + "','待处理',now())"
        print(sql)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行`
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()
        self.cleanall()

    def cleanall(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.textEdit.setText("")










if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog_repair()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())