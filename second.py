#interfacing webcam

import cv2
import numpy as np

cap = cv2.VideoCapture(1)
# 0 for first webcam and 1 for second webcam


# to save the video stream
fourcc = cv2.VideoWriter_fourcc(*"XVID")    # wtf is  this
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))


while True:
	ret, frame = cap.read()              # either True or False is stored in ret which ca be used to verify the webcam feed
	cv2.imshow("camera feed", frame)     # syntax of imshow is ("Window name", image variable)
	out.write(frame)
	gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)   # converting color bgr(not rgb)  to gray
	cv2.imshow("gray feed",gray)	

	if cv2.waitKey(1) & 0xFF == ord("q"):    #  search what is waitKey(1)   and other is to check if qq is pressed or not
		break

cap.release()
out.release()
cv2.destroyAllWindows()
