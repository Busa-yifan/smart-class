import cv2
import facecheck
import time
import  threading
import  classKQ
import  os


def checkface():

    i = 0
    failcount = 0
    picpath="G:/tiaozhanbei/baiduapi/checktest/test"



    #cv2.imshow("capture", frame)
    time.sleep(5)
    while (1):
        print("开始检测！")
        #cv2.waitKey(0)
        time.sleep(5)
        ret, frame = cap.read()
        cv2.imwrite(picpath+str(i)+".jpg", frame)
        face_num = facecheck.fa_check((picpath+str(i)+".jpg"))
        if(face_num>0):
            print("检测成功！开始拍照")
            time.sleep(2)
            ret, frame = cap.read()
            cv2.imwrite(picpath + str(i) + ".jpg", frame)
            face_num = facecheck.fa_check((picpath + str(i) + ".jpg"))
            print("总共有",face_num,"张人脸")
            if(face_num>0):
                print("拍照成功！下一个同学！")
                time.sleep(5)
                i+=1
                continue
            else:
                print("拍照失败，重新检测")
                os.remove(picpath + str(i) + ".jpg")
                time.sleep(5)
                continue
        else:
            print("检测不到人脸，5秒后重新检测")
            os.remove(picpath + str(i) + ".jpg")
            time.sleep(5)
            failcount+=1     #failcount次检测不到人之后关闭程序
            if(failcount==2):
                print("谢谢使用！")
                print("开始考勤")
                classKQ.Classqiandao()
                break
            continue

    cap.release()
    cv2.destroyAllWindows()




def view():
    while(1):
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #cap.release()
    #cv2.destroyAllWindows()

threads = []
t1 = threading.Thread(target=view)
threads.append(t1)
t2 = threading.Thread(target=checkface)
threads.append(t2)



if __name__ == '__main__':
    cap = cv2.VideoCapture(1)
    for t in threads:
        t.setDaemon(False)
        t.start()

 #   t.join()
