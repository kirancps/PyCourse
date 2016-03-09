import cv2
import numpy as np
def nothing(x):
    pass

cap=cv2.VideoCapture(0)
cv2.namedWindow('image')
cv2.createTrackbar('hMax','image',0,255,nothing)
cv2.createTrackbar('hMin','image',0,255,nothing)
cv2.createTrackbar('sMax','image',0,255,nothing)
cv2.createTrackbar('sMin','image',0,255,nothing)
cv2.createTrackbar('vMin','image',0,255,nothing)
cv2.createTrackbar('vMax','image',0,255,nothing)


while (cv2.waitKey(1)!=27):
	
	frame,image=cap.read()
	hMax = cv2.getTrackbarPos('hMax','image')
   	hMin = cv2.getTrackbarPos('hMin','image')
    	sMax = cv2.getTrackbarPos('sMax','image')
	sMin = cv2.getTrackbarPos('sMin','image')
   	vMin = cv2.getTrackbarPos('vMin','image')
    	vMax = cv2.getTrackbarPos('vMax','image')
	


	imgHSV=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
	
	lowerVal=np.array([0,138,107])
	highVal=np.array([12,255,255])
	#imgThreshLow = cv2.inRange(imgHSV, np.array([0, 135, 135]), np.array([19, 255, 255]))
        #imgThreshHigh = cv2.inRange(imgHSV, np.array([hMin,sMin,vMin]), np.array([hMax,sMax,vMax]))
 	#imgThresh = cv2.add(imgThreshLow, imgThreshHigh)
	
	imgThresh=cv2.inRange(imgHSV,lowerVal,highVal)

	#imgThresh = cv2.GaussianBlur(imgThresh, (3, 3), 2)

        imgThresh = cv2.dilate(imgThresh, np.ones((5,5),np.uint8))
        imgThresh = cv2.erode(imgThresh, np.ones((5,5),np.uint8))
	

	intRows, intColumns = imgThresh.shape
	#contours,hierarchy = cv2.findContours(imgThresh, 1, 2)
     
   	#cnt = contours[0]
	M = cv2.moments(imgThresh,0)
	#area = cv2.contourArea(cnt)
	print (M['m00'])


        circles = cv2.HoughCircles(imgThresh, cv2.HOUGH_GRADIENT, 5, intRows / 4)  
	if circles is not None:                     # this line is necessary to keep program from crashing on next line if no circles were found
            for circle in circles[0]:                           # for each circle
                x, y, radius = circle                                                                       # break out x, y, and radius
               # print "ball position x = " + str(x) + ", y = " + str(y) + ", radius = " + str(radius)       # print ball position and radius
                cv2.circle(image, (x, y), 3, (0, 255, 0), -1)           # draw small green circle at center of detected object
                cv2.circle(image, (x, y), radius, (0, 0, 255), 3)     
	
	
	
	
	
	cv2.imshow("frame", image)
	cv2.imshow("hsv", imgHSV)
	cv2.imshow("filt",imgThresh)

cv2.destroyAllWindows()

	
