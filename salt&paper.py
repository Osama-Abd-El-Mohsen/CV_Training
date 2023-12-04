import cv2

img = cv2.imread("assits/noisyimg.png")
img_enhance=cv2.medianBlur(img,5)
cv2.imshow("before",img)
cv2.imshow("after",img_enhance)

cv2.waitKey(0)
cv2.destroyAllWindows()
