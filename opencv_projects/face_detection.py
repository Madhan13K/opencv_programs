import cv2 as cv
import numpy as np
face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv.imread('lena.png')
grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(grey,1.1,4)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+h,y+w),(0,255,0),thickness=2)

cv.imshow('output',img)
cv.waitKey()
cv.destroyAllWindows()