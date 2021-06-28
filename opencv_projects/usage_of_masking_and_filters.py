import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('smarties.png')
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_,mask=cv.threshold(img,220,255,cv.THRESH_BINARY_INV)
kernal=np.ones((2,2),np.uint8)
dilation=cv.dilate(mask,kernal,iterations=2)
erosion=cv.erode(mask,kernal,iterations=1)
opening=cv.morphologyEx(mask,cv.MORPH_OPEN,kernal)
closing=cv.morphologyEx(mask,cv.MORPH_CLOSE,kernal)
mg=cv.morphologyEx(mask,cv.MORPH_GRADIENT,kernal)
th=cv.morphologyEx(mask,cv.MORPH_TOPHAT,kernal)

title=['smarties','mask','dilate','erosion','opening','closing','mg','th']
images=[img,mask,dilation,erosion,opening,closing,mg,th]
for i in range(8):
    plt.subplot(3,3,i+1),plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])
plt.show()