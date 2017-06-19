# morhological, erosion and dilation

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
        _,  frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)       # frame is converted to hsv

        # HSV =  hue sat val,  hue mainly decides the color
        lower_org = np.array([3,160,60])       # lower hsv values
        upper_org = np.array([20,200,200])  # upper hsv values 

#       cv2.circle(frame,(100,100),20, (0,0,0), 2)
#       print(val[2])

        mask = cv2.inRange(hsv, lower_org, upper_org) # mask is 1 or high where the hsv values of pixels lie in the range provided
        res = cv2.bitwise_and(frame, frame, mask = mask)  # search what are the parameters
	
	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask, kernel, iterations =1)
	dilation = cv2.dilate(mask, kernel, iterations =1)
	

        cv2.imshow("frame", frame)
        cv2.imshow("result", res)
	cv2.imshow("erosion", erosion)
	cv2.imshow("dilation", dialtion)


        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cv2.destroyAllWindows()

