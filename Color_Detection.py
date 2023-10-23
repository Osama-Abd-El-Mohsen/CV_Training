import cv2
import numpy as np

def nothing(x):
    print(x)

cv2.namedWindow("Trackers")
cv2.createTrackbar("LH","Trackers",0,255,nothing)
cv2.createTrackbar("LS","Trackers",0,255,nothing)
cv2.createTrackbar("LV","Trackers",0,255,nothing)

cv2.createTrackbar("UH","Trackers",0,255,nothing)
cv2.createTrackbar("US","Trackers",0,255,nothing)
cv2.createTrackbar("UV","Trackers",0,255,nothing)







cap = cv2.VideoCapture(0)
while 1 :
    _,frame = cap.read()
    # img = cv2.imread("balls2.jpg")
    # img = cv2.resize(img,(700,500))
    img_conv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("LH",'Trackers')
    ls = cv2.getTrackbarPos("LS",'Trackers')
    lv = cv2.getTrackbarPos("LV",'Trackers')

    uh = cv2.getTrackbarPos("UH",'Trackers')
    us = cv2.getTrackbarPos("US",'Trackers')
    uv = cv2.getTrackbarPos("UV",'Trackers')

    l = np.array([lh,ls,lv])
    u = np.array([uh,us,uv])

    mask = cv2.inRange(img_conv,l,u)

    colored_mask = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("mask",mask)
    cv2.imshow("Trackers",frame)
    cv2.imshow("colored_mask",colored_mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()