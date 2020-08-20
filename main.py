import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import mainwindow2
from mainwindow2 import Ui_MainWindow
from cover import Ui_Dialogcover
from lessoncheck import Ui_Dialoglesson
from grade_login import Ui_Dialog_grade_login
from lost_object import  Ui_DialogLost
from lost_search import  Ui_Dialog_lostsearch
from lost_write import Ui_Dialog_lostwrite
from repair import Ui_Dialog_repair
from check import  Ui_Dialog_check
import cv2
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import classCheck2
import time
import inspect
import ctypes
import CONFIG
import face_captest
from float import Ui_Dialogfloat


#封面界面
class coverform(QWidget, Ui_Dialogcover):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def kqshow(self):  # 点击按钮将窗体1关掉
        w9_check.show()
        w9_check.startthread()
        self.close()
    def lessonshow(self):
        self.close()
        w3_lesson.show()
    def gradeshow(self):
        self.close()
        w4_grade.show()
    def lostshow(self):
        self.close()
        w5_lost.show()
    def show_w1(self):
        self.show()
    def repair_show(self):
        self.close()
        w8_repair.show()


class checkform(QWidget, Ui_Dialog_check):
    def __init__(self):
        super().__init__()
        self.setupUi(self,cap)
    def show_check(self):
        self.show()
    def hide_check(self):
        self.hide()
    def close_check(self):
        self.stopthread()
        self.close()
        w1_cover.show()


#滚动屏幕界面
class floatform(QWidget, Ui_Dialogfloat):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def mousePressEvent(self, e):
        self.hide()
        w1_cover.show()
        tcover = threading.Thread(target=showfloat)
        tcover.start()
    def show_float(self):
        self.show()
    def hide_float(self):
        self.hide()


#课表查询界面
class lessonform(QWidget, Ui_Dialoglesson):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def show_lesson(self):
        self.show()
    def hide_lesson(self):
        self.hide()
    def close_losson(self):
        self.close()
        w1_cover.show()

#成绩查询界面
class gradeform(QWidget, Ui_Dialog_grade_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def show_grade(self):
        self.show()
    def hide_grade(self):
        self.hide()
    def close_grade(self):
        self.close()
        w1_cover.show()

#失物招领菜单界面
class lostform(QWidget, Ui_DialogLost):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def show_lost(self):
        self.show()
    def hide_lost(self):
        self.hide()
    def close_lost(self):
        self.close()
        w1_cover.show()
    def show_lost_write(self):
        w7_lostwrite.show()
        w7_lostwrite.remake()

#失物登记界面
class lostwrite_form(QWidget, Ui_Dialog_lostwrite):
    def __init__(self):
        super().__init__()
        self.setupUi(self,cap)
    def lostwrite_close(self):
        self.stopthread()
        self.close()
        w5_lost.show()


#失物招领查询界面
class lostsearch_form(QWidget, Ui_Dialog_lostsearch):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class repairform(QWidget, Ui_Dialog_repair):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def show_repair(self):
        self.show()
    def hide_repair(self):
        self.hide()
    def close_repair(self):
        self.close()
        w1_cover.show()

'''
#视频循环类
def showcamera(cap,ui,threadshow):
    since = time.time()
    time_start = time.time()
    red = (0, 0, 255)
    global pt1
    global pt2
    pt1 = (0, 0)
    pt2 = (0, 0)
    while(1):
        if (cap.isOpened()):
            ret, img = cap.read()

            cv2.rectangle(img, pt1, pt2, red, 2)

            height, width, bytesPerComponent = img.shape
            bytesPerLine = bytesPerComponent * width
            # 变换彩色空间顺序
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
            # 转为QImage对象
            ui.image = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            ui.label.setPixmap(QPixmap.fromImage(ui.image).scaled(ui.label.width(), ui.label.height()))
            time_elapsed=time.time()-since
            time_end = time.time()

            if (time_end-time_start > 1.4):
                cv2.imwrite("G:/tiaozhanbei/facetest/test0.jpg", img)
                #pt1, pt2 = face_captest.drawpic("G:/tiaozhanbei/facetest/test0.jpg")
                time_start = time.time()


            if(time_elapsed>30):
                break

    #cap.release()
    #cv2.destroyAllWindows()
    w1_cover.show()
    MainWindow.close()
    for t in threadshow:
        stop_thread(t)




#杀线程类
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def facewrite():

    picf="G:/tiaozhanbei/facetest/test0.jpg"
    time_start=time.time()
    global pt1
    global pt2
    while(1):
        time_end = time.time()
        if (time_end - time_start > 1.6):
            pt1,pt2=face_captest.drawpic(picf)
            time_start = time.time()

#线程控制的三个方法
def thread_start():
    threads = []
    t1 = threading.Thread(target=classCheck2.checkface, args=(cap, ui, conn))
    threads.append(t1)
    t2 = threading.Thread(target=showcamera, args=(cap, ui, threads))
    threads.append(t2)
    t3 = threading.Thread(target=facewrite)
    threads.append(t3)
    for t in threads:
        t.setDaemon(False)
        t.start()

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)
def stop(threads):
    for t in threads:
        t.stop()
'''

#定时从主界面跳到大字页面
def showfloat():
    float_since = time.time()
    while(1):
        if(w1_cover.isVisible()==True):
            float_time_elapsed = time.time() - float_since
            if ((float_time_elapsed > 30)):#定时参数
                break
        else:
            float_since = time.time()
    w1_cover.hide()
    #w2_float.show()








if __name__ == '__main__':

    conn = pymysql.connect(host=CONFIG.host, port=3306, user='root', passwd=CONFIG.hostps, db="classkq", charset='utf8');
    cap = cv2.VideoCapture(CONFIG.capnum)#开启摄像头
    app = QApplication(sys.argv)#app

    #考勤窗口初始化
   # MainWindow =  QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)


    '''
    #线程初始化
    threads = []
    t1 = threading.Thread(target=classCheck2.checkface, args=(cap, ui, conn))
    threads.append(t1)
    t2 = threading.Thread(target=showcamera2, args=(cap, ui,threads))
    threads.append(t2)
    '''

    #封面窗口实例化
    w1_cover = coverform()
   # w2_float= floatform()
    w3_lesson = lessonform()
    w4_grade = gradeform()
    w5_lost = lostform()
    w6_lostsearch = lostsearch_form()
    w7_lostwrite = lostwrite_form()
    w8_repair = repairform()
    w9_check = checkform()

    w1_cover.show()

  #  tcover = threading.Thread(target=showfloat)
  #  tcover.start()



    #封面窗口按钮连接
    w1_cover.pushButton.clicked.connect(w1_cover.kqshow)
    w1_cover.pushButton.clicked.connect(w7_lostwrite.stopthread)
    w1_cover.pushButton_2.clicked.connect(w1_cover.lessonshow)
    w1_cover.pushButton_3.clicked.connect(w1_cover.gradeshow)
 #   w1_cover.pushButton_4.clicked.connect(w2_float.show)
    w1_cover.pushButton_5.clicked.connect(w8_repair.show)
    w1_cover.pushButton_7.clicked.connect(w1_cover.lostshow)

    #失物招领
    w5_lost.pushButton.clicked.connect(w6_lostsearch.show)
    w5_lost.pushButton.clicked.connect(w5_lost.hide)
    w5_lost.pushButton_2.clicked.connect(w5_lost.show_lost_write)
    w5_lost.pushButton_2.clicked.connect(w5_lost.hide)
    w5_lost.pushButton_3.clicked.connect(w5_lost.close_lost)

    w7_lostwrite.pushButton_2.clicked.connect(w7_lostwrite.lostwrite_close)
    w6_lostsearch.pushButton_2.clicked.connect(w5_lost.show)
    w6_lostsearch.pushButton_2.clicked.connect(w6_lostsearch.close)


    w3_lesson.pushButton.clicked.connect(w3_lesson.close_losson)#退出按钮
    w4_grade.pushButton_2.clicked.connect(w4_grade.close_grade)#退出按钮
    w8_repair.pushButton_2.clicked.connect(w8_repair.close_repair)#退出按钮
    w9_check.pushButton.clicked.connect(w9_check.close_check)#退出按钮


    #w1.pushButton.clicked.connect(w2.show_w2)
    #w1.pushButton.clicked.connect(w2.show_w2)
    #w2.pushButton.clicked.connect(w2.close_w2)
    #w2.pushButton.clicked.connect(w1.show_w1)
    app.exec_()