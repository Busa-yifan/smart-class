# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'float.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui  import *

import sys

class Ui_Dialogfloat(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1133, 824)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 100, 511, 191))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 290, 871, 161))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(420, 460, 381, 101))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.beijing = QtWidgets.QLabel(Dialog)
        self.beijing.setGeometry(QtCore.QRect(0, 0, 1197, 850))
        self.beijing.setText("")
        self.beijing.setObjectName("beijing")
        self.beijing.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()

        pix = QPixmap('G:/tiaozhanbei/beijing4.jpg')
        self.beijing.setPixmap(pix)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">现在正在进行的是：</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">毛泽东思想和中国特色社会主义理论体系概论</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">软件工程1164</span></p></body></html>"))
        self.label.setFont(QFont("Microsoft YaHei"))
        self.label.setStyleSheet("color:white")
        self.label_2.setFont(QFont("Microsoft YaHei"))
        self.label_2.setStyleSheet("color:white")
        self.label_3.setFont(QFont("Microsoft YaHei"))
        self.label_3.setStyleSheet("color:white")




if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialogfloat()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())