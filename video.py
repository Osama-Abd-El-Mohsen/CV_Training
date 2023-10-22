import cv2
import os,datetime
import numpy as np

cap = cv2.VideoCapture(0)
print(cap.get(3))
print(cap.get(4))

cap.set(3,3000)
cap.set(4,3000)

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    state,frame = cap.read()
    x=datetime.datetime.now()
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame,f'Time = {x}',(10,100),font,1,(0,255,0),4)
    cv2.imshow('cap',frame)

    if(cv2.waitKey(1)) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

