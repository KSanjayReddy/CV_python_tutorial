# foreground extraction

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("fore.jpg")
mask = np.zeros( img.shape[:2], np.uint8)      # search about shape operator

bgdModel = np.zeros( (1,65), np.float64)
fgdModel = np.zeros( (1,65), np.float64)

rect = (64,64, 550,550)

cv2.grabCut( img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where( (mask==2) | (mask==0), 0,1).astype("uint8")
img = img * mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
