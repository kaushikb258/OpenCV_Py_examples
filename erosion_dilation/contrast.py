import cv2
import numpy as np

# Grayscale
img = cv2.imread('sally.jpg',0)
print img.shape
histeq = cv2.equalizeHist(img)
cv2.imshow('Hist Eq Grayscale',histeq)
cv2.waitKey()


# Color
img = cv2.imread('sally.jpg')
img_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
out = cv2.cvtColor(img_yuv,cv2.COLOR_YUV2BGR)
cv2.imshow('Hist Eq Color',out)
cv2.waitKey()
