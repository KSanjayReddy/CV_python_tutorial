# basic image operarion

import cv2
import numpy as np

img = cv2.imread("a.jpg", cv2.IMREAD_COLOR)

img[100,100] = [255,255,255]
px = img[100,100]
#print (px)

roi = img[100:150,100:150]
img[100:150,100:150] = [255,0,0]

img[0:50,0:50] = roi

cv2.imshow("image",img)
#cv2.imshow("image",roi)         roi is a matrix not an image
cv2.waitKey(0)
cv2.destroyAllWindows()
