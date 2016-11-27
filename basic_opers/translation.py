import cv2
import numpy as np

img = cv2.imread('sally.jpg')
row, col, chan = img.shape
print row, col, chan

tx = 90
ty = 50

# translate image
trans_mat = np.float32([[1, 0, tx], [0, 1, ty]])
img_trans = cv2.warpAffine(img,trans_mat,(row,col))
cv2.imshow('translation image',img_trans)


# translate image using loops
t1_img = np.zeros(([row,col,chan]),dtype=np.uint8)
for r in range(row):
 for c in range(col):
  for ch in range(chan):
   r1 = r + ty
   c1 = c + tx
   if(r1 <= row-1 and c1 <= col-1): 
    t1_img[r1,c1,ch] = img[r,c,ch]
cv2.imshow('my image',t1_img)  
print t1_img.shape
cv2.waitKey()


# rotate image
r_mat = cv2.getRotationMatrix2D((row/2,col/2),30,1)
img_rot = cv2.warpAffine(img,r_mat,(col,row))
cv2.imshow('rot img',img_rot)
cv2.waitKey()


# scale image
img_scaled = cv2.resize(img,None,fx=1.2,fy=1.2,interpolation=cv2.INTER_LINEAR)
cv2.imshow('linear interp',img_scaled)
img_scaled = cv2.resize(img,None,fx=1.2,fy=1.2,interpolation=cv2.INTER_CUBIC)
cv2.imshow('cubic interp',img_scaled)
img_scaled = cv2.resize(img,(525,189),interpolation=cv2.INTER_AREA)
cv2.imshow('skewed',img_scaled)
cv2.waitKey()


# Affine transformation
src_pts = np.float32([[0,0], [0,row-1], [col-1,0]])
dst_pts = np.float32([[0,0], [int(0.4*(col-1)),row-1], [int(0.6*(col-1)),0]])
affine_mat = cv2.getAffineTransform(src_pts,dst_pts)
img_out = cv2.warpAffine(img,affine_mat,(col,row))
cv2.imshow('affine',img_out)
cv2.waitKey()


# mirror image
src_pts = np.float32([[0,0], [0,row-1], [col-1,0]])
dst_pts = np.float32([[col-1,0], [col-1,row-1], [0,0]])
affine_mat = cv2.getAffineTransform(src_pts,dst_pts)
img_out = cv2.warpAffine(img,affine_mat,(col,row))
cv2.imshow('mirror',img_out)
cv2.waitKey()


#projective transformations
src_pts = np.float32([[0,0], [0,row-1], [col-1,0], [col-1,row-1]])
dst_pts = np.float32([[0,0], [int(0.33*(col-1)),row-1], [col-1,0], [int(0.66*(col-1)),row-1]])
proj_mat = cv2.getPerspectiveTransform(src_pts,dst_pts)
img_out = cv2.warpPerspective(img,proj_mat,(col,row))
cv2.imshow('projective',img_out)
cv2.waitKey()


