# basic image operations
# need a good logo and try again


import cv2
import numpy as np

#read two same size image
img1 = cv2.imread("a.jpg")
img2 = cv2.imread("logo.png")

#add1 = img1+img2
#add2 = cv2.add(img1,img2)  # these two basically add every pixel and the values aboves 255 are treated as 255... not so useful
#weighted = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)  # what is the last parameter
#cv2.imshow("addition", weighted)

rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]

print(rows,cols,channels)   # rows and cols are height and width and channels = 3 for bgr image
# roi is the new image which contains only the specified area

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # image2 is converted to gray
ret, mask = cv2.threshold(img2gray, 90, 255, cv2.THRESH_BINARY_INV)  # by thresholding all the pixels above 90 are converted to 255 then the image is inverted,   so a binary logo is obtained

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi, mask = mask_inv)   # search for bitwise operators
#test = cv2.bitwise_and(roi,roi, mask = mask)
img2_fg = cv2.bitwise_and(img2,img2, mask=mask)

net = cv2.add(img1_bg, img2_fg)
img1[0:rows,0:cols] = net

cv2.imshow("img1",img1)
cv2.imshow("net",net)
#cv2.imshow("inv mask",mask_inv)
#cv2.imshow("img1_bg", img1_bg)
#cv2.imshow("img2_fg", img2_fg)

cv2.waitKey(0)
cv2.destroyAllWindows()

