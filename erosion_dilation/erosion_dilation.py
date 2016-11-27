import numpy as np
import cv2

img = cv2.imread('coke.jpg')

kernel = np.ones((5,5),np.uint8)

e = cv2.erode(img,kernel,iterations=1)
d = cv2.dilate(img,kernel,iterations=1)

cv2.imshow('Erosion',e)
cv2.imshow('Dilation',d)

cv2.waitKey()

