# template matching

import cv2
import numpy as np

img1 = cv2.imread("full.png")
img2 = cv2.imread("sample.png",0)

img1gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
w, h = img2.shape[::-1]  #search for it

res = cv2.matchTemplate(img1gray,img2, cv2.TM_CCOEFF_NORMED)
threshold = 0.75
loc = np.where( res>= threshold)

for pt in zip(*loc[::-1]):        # search for this
	cv2.circle(img1, pt, 15, (255,0,0), 1)
	print(pt)

cv2.imshow("detected", img1)
cv2.imshow("sample", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
