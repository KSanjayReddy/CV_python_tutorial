#color filtering , different types of blur

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_,  frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)       # frame is converted to hsv
	
	# HSV =  hue sat val,  hue mainly decides the color
	lower_org = np.array([3,160,60])       # lower hsv values
	upper_org = np.array([20,200,200])  # upper hsv values 
	
#	cv2.circle(frame,(100,100),20, (0,0,0), 2)
#	print(val[2])

	mask = cv2.inRange(hsv, lower_org, upper_org) # mask is 1 or high where the hsv values of pixels lie in the range provided
	res = cv2.bitwise_and(frame, frame, mask = mask)  # search what are the parameters
	
	kernel = np.ones((15,15), np.float32)/225
	smoothed = cv2.filter2D(res,-1,kernel)  # search about it       
	blur = cv2.GaussianBlur( res, (15,15), 0)    # search for it	 
	median = cv2.medianBlur(res, 15)	
	bilateral = cv2.bilateralFilter(res,15,75,75)

	cv2.imshow("frame", frame)
	cv2.imshow("GAUSSIAN", blur)
	cv2.imshow("smooth",  smoothed)
	cv2.imshow("median",  median)
	cv2.imshow("bilateral", bilateral)



	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
