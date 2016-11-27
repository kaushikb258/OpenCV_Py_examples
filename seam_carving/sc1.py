import cv2
import numpy as np
import sys

def compute_energy(img):
 gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 sobel_x = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
 sobel_y = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)
 abs_sobel_x = cv2.convertScaleAbs(sobel_x)
 abs_sobel_y = cv2.convertScaleAbs(sobel_y)
 energy = cv2.addWeighted(abs_sobel_x,0.5,abs_sobel_y,0.5,0)
 return energy


def path_energy(rows,cols1,e):
 e1 = np.zeros(cols1,dtype=np.float)
 for j in range(cols1):
  jc = j
  for i in range(rows): 
   if jc==0:
     if e[i,jc] < e[i,jc+1]:
      e1[j] += e[i,jc]
     else:
      e1[j] += e[i,jc+1]
      jc = jc+1        
   if jc==cols1-1:
     if e[i,jc-1] < e[i,jc]:
      e1[j] += e[i,jc-1]
      jc = jc-1
     else:
      e1[j] += e[i,jc]
   if jc>0 and jc <cols1-1:
     if e[i,jc-1] < min(e[i,jc],e[i,jc+1]):
      e1[j] += e[i,jc-1]
      jc = jc-1
     elif e[i,jc] < min(e[i,jc-1],e[i,jc+1]):
      e1[j] += e[i,jc]
     else:
      e1[j] += e[i,jc+1]
      jc = jc+1
 j = np.argmin(e1)
 # this j is the column number of min energy path  
 jj = np.zeros(rows,dtype=np.int)  
 jc = j
 for i in range(rows): 
   if jc==0:
     if e[i,jc] < e[i,jc+1]:
      jc = jc
     else:
      jc = jc+1        
   if jc==cols1-1:
     if e[i,jc-1] < e[i,jc]:
      jc = jc-1
     else:
      jc = jc
   if jc>0 and jc <cols1-1:
     if e[i,jc-1] < min(e[i,jc],e[i,jc+1]):
      jc = jc-1
     elif e[i,jc] < min(e[i,jc-1],e[i,jc+1]):
      jc = jc
     else:
      jc = jc+1
   jj[i] = jc
 return j, jj 


def remove_seam(img1,rows,cols1,jj):
 for i in range(rows):
  jremove = jj[i]
  img1[i,jremove:cols1-2,:] = img1[i,jremove+1:cols1-1,:]
 img1 = img1[:,:-1,:]  
 return img1

def vertical_seam_shrink(cols_desired,img):
 rows, cols, chan = img.shape 
 img1 = np.copy(img)  
 cols1 = cols
 while cols1 > cols_desired:
  e = compute_energy(img1)
  jmin, jj = path_energy(rows,cols1,e)
  img1 = remove_seam(img1,rows,cols1,jj)
  cols1 -= 1  
 return img1 


if __name__ == '__main__':
 img = cv2.imread(sys.argv[1])
 rows, cols, chan = img.shape
 print "dimensions of original image = ", rows, cols

 cols_desired = cols - 200
 img_out = vertical_seam_shrink(cols_desired,img)
 print "dimensions of seam carved image = ", img_out.shape[:2]

 cv2.imshow('original image', img)
 cv2.imshow('seam carved image',img_out)
 cv2.imwrite('seam_carved_shrunk.jpg',img_out)
 cv2.waitKey()
