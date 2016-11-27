import cv2
import numpy as np
import math

img = cv2.imread('sally.jpg')
row, col, chan = img.shape
pi = 3.14


# vertical wave
img_out = np.zeros(img.shape,dtype=img.dtype)

for r in range(row):
 for c in range(col):
  dx = int(18.0*math.sin(2.0*pi*r/180.0))
  dy = 0
  if c+dx < col:
   img_out[r,c,:] = img[r,(c+dx)%col,:]
  else:
   img_out[r,c,:] = 0
cv2.imshow('vertical wave',img_out)
cv2.waitKey()


# horizontal wave
img_out = np.zeros(img.shape,dtype=img.dtype)

for r in range(row):
 for c in range(col):
  dx = 0
  dy = int(26.0*math.sin(2.0*pi*c/180.0))
  if r+dy < row:
   img_out[r,c,:] = img[(r+dy)%row,c,:]
  else:
   img_out[r,c,:] = 0
cv2.imshow('horizontal wave',img_out)
cv2.waitKey()



# both horizontal and vertical waves
img_out = np.zeros(img.shape,dtype=img.dtype)

for r in range(row):
 for c in range(col):
  dx = int(20.0*math.sin(2.0*pi*r/150.0))
  dy = int(20.0*math.sin(2.0*pi*c/150.0))
  if r+dy < row and c+dx < col:
   img_out[r,c,:] = img[(r+dy)%row,(c+dx)%col,:]
  else:
   img_out[r,c,:] = 0
cv2.imshow('multidir wave',img_out)
cv2.waitKey()

