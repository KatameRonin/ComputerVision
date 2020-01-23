import cv2
#import pyopencv as cv
import numpy as np

#read image
src=cv2.imread("lion.jpg")

#apply gaussian blur
dst=cv2.GaussianBlur(src,(5,5),cv2.BORDER_DEFAULT)

#display
cv2.imshow("Gaussian Blur",np.hstack((src,dst)))
#cv.imwrite("Gaussian
cv2.waitKey(0)
cv2.destroyAllWindows()
