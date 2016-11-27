import cv2
import numpy as np

img = cv2.imread('sally.jpg')
row, col, chan = img.shape

# Gaussian kernels

# center
kernel_x = cv2.getGaussianKernel(col,250)
kernel_y = cv2.getGaussianKernel(row,250)
kernel = kernel_y*kernel_x.T
mask = 255*kernel/np.linalg.norm(kernel)

out = np.copy(img)

for i in range(chan):
  out[:,:,i] = out[:,:,i]*mask

cv2.imshow('Vignette',out)

cv2.waitKey()  

# off-center
kernel_x = cv2.getGaussianKernel(int(1.5*col),250)
kernel_y = cv2.getGaussianKernel(int(1.5*row),250)
kernel = kernel_y*kernel_x.T
mask = 255*kernel/np.linalg.norm(kernel)
mask = mask[int(0.5*row):,int(0.5*col):]

out = np.copy(img)

for i in range(chan):
  out[:,:,i] = out[:,:,i]*mask

cv2.imshow('shifted focus Vignette',out)

cv2.waitKey()  
