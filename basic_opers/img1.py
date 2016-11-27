import cv2

img = cv2.imread('sally.jpg')

# grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('my window',gray_img)
cv2.waitKey()

#yuv scale
yuv_img = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
cv2.imshow('Y channel',yuv_img[:,:,0])
cv2.imshow('U channel',yuv_img[:,:,1])
cv2.imshow('V channel',yuv_img[:,:,2])
cv2.waitKey()

# hsv scale
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('H channel',hsv_img[:,:,0])
cv2.imshow('S channel',hsv_img[:,:,1])
cv2.imshow('V channel',hsv_img[:,:,2])
cv2.waitKey()
