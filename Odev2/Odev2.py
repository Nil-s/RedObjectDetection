import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while camera.isOpened():
    ret, frame = camera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([0,50,50])
    upper = np.array([10,255,255])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("Orijinal", frame)
    cv2.imshow("HSV", mask)
    cv2.imshow("Kırmızı Nesne",result)

    if cv2.waitKey(1) == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()