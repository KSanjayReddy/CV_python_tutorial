# feature matching

import cv2
import numpy as np  
import matplotlib.pyplot as plt

imgc = cv2.imread("complete.png",1)  # 0 means grayscale
imgf = cv2.imread("tofind.png",1)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(imgc, None)
kp2, des2 = orb.detectAndCompute(imgf, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key =lambda x:x.distance)

img3 = cv2.drawMatches(imgc, kp1,imgf, kp2, matches[:30], None, flags=2)
#plt.imshow(img3)
#plt.show()

cv2.imshow("",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
