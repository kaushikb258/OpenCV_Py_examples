import cv2
import numpy as np

img = cv2.imread('sally.jpg')
row, col, chan = img.shape

# Blur

kernel3 = np.ones((3,3),np.float32)/9.0
kernel5 = np.ones((5,5),np.float32)/25.0
kernel11 = np.ones((11,11),np.float32)/121.0

out = cv2.filter2D(img,-1,kernel3)
cv2.imshow('kernel3',out)
cv2.waitKey()

out = cv2.filter2D(img,-1,kernel5)
cv2.imshow('kernel5',out)
cv2.waitKey()

out = cv2.filter2D(img,-1,kernel11)
cv2.imshow('kernel11',out)
cv2.waitKey()



# Edge detection

sobel_hor = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobel_vert = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imshow('Sobel-hor',sobel_hor)
cv2.imshow('Sobel-vert',sobel_vert)
cv2.waitKey()

laplacian = cv2.Laplacian(img,cv2.CV_64F)
canny = cv2.Canny(img,50,240)

cv2.imshow('Laplacian',laplacian)
cv2.imshow('Canny',canny)
cv2.waitKey()



# Motion Blur

size = 15
kernel = np.zeros((size,size))
kernel[(size-1)/2,:] = np.ones(size)
kernel = kernel/size

out = cv2.filter2D(img,-1,kernel)
cv2.imshow('Motion blur',out)
cv2.waitKey()


# Sharpen

kernel = np.array([[-1, -1, -1, -1, -1], [-1, 2, 2, 2, -1], [-1, 2, 8, 2, -1], [-1, 2, 2, 2, -1], [-1, -1, -1, -1, -1]])/8.0

out = cv2.filter2D(img,-1,kernel)
cv2.imshow('Sharp',out)
cv2.waitKey()


