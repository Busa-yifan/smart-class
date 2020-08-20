import cv2
import face_captest

cap = cv2.VideoCapture(0)

while(True):
    # 获取一帧
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
    facenum = face_captest.fa_check(frame)
    print(facenum)
    if cv2.waitKey(1) == ord('q'):
        break

facenum = face_captest.fa_check(frame)
print(facenum)
