# make ghost of a live video stream

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
  img = cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
  (x0,y0) = top_left
  (x1,y1) = bottom_right
  img[y0:y1,x0:x1] = 255 - img[y0:y1,x0:x1] 
  cv2.imshow('input',img)

  if cv2.waitKey(1) == 27:
   break

cap.release()
cv2.destroyAllWindows()
 
