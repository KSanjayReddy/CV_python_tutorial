# corner detection

import cv2
import numpy as np

img = cv2.imread("corner.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)    # search for it

corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10) # search for it (quality and minimum dist)
corners = np.int0(corners)

for  corner in corners:
	x,y = corner.ravel()
	cv2.circle(img, (x,y), 3, (0,255,0), 2)

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
