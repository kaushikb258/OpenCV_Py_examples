# cartoonize a live video stream

import cv2
import numpy as np


def draw_rect(event,x,y,flags,params):
 global x_init, y_init, drawing, top_left, bottom_right  

 if event == cv2.EVENT_LBUTTONDOWN:
  drawing = True
  x_init = x
  y_init = y

 elif event == cv2.EVENT_MOUSEMOVE:
  if drawing:
   top_left = (min(x_init,x),min(y_init,y))
   bottom_right = (max(x_init,x),max(y_init,y))
   img[y_init:y,x_init:x] = 255 - img[y_init:y,x_init:x]

 elif event == cv2.EVENT_LBUTTONUP:
  drawing = False
  top_left = (min(x_init,x),min(y_init,y))
  bottom_right = (max(x_init,x),max(y_init,y))
  img[y_init:y,x_init:x] = 255 - img[y_init:y,x_init:x]
 
if __name__=='__main__':
 drawing = False
 top_left = (0,0)
 bottom_right = (0,0)  

 cap = cv2.VideoCapture(0) 
 cv2.namedWindow('input')
 cv2.setMouseCallback('input',draw_rect)

 while True:
  ret, frame = cap.read()
  img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  
  edges = cv2.Laplacian(img,cv2.CV_8U,ksize=5)
  ret, mask = cv2.threshold(edges,100,255,cv2.THRESH_BINARY_INV) 

  img_small = cv2.resize(img,None,fx=0.25,fy=0.25,interpolation=cv2.INTER_AREA)
  num_rep = 10
  sigma_color = 5
  sigma_space = 7
  size = 5

  for i in range(num_rep):
   img_small = cv2.bilateralFilter(img_small,size,sigma_color,sigma_space)

  img_out = cv2.resize(img_small,None,fx=4.0,fy=4.0,interpolation=cv2.INTER_AREA)
  
  dst = np.zeros(img.shape)
  dst = cv2.bitwise_and(img_out,img_out,mask=mask)
  img = cv2.cvtColor(dst,cv2.COLOR_GRAY2BGR)

  (x0,y0) = top_left
  (x1,y1) = bottom_right
  img[y0:y1,x0:x1] = 255 - img[y0:y1,x0:x1] 
  cv2.imshow('input',img)

  if cv2.waitKey(1) == 27:
   break

cap.release()
cv2.destroyAllWindows()
 
