import cv2
import numpy as np

img = cv2.imread('tower.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#SURF
surf = cv2.SURF()
surf.hessianThreshold = 15000
kp, des = surf.detectAndCompute(gray,None)
img = cv2.drawKeypoints(img,kp,None,(0,255,0),4)
cv2.imshow('SURF',img)
cv2.waitKey()


# FAST
fast = cv2.FastFeatureDetector()
keypoints = fast.detect(gray,None)
print "FAST with non max suppression", len(keypoints)
img_out = cv2.drawKeypoints(gray,keypoints,color=(0,0,255))
cv2.imshow('FAST - non max suppression',img_out)
cv2.waitKey()

# Disable non max suppression
fast.setBool('nonmaxSuppression',False)
keypoints = fast.detect(gray,None)
print "FAST without non max suppression", len(keypoints)
img_out = cv2.drawKeypoints(gray,keypoints,color=(0,0,255))
cv2.imshow('FAST - without non max suppression',img_out)
cv2.waitKey()


# ORB
orb = cv2.ORB()
keypoints = orb.detect(gray,None)
kp, des = orb.compute(gray,keypoints)
img_out = cv2.drawKeypoints(img,kp,color=(0,255,0),flags=0)
cv2.imshow('ORB',img_out)
cv2.waitKey()
