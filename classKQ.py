import faceid2
import cv2
import os
import  time


def judge(pic1path,pic2path):

    score = faceid2.getresult(pic1path,pic2path)
    if (score>80):
        #print('是同一个人，score:=',score)
        return 1
    else:
       #print('不是同一个人！，score:=',score)
        return 0




def Classqiandao():
    path = "G:/tiaozhanbei/baiduapi/checktest/"
    files = os.listdir(path)
    files_count = 0

    filename = "G:/tiaozhanbei/签到表.txt"
    fe = open(filename, 'w')
    fe.truncate()
    filetxt = open( filename,'a')
    filetxt.write("考勤签到表"+ '\n')



    for num in files:
        if os.path.isfile(os.path.join(path, num)):
            files_count += 1
    global i
    i = 0
    for j in range(0,files_count):
        while (1):
            pic2 = "G:/tiaozhanbei/baiduapi/test"+str(i)+".jpg"
            print(pic2)
            if(judge(path+files[j],pic2)==0):
                i+=1
                if(i==6):#总共判断的数量，全班人数
                    print("你不是本班的人！")
                    break
                else:
                    time.sleep(0.1)
                    continue
            else:
                if(i==0):name='琦琦'
                if(i==1):name="奕帆"
                if(i==2):name="云鹏"
                if(i==3):name="志立"
                if(i==4):name="卓铭"
                if(i==5):name="锦嘉"
                writetxt = name+"已签到。"
                print(writetxt)
                filetxt.write(writetxt + '\n')

                time.sleep(0.1)
                break
        i=0   # 重置