import cv2 as cv
import numpy as np
#img=cv.imread('lena.jpg')
img=np.zeros([512,512,3],np.uint8)
img=cv.line(img,(0,0),(255,255),(0,0,255),10) # we should want to give bgr form for line
img=cv.arrowedLine(img,(0,255),(255,255),(255,0,0),10)

img=cv.rectangle(img,(384,0),(510,120),(0,0,255),10)
img=cv.circle(img,(447,63),63,(0,255,0),-1)
font=cv.FONT_HERSHEY_COMPLEX
img=cv.putText(img,'opencv',(10,500),font,4,(0,255,255),10,cv.LINE_AA)
cv.imshow('image',img)
cv.waitKey()
cv.destroyAllWindows()