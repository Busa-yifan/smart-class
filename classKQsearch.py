import face_search
import cv2
import os
import  time
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
def Classqiandao(pic1,ui,conn):

    classnum,score = face_search.getresult(pic1)
    score = float(score)
    if((classnum!=0) and (score>=80)):
        cursor = conn.cursor()
        sql = ("select * from student WHERE classnumber = '"+str(classnum)+"'")#这里完善后应该再加上判断班级的where
        cursor.execute(str(sql))
        data = cursor.fetchall()
        ui.label_6.setText(data[0][1])
        ui.label_7.setText(data[0][2])
        ui.label_8.setText(data[0][5])
        ui.label_9.setText(data[0][4])
        ui.label_11.setText("已成功签到")
    else:
        ui.label_6.setText("")
        ui.label_7.setText("")
        ui.label_8.setText("")
        ui.label_9.setText("")
        ui.label_11.setText("不是本班学生")



