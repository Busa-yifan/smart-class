import cv2
import facecheck
import time
import  threading
#import  classKQSINGLE
import classKQsearch
import  os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QFont, QPixmap, QPainter, QImage
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui  import *


def checkface(capc,ui,conn):

    #i = 0
    global  failcount
    failcount = 0
    picpath="G:/tiaozhanbei/baiduapi/checktest/test0"

    #cv2.imshow("capture", frame)
    time.sleep(5)
    while (1):

        ui.label_11.setText("开始检测！")
        #cv2.waitKey(0)
        time.sleep(1)
        ret, frame = capc.read()
        cv2.imwrite(picpath+".jpg", frame)

        face_num = facecheck.fa_check((picpath+".jpg"))


        if(face_num>0):
            ui.label_11.setText("检测成功，开始拍照！")
            time.sleep(2)
            ret, frame = capc.read()
            cv2.imwrite(picpath + ".jpg", frame)
            face_num = facecheck.fa_check((picpath +  ".jpg"))
            print("总共有",face_num,"张人脸")
            if(face_num>0):
                ui.label_11.setText("拍照成功，开始核实身份！")
                failcount = 0
                classKQsearch.Classqiandao(picpath +  ".jpg",ui,conn)
                print("下一个同学！")
                time.sleep(5)
                continue
            else:
                print("拍照失败，重新检测")
                os.remove(picpath + ".jpg")
                time.sleep(5)
                continue
        else:
            print("检测不到人脸，5秒后重新检测")
            os.remove(picpath + ".jpg")
            time.sleep(5)
            continue
    #capc.release()
    #cv2.destroyAllWindows()




'''
def view(capv):
    while(1):
        ret, frame = capv.read()
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #cap.release()
    #cv2.destroyAllWindows()

'''
'''
def classmain(cap):

    threads = []
    t1 = threading.Thread(target=view, args=cap)
    threads.append(t1)
    t2 = threading.Thread(target=checkface,args=cap)
    threads.append(t2)

    
    cap = cv2.VideoCapture(0)

    for t in threads:
        t.setDaemon(False)
        t.start()

    '''
