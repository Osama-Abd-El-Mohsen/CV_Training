import cv2
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()
    cvt_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hight, width, _ = frame.shape
    cx = int(width / 2)
    cy = int(hight / 2)

    HSV_center_point_colors = cvt_frame[cy, cx]
    BGR_center_point_colors = frame[cy, cx]
    b, g, r = int(BGR_center_point_colors[0]), int(
        BGR_center_point_colors[1]), int(BGR_center_point_colors[2])

    color = "undefined".upper()
    if HSV_center_point_colors[0] < 5:
        color = "red".upper()
    elif HSV_center_point_colors[0] < 22:
        color = "orange".upper()
    elif HSV_center_point_colors[0] < 50:
        color = "yellow".upper()
    elif HSV_center_point_colors[0] < 78:
        color = "green".upper()
    elif HSV_center_point_colors[0] < 131:
        color = "blue".upper()
    elif HSV_center_point_colors[0] < 170:
        color = "violet".upper()
    elif HSV_center_point_colors[0] < 255:
        color = "pink".upper()
    elif HSV_center_point_colors[0] < 200:
        color = "baby blue".upper()
    # Add more color conditions as needed.

    cv2.rectangle(frame, (cx-200, 10), (cx+200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx-200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()
