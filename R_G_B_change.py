import cv2
import numpy


def nothing(x):
    print(x)


img = numpy.zeros((512, 512, 3), numpy.uint8)

cv2.namedWindow('controls')
cv2.createTrackbar('R', 'controls', 0, 255, nothing)
cv2.createTrackbar('G', 'controls', 0, 255, nothing)
cv2.createTrackbar('B', 'controls', 0, 255, nothing)
cv2.createTrackbar('switch', 'controls', 0, 1, nothing)
cv2.setTrackbarPos("switch","controls",1)
while (1):

    key = cv2.waitKey(1)
    if key == 27:
        break

    cv2.imshow('controls', img)
    r = cv2.getTrackbarPos('R', 'controls')
    g = cv2.getTrackbarPos('G', 'controls')
    b = cv2.getTrackbarPos('B', 'controls')
    s = cv2.getTrackbarPos("switch", 'controls')

    if s == 1:
        img[:] = [r, g, b]
    elif s == 0:
        img[:] = 0


cv2.destroyAllWindows()
