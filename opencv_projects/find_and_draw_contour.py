import numpy as np
import cv2 as cv

img=cv.imread('opencv-logo.png')
imgray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
res,thresh=cv.threshold(img,237,255,0)
contours,heirachy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print("number of cotours= "+str(len(contours)))
cv.drawContours(img,contours,-1,(0,255,0),3)
cv.imshow('image',img)
cv.imshow('gray',imgray)
cv.waitKey()
cv.destroyAllWindows()