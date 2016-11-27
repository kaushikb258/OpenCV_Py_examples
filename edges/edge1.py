import cv2
import numpy as np

img = cv2.imread('images.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Harris corner detector
dst = cv2.cornerHarris(gray,14,5,0.04)
dst = cv2.dilate(dst,None)
img [dst > 0.01*dst.max()] = [0,0,0]
cv2.imshow('Harris Corners',img)
cv2.waitKey()


# Good features
corners = cv2.goodFeaturesToTrack(gray,7,0.05,25)
corners = np.float32(corners)

for item in corners:
  x, y = item[0]
  cv2.circle(img,(x,y),5,255,-1)

cv2.imshow('Top features',img)
cv2.waitKey()
