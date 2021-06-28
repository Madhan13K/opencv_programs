import cv2 as cv
import numpy as np
# to add two images
img=cv.imread('messi5.jpg')
img2=cv.imread('opencv-logo.png')
print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv.split(img)
print((b,g,r))
img=cv.merge((b,g,r))
#print(img)
ball=img[280:340,330:390]
img[273:333,100:160]=ball
img=cv.resize(img,(512,512))
img2=cv.resize(img2,(512,512))

#dst=cv.add(img,img2(
dst=cv.addWeighted(img,.9,img2,.1,0)
cv.imshow('image',dst)
cv.waitKey()
cv.destroyAllWindows()