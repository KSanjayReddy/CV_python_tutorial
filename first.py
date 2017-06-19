import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("me.jpg",cv2.IMREAD_GRAYSCALE)

# default is unchanged
# other parameters available are
# IMREAD_COLOR        =  1
#IMREAD_UNCHANGED     =  -1
#IMREAD_GRAYSCALE     =  0


# showing image using cv

#cv2.imshow("ITS ME",img)
#cv2.waitKey(0)      #waits untill any key is pressed
#cv2.destroyAllWindows()    # to destroy all the windows

# showing image using matplotlib

plt.imshow(img, cmap="gray", interpolation= "bicubic")  # search what is  interpolation
plt.plot(  [0,0], [1000,1000], "c", linewidth=5)

plt.show()

# save a image

cv2.imwrite("saved.jpg",img)
