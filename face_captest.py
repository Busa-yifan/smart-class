# encoding:utf-8
import urllib.request
import json
import base64
import ssl
import cv2
import CONFIG
import time
import threading


def getresult(pic1path):
    null=""

    f1 = open(pic1path, 'rb')

    pic1 = f1.read()


    img1 = base64.b64encode(pic1)

    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    context = ssl._create_unverified_context()


    params = json.dumps({ "image" : str(img1, 'utf-8') , "image_type": "BASE64" , "face_type" : "LIVE" })

    access_token = CONFIG.access_token

    request_url = request_url + "?access_token=" + access_token

    #转码
    params_2 = params.encode(encoding='UTF8')

    request = urllib.request.Request(url=request_url, data=params_2)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request,context=context)
    content = response.read()
    content = eval(content)
    #print(content)
    result = content['result']

    if(result!=""):
        #print("result:",result)
        face_list = result['face_list']
        face_num = result['face_num']
        #print("face_list:",face_list)

        location = face_list[0]
        location = location['location']
        height = location['height'];
        left = location['left'];
        top = location['top'];
        width = location['width'];

        return(height,left,top,width)
    else:
        print("检测框没检测到人")
        return(0,0,0,0)



def drawpic(imgpath):

    height, left, top, width = getresult(imgpath)
    pt1 = (round(left), round(top))
    pt2 = (round(left + width), round(top + height))
    return(pt1,pt2)



def cvwrite():
    picf = "G:/tiaozhanbei/facetest/test0.jpg"
    time_start=time.time()
    global pt1
    global pt2
    while(1):
        time_end = time.time()
        if (time_end - time_start > 0.3):
            pt1,pt2=drawpic(picf)
            time_start = time.time()



'''
if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    picf = "G:/tiaozhanbei/facetest/test0.jpg"
    #img = cv2.imread('G:/tiaozhanbei/baiduapi/test0.jpg', 1)
    time_start = time.time()
    red = (0, 0, 255)
    pt1=(0,0)
    pt2=(0,0)
    t1 = threading.Thread(target=cvwrite)
    t1.start()
    while (1):
        ret, frame = cap.read()
        cv2.rectangle(frame, pt1, pt2, red, 2)
        cv2.imshow("capture", frame)
        time_end = time.time()
        if(time_end-time_start>0.2):
            cv2.imwrite("G:/tiaozhanbei/facetest/test0.jpg", frame)
            #pt1,pt2=drawpic(picf)
            #time_start=time.time()
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
'''


