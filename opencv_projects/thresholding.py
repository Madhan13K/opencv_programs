import numpy as np
import cv2 as cv
def thresholding(img):
    imghsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    lowerlimit=np.array([0,0,0,])
    upperlimit=np.array([179,255,255])
    maskwite=cv.inRange(imghsv,lowerlimit,upperlimit)
    return  maskwite