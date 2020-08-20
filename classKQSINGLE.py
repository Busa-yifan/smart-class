import faceid
import cv2
import os
import  time
from PyQt5.QtGui  import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *



def judge(pic1path,pic2path):

    score = faceid.getresult(pic1path,pic2path)
    if (score>80):
        #print('是同一个人，score:=',score)
        return 1
    else:
       #print('不是同一个人！，score:=',score)
        return 0




def Classqiandao(pic1,ui,conn):
    path = "G:/tiaozhanbei/baiduapi/checktest/"
    files = os.listdir(path)
    files_count = 0





    global i
    i = 0
    while (1):
        pic2 = "G:/tiaozhanbei/baiduapi/test"+str(i)+".jpg"
        print(pic2)
        if(judge(pic1,pic2)==0):
            i+=1
            if(i==7):#总共判断的数量，全班人数
                print("你不是本班人！")
                break
            else:
                time.sleep(0.1)
                continue
        else:

             if(i==0):name='奕帆'
             if(i==1):name="卓铭"
             if(i==2):name="云鹏"
             if(i==3):name="志立"
             if(i==4):name="锦嘉"
             if(i==5):name="琦琦"
             if(i==6):name="姚旭"
             classnum = i+1


             cursor = conn.cursor()
             sql = ("select * from student WHERE classnumber = '"+str(classnum)+"'")#这里完善后应该再加上判断班级的where
             '''
             if(classnum%7==0):
                 classj = 6
                 classi = int(classnum/7)
             else:
                 classi = int(classnum / 7)
                 classj = classnum - (classi*7) - 1
            '''
             cursor.execute(str(sql))
             data = cursor.fetchall()
             ui.label_6.setText(data[0][1])
             ui.label_7.setText(data[0][2])
             ui.label_8.setText(data[0][5])
             ui.label_9.setText(data[0][4])
             ui.label_11.setText("已成功签到")


             time.sleep(0.1)
             break
