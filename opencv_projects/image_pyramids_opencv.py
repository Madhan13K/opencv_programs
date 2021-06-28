import cv2 as cv
import numpy as np
img=cv.imread('lena.jpg')
layer=img.copy()
gp=[layer]
for i in range(6):
    layer=cv.pyrDown(layer)
    gp.append(layer)
    #cv.imshow(str(i),layer)
# lr=cv.pyrDown(img)
# lr1=cv.pyrDown(lr)
# hr=cv.pyrUp(lr1)
layer=gp[5]
cv.imshow('upper level',layer)
lp=[layer]
for i in range(5,0,-1):
    guassian_extend=cv.pyrUp(gp[i])
    lapalcian=cv.subtract(gp[i-1],guassian_extend)
    cv.imshow(str(i),lapalcian)
cv.imshow('image',img)
# cv.imshow('pyrdown',lr)
# cv.imshow('2nd pyrdown',lr1)
# cv.imshow('pyrup',hr)
cv.waitKey()
cv.destroyAllWindows()