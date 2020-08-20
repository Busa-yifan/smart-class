import cv2

cap = cv2.VideoCapture(0) # 使用第5个摄像头（我的电脑插了5个摄像头）
face_cascade = cv2.CascadeClassifier('G:/test/opencvface/haarcascade_frontalface_alt2.xml') # 加载人脸特征库

while(True):
    ret, frame = cap.read() # 读取一帧的图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 转灰

    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.15, minNeighbors = 5, minSize = (5, 5)) # 检测人脸
    for(x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2) # 用矩形圈出人脸

    cv2.imshow('Face Recognition',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # 释放摄像头
cv2.destroyAllWindows()
