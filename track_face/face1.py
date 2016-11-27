import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('/home/kb/opencv-2.4.13/data/haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('/home/kb/opencv-2.4.13/data/haarcascades/haarcascade_eye.xml')
left_ear_cascade = cv2.CascadeClassifier('/home/kb/opencv-2.4.13/data/haarcascades/haarcascade_mcs_leftear.xml')
right_ear_cascade = cv2.CascadeClassifier('/home/kb/opencv-2.4.13/data/haarcascades/haarcascade_mcs_rightear.xml')

cap = cv2.VideoCapture(0)
cv2.namedWindow('face and eye detector')
scaling = 0.5

while True:
  ret, frame = cap.read()
  frame = cv2.resize(frame,None,fx=scaling,fy=scaling,interpolation=cv2.INTER_AREA)
  gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  face_rects = face_cascade.detectMultiScale(gray,1.3,5)
  for (x,y,w,h) in face_rects:
   cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
   roi_gray = gray[y:y+h, x:x+w]
   roi_color = frame[y:y+h, x:x+w]
   eyes = eye_cascade.detectMultiScale(roi_gray)
   for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

  left_ear = left_ear_cascade.detectMultiScale(gray,1.3,5)
  right_ear = right_ear_cascade.detectMultiScale(gray,1.3,5)
  for (x,y,w,h) in left_ear:
   cv2.circle(frame,(x+int(w/2),y+int(h/2)),max(int(w/2),int(h/2)),(0,0,255),2)
  for (x,y,w,h) in right_ear:
   cv2.circle(frame,(x+int(w/2),y+int(h/2)),max(int(w/2),int(h/2)),(0,0,255),2)  

  cv2.imshow('face and eye detector',frame)

  if cv2.waitKey(1) == 27:
   break

cap.release()
cv2.destroyAllwindows()
