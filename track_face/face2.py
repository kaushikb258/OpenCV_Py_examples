import numpy as np
import cv2
 
# detect face, eyes, ears

face_cascade = cv2.CascadeClassifier('/home/kb/opencv-2.4.13/data/haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('/home/kb/opencv-2.4.13/data/haarcascades/haarcascade_eye.xml')
left_ear_cascade = cv2.CascadeClassifier('/home/kb/opencv-2.4.13/data/haarcascades/haarcascade_mcs_leftear.xml')
right_ear_cascade = cv2.CascadeClassifier('/home/kb/opencv-2.4.13/data/haarcascades/haarcascade_mcs_rightear.xml')

img = cv2.imread('kaushik.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
  cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
  roi_gray = gray[y:y+h, x:x+w]
  roi_color = img[y:y+h, x:x+w]
  eyes = eye_cascade.detectMultiScale(roi_gray)
  for (ex,ey,ew,eh) in eyes:
   cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

left_ear = left_ear_cascade.detectMultiScale(gray,1.3,5)
right_ear = right_ear_cascade.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in left_ear:
  cv2.circle(img,(x+int(w/2),y+int(h/2)),max(int(w/2),int(h/2)),(0,0,255),2)
for (x,y,w,h) in right_ear:
  cv2.circle(img,(x+int(w/2),y+int(h/2)),max(int(w/2),int(h/2)),(0,0,255),2) 

 
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
