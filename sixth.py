# threshold the images

import cv2
import numpy as np

img1 = cv2.imread("t1.jpg")
img2 = cv2.imread("t2.jpg")

retval, threshold1 = cv2.threshold(img1,120, 255,cv2.THRESH_BINARY)
#retval, threshold2 = cv2.threshold(img2,12, 255,cv2.THRESH_BINARY)

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(gray,120, 255,cv2.THRESH_BINARY)
gauss = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115,1) # what are the last two values
retval3, otsu = cv2.threshold(gray,120, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow("org",img1)
#cv2.imshow("orgg",img2)
cv2.imshow("otsu",otsu)
cv2.imshow("thresh2",threshold2)  
cv2.imshow("gauss",gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()





