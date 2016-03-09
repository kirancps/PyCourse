import cv2
import numpy as np

cap=cv2.VideoCapture(1)

flag,img=cap.read()

cv2.imshow("image", img)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)


cv2.waitKey(0)
cv2.destroyAllWindows()


