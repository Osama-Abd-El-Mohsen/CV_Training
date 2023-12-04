import cv2

img = cv2.imread("assits/contours.jpg")
img = cv2.resize(img, (512, 512))

wb_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thres = cv2.threshold(wb_img, 20, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.imshow("img", img)
contourrs_img = cv2.drawContours(img, contours, -1, (0, 0, 255), 4)
cv2.imshow("contourrs_img", contourrs_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
