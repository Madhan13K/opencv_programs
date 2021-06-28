import numpy as np
import cv2 as cv
#bitwise operators in opencv

img1=np.zeros([250,500,3],np.uint8)
img1=cv.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2=cv.imread('image_1.png')
bitAnd=cv.bitwise_and(img1,img2)
bitOr=cv.bitwise_or(img1,img2)
bitXor=cv.bitwise_xor(img1,img2)
bitNot=cv.bitwise_not(img1)
cv.imshow('bitAnd',bitAnd)
cv.imshow('bitOr',bitOr)

cv.imshow('img1',img1)
cv.imshow('img2',img2)
cv.waitKey()
cv.destroyAllWindows()