import cv2
import numpy


def click_event (event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(img,(x,y),10,(0,255,0),4)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img,points[-1],points[-2],(0,255,255),4)

        cv2.imshow("octane",img)
    elif event == cv2.EVENT_RBUTTONDOWN :
        points.clear()
        cv2.imshow("octane",img)


points=[]
img=numpy.zeros((512,512,3),numpy.uint8)
# img=cv2.imread("octane.jpg",1)
cv2.imshow("octane",img)
cv2.setMouseCallback("octane",click_event)

cv2.waitKey(0)  
cv2.destroyAllWindows()