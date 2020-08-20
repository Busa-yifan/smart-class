# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui  import *
import sys
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
import CONFIG

class Ui_Dialogcover(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1133, 824)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(300, 240, 550, 111))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 480, 1501, 300))
        self.label_2.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(925, 705, 200, 200))
        self.label_3.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 540, 201, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 540, 201, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 540, 201, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(860, 540, 201, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 650, 201, 71))
        self.pushButton_5.setObjectName("pushButton")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 650, 201, 71))
        self.pushButton_6.setObjectName("pushButton_2")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(610, 650, 201, 71))
        self.pushButton_7.setObjectName("pushButton_3")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(860, 650, 201, 71))
        self.pushButton_8.setObjectName("pushButton_4")

        self.beijing = QtWidgets.QLabel(Dialog)
        self.beijing.setGeometry(QtCore.QRect(0, 0, 1197, 850))
        self.beijing.setText("")
        self.beijing.setObjectName("beijing")
        self.beijing.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        pix = QPixmap('G:/tiaozhanbei/beijing4.jpg')
        self.beijing.setPixmap(pix)

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.4)
        self.label_2.setGraphicsEffect(op)
        self.label_2.setAutoFillBackground(True)

        self.pushButton.setStyleSheet(
            "QPushButton{color:black}"
            "QPushButton:hover{color:red}"
            "QPushButton{background-color:white}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:2px 4px}")

        self.pushButton_2.setStyleSheet(
            "QPushButton{color:black}"
            "QPushButton:hover{color:red}"
            "QPushButton{background-color:white}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:2px 4px}")

        self.pushButton_3.setStyleSheet(
            "QPushButton{color:black}"
            "QPushButton:hover{color:red}"
            "QPushButton{background-color:white}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:2px 4px}")

        self.pushButton_4.setStyleSheet(
            "QPushButton{color:black}"
            "QPushButton:hover{color:red}"
            "QPushButton{background-color:white}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:2px 4px}")

        self.pushButton_5.setStyleSheet(
            "QPushButton{color:black}"
            "QPushButton:hover{color:red}"
            "QPushButton{background-color:white}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:2px 4px}")

        self.pushButton_6.setStyleSheet(
            "QPushButton{color:black}"
            "QPushButton:hover{color:red}"
            "QPushButton{background-color:white}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:2px 4px}")

        self.pushButton_7.setStyleSheet(
            "QPushButton{color:black}"
            "QPushButton:hover{color:red}"
            "QPushButton{background-color:white}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:2px 4px}")

        self.pushButton_8.setStyleSheet(
            "QPushButton{color:black}"
            "QPushButton:hover{color:red}"
            "QPushButton{background-color:white}"
            "QPushButton{border:2px}"
            "QPushButton{border-radius:10px}"
            "QPushButton{padding:2px 4px}")

        self.label_2.setStyleSheet(
            "QLabel{background-color:white}"
        )


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setFont(QFont("Microsoft YaHei"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:25pt; font-weight:600;color:white;\">Smart-Class智能课室系统</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "开始考勤"))
        self.pushButton_2.setText(_translate("Dialog", "查看课室时间安排表"))
        self.pushButton_3.setText(_translate("Dialog", "查询成绩"))
        self.pushButton_4.setText(_translate("Dialog", "公告栏"))
        self.pushButton_5.setText(_translate("Dialog", "课堂报修登记"))
        self.pushButton_6.setText(_translate("Dialog", "教室电器控制"))
        self.pushButton_7.setText(_translate("Dialog", "失物招领"))
        self.pushButton_8.setText(_translate("Dialog", "帮助"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:100;color:white;\">课室号："+CONFIG.classroomNO+"</span></p></body></html>"))

        self.pushButton.setFont(QFont("Microsoft YaHei"))
        self.pushButton_2.setFont(QFont("Microsoft YaHei"))




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialogcover()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
