import cv2
import numpy


def click_event (event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN :
        red = img[y,x,0]
        green = img[y,x,1]
        blue = img[y,x,2]
        new_window=numpy.zeros((250,250,3),numpy.uint8)
        new_window[:] = [red,green,blue]
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(new_window,f"{[red,green,blue]}",(20,50),font,1,(255,255,255),4)
        cv2.imshow("New Window",new_window)


points=[]

img=cv2.imread("octane.jpg",1)
img=cv2.resize(img,(512,512))
print(img.size)
cv2.imshow("octane",img)
cv2.setMouseCallback("octane",click_event)

cv2.waitKey(0)  
cv2.destroyAllWindows()