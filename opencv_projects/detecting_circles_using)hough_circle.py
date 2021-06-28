import numpy as np
import cv2 as cv
img=cv.imread('shape.png')
output=img.copy()

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=cv.medianBlur(gray,5)
circle=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,minDist=20,param1=50,param2=30,minRadius=0,maxRadius=0)
detected_circles=np.uint16(np.round(circle))
for (x,y,r) in detected_circles[0,:]:
    cv.circle(output,(x,y),r,(0,255,0),thickness=2)
    cv.circle(output,(x,y),2,(0,255,255),thickness=2)



cv.imshow('smarties',output)
cv.waitKey()
cv.destroyAllWindows()