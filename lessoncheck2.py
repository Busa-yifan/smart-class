# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lessoncheck.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui  import *
import sys
import pymysql
import CONFIG

class Ui_Dialoglesson(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1133, 824)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(60, 150, 1021, 641))
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(126)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(105)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(60, 110, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 121, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 50, 151, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(1000, 0, 129, 129))
        self.label_3.setStyleSheet("QLabel{\n"
"background-color:black;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(1010, 120, 121, 20))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(520, 795, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        pix = QPixmap('G:/tiaozhanbei/erweima.jpg')
        self.label_3.setPixmap(pix)










    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "时间"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Dialog", "星期一"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Dialog", "星期二"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Dialog", "星期三"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Dialog", "星期四"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("Dialog", "星期五"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("Dialog", "星期六"))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("Dialog", "星期日"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Dialog", "第一二大节"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Dialog", "第三四大节"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Dialog", "第五六大节"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Dialog", "第七八大节"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Dialog", "第九十大节"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.comboBox.setItemText(0, _translate("Dialog", "第一周"))
        self.comboBox.setItemText(1, _translate("Dialog", "第二周"))
        self.comboBox.setItemText(2, _translate("Dialog", "第三周"))
        self.comboBox.setItemText(3, _translate("Dialog", "第四周"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">教室号：</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">钟海楼03021</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.label_4.setText(_translate("Dialog", "申请课室扫一扫"))
        self.pushButton.setText(_translate("Dialog", "关闭"))

        self.comboBox.currentIndexChanged.connect(self.comchange)

        conn = pymysql.connect(host=CONFIG.host, port=3306, user='root', passwd=CONFIG.hostps, db="classkq",
                               charset='utf8');
        cursor = conn.cursor()
        sql = "select * from classuse WHERE classroom = '钟海楼' AND classno = '03021' AND time = '第一周'"
        cursor.execute(sql)
        data = cursor.fetchall()
        datanum = int(len(data))
        for i in range(0, datanum):
            if (data[i][4] == "星期一"): j = 1
            if (data[i][4] == "星期二"): j = 2
            if (data[i][4] == "星期三"): j = 3
            if (data[i][4] == "星期四"): j = 4
            if (data[i][4] == "星期五"): j = 5
            if (data[i][4] == "星期六"): j = 6
            if (data[i][4] == "星期日"): j = 7
            clsi = data[i][5]
            content = (data[i][6] + "\n" + data[i][8])
            self.tableWidget.setItem(clsi, j, QTableWidgetItem(content))

    def comchange(self):
        conn = pymysql.connect(host=CONFIG.host, port=3306, user='root', passwd=CONFIG.hostps, db="classkq",
                               charset='utf8');
        for i in range(1, 6):
            for j in range(1, 8):
                self.tableWidget.setItem(i, j, QTableWidgetItem(" "))
        comindex = self.comboBox.currentText()
        cursor = conn.cursor()
        sql = "select * from classuse WHERE classroom = '钟海楼' AND classno = '03021' AND time = '" + comindex + "'"
        cursor.execute(sql)
        data = cursor.fetchall()
        datanum = int(len(data))
        for i in range(0, datanum):
            if (data[i][4] == "星期一"): j = 1
            if (data[i][4] == "星期二"): j = 2
            if (data[i][4] == "星期三"): j = 3
            if (data[i][4] == "星期四"): j = 4
            if (data[i][4] == "星期五"): j = 5
            if (data[i][4] == "星期六"): j = 6
            if (data[i][4] == "星期日"): j = 7
            clsi = data[i][5]
            content = (data[i][6] + "\n" + data[i][8])
            self.tableWidget.setItem(clsi, j, QTableWidgetItem(content))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialoglesson()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())