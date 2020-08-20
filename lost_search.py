# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lost_search.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *
from lost_detail import Ui_Dialog_lostdetail
import sys
import pymysql
import CONFIG

class Ui_Dialog_lostsearch(object):
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
        self.pushButton.setGeometry(QtCore.QRect(480, 190, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(990, 770, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 70, 111, 41))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(420, 70, 111, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(790, 70, 61, 41))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 130, 111, 41))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(570, 130, 111, 41))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 70, 201, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(540, 70, 201, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(680, 130, 381, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(860, 70, 201, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(190, 130, 311, 41))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(70, 280, 991, 435))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(161)

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
        self.label_7.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.tableWidget.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()

        pix = QPixmap('G:/tiaozhanbei/beijing4.jpg')
        self.beijing.setPixmap(pix)

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.4)
        self.label_2.setGraphicsEffect(op)
        self.label_2.setAutoFillBackground(True)

        self.pushButton.clicked.connect(self.search_data)

        global w1_detail
        w1_detail = lostdetail_form()
        w1_detail.pushButton_2.clicked.connect(w1_detail.hide)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "查找"))
        self.pushButton_2.setText(_translate("Dialog", "返回"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">物品名字：</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">物品种类：</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">颜色：</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">拾取地点：</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">拾取时间：</span></p></body></html>"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "物品名字"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Dialog", "物品种类"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Dialog", "颜色"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Dialog", "拾取地点"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Dialog", "拾取时间"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("Dialog", "操作"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)




    def buttonForRow(self, id):#添加按钮类
        widget = QWidget()
        detailBtn = QPushButton('查看详情')
        detailBtn.setStyleSheet(''' text-align : center;
                                               background-color : DarkSeaGreen;
                                               height : 30px;
                                               border-style: outset;
                                             font : 13px  ''')
        detailBtn.clicked.connect(lambda: self.opendetail(id))
        hLayout = QHBoxLayout()
        hLayout.addWidget(detailBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget



    def search_data(self):

        #清空表格
        row_count = self.tableWidget.rowCount()
        for row in range(row_count,1,-1):
            self.tableWidget.removeRow(row-1)


        conn = pymysql.connect(host=CONFIG.host, port=3306, user='root', passwd=CONFIG.hostps, db="classkq",
                               charset='utf8');
        cursor = conn.cursor()

        namesql = self.lineEdit.text()
        typesql = self.lineEdit_2.text()
        colorsql = self.lineEdit_4.text()
        placesql = self.lineEdit_5.text()
        timesql = self.lineEdit_3.text()

        sql = "select * from lost_object WHERE (objectname like '%"+namesql+"%' and type like '%"+typesql+"%' and color like '%"+colorsql+"%' and place like '%"+placesql+"%' and time like '%"+timesql+"%')"
        cursor.execute(sql)
        rsdata = cursor.fetchall()
        row_number = int(len(rsdata))
        for i in range(0, row_number):
            self.tableWidget.insertRow(i+1)
            self.tableWidget.setItem(i+1, 0, QtWidgets.QTableWidgetItem(str(rsdata[i][1])))
            self.tableWidget.setItem(i + 1, 1, QtWidgets.QTableWidgetItem(str(rsdata[i][2])))
            self.tableWidget.setItem(i + 1, 2, QtWidgets.QTableWidgetItem(str(rsdata[i][3])))
            self.tableWidget.setItem(i + 1, 3, QtWidgets.QTableWidgetItem(str(rsdata[i][4])))
            self.tableWidget.setItem(i + 1, 4, QtWidgets.QTableWidgetItem(str(rsdata[i][7])))
            # 添加按钮
            # 传入当前id
            self.tableWidget.setCellWidget(i+1, 5, self.buttonForRow(str(rsdata[i][0])))


    def opendetail(self,id):
        w1_detail.change(id)
        w1_detail.show()






class lostdetail_form(QWidget, Ui_Dialog_lostdetail):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

