import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('/home/bhumika/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml')
face_cascade1 = cv2.CascadeClassifier('/home/bhumika/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
face_cascade2 = cv2.CascadeClassifier('/home/bhumika/opencv/data/haarcascades/haarcascade_profileface.xml')
eye_cascade = 	cv2.CascadeClassifier('/home/bhumika/opencv/data/haarcascades/haarcascade_eye.xml')
img= cv2.imread('i4.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
faces1= face_cascade1.detectMultiScale(gray, 1.3, 5)
faces2= face_cascade1.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]
	eyes = eye_cascade.detectMultiScale(roi_gray)
	for (ex,ey,ew,eh) in eyes:
	 	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

for (x,y,w,h) in faces1:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]
	
for (x,y,w,h) in faces2:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]


img1 = cv2.resize(img, (400, 300))
cv2.imshow('Detected faces',img1)
with open("examples.txt") as f:
		content=f.readlines()

length=len(content)
print length
for i in range(0,length):
	        x,y=content[i].rstrip().split(',')[0],content[i].rstrip().split(',')[1]
		cv2.rectangle(img1, (int(x)+5, int(y)+5), (int(x)+8, int(y)+8), (0,0,255), -1)

img1=cv2.resize(img1,(800,534))
cv2.imshow('Detected faces',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
