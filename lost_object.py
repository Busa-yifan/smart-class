# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lost_object.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui  import *
from lost_write import Ui_Dialog_lostwrite
from lost_search import  Ui_Dialog_lostsearch
from lost_detail import  Ui_Dialog_lostdetail
import cv2

class Ui_DialogLost(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1133, 824)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 280, 800, 250))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 330, 241, 141))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font-size:30px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(650, 330, 241, 141))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    font-size:30px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(990, 760, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.beijing = QtWidgets.QLabel(Dialog)
        self.beijing.setGeometry(QtCore.QRect(0, 0, 1197, 850))
        self.beijing.setText("")
        self.beijing.setObjectName("beijing")
        self.beijing.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()



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
        self.pushButton_2.setFont(QFont("Microsoft YaHei"))
        self.pushButton_3.setFont(QFont("Microsoft YaHei"))
        self.label_2.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "失物招领"))
        self.pushButton_2.setText(_translate("Dialog", "失物登记"))
        self.pushButton_3.setText(_translate("Dialog", "返回"))



class lostwrite_form(QWidget, Ui_Dialog_lostwrite):
    def __init__(self):
        super().__init__()
        self.setupUi(self,cap1)
    def show_grade(self):
        self.show()
    def hide_grade(self):
        self.hide()
    def close_grade(self):
        self.close()


class lostsearch_form(QWidget, Ui_Dialog_lostsearch):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def show_grade(self):
        self.show()
    def hide_grade(self):
        self.hide()
    def close_grade(self):
        self.close()




if __name__ == '__main__':
    cap1 = cv2.VideoCapture(0)
    app = QtWidgets.QApplication(sys.argv)

    w1_lostwrite = lostwrite_form()
    w2_lostsearch = lostsearch_form()

    MainWindow = QtWidgets.QDialog()
    ui = Ui_DialogLost()
    ui.setupUi(MainWindow)

    ui.pushButton.clicked.connect(w2_lostsearch.show)
    ui.pushButton.clicked.connect(MainWindow.hide)
    ui.pushButton_2.clicked.connect(w1_lostwrite.show)
    ui.pushButton_2.clicked.connect(MainWindow.hide)
    w1_lostwrite.pushButton_2.clicked.connect(MainWindow.show)
    w1_lostwrite.pushButton_2.clicked.connect(w1_lostwrite.close)
    w2_lostsearch.pushButton_2.clicked.connect(MainWindow.show)
    w2_lostsearch.pushButton_2.clicked.connect(w2_lostsearch.close)

    MainWindow.show()
    sys.exit(app.exec_())