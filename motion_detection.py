import cv2

cap = cv2.VideoCapture("assits/motion_detection.mp4")

while 1:

    _, frame1 = cap.read()
    _, frame2 = cap.read()
    frame1 = cv2.resize(frame1, (600, 500))
    frame2 = cv2.resize(frame2, (600, 500))
    cv2.waitKey(20)

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, threth = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
    dilate = cv2.dilate(threth, None, iterations=25)
    contours, _ = cv2.findContours(
        dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contours in contours:
        (x, y, w, h) = cv2.boundingRect(contours)

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 4)

    cv2.imshow("Filter", dilate)
    cv2.imshow("Output", frame1)

    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
cap.release()
