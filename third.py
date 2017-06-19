# drawing in opencv

import numpy as np
import cv2

img = cv2.imread("me.jpg", cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (500,500), (255,0,0), 15)   # where, line start, line end, line color in bgr, optional line width in px
cv2.rectangle(img, (100,100), (500,500), (0,255,0), 5 )  # top left  corner of rect and bottom right corner of rect
cv2.circle(img, (250,250), 100, (0,0,255), -1)          # center , radius and if line width is -1 it means fill the closed circle 


pts = np.array([[10,10], [50,50], [100,100], [200,200], [280,300]], np.int64)
# pts = pts.reshape((-1,1,2))        
# search why reshaping is required
cv2.polylines( img,[pts]  , True, (100,100,100), 3)  # list of points then True means closed i.e first and last points will be joined 
 
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText( img," OpenCV " , (500,500), font, 5, (0,0,0), 7, cv2.LINE_AA) # [text, center, font, size(can be a decimal), color, thickness of text , searc for LINE_AA

cv2.imshow("its me",img)

cv2.waitKey(0)
cv2.destrotAllWindows()
