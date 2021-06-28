import numpy as np
import cv2 as cv

def ntg(x):
    pass
# ig=np.zeros([512,512,3],np.uint8)
cv.namedWindow('Tracking')
cv.createTrackbar('LH','Tracking',0,255,ntg)
cv.createTrackbar('LS','Tracking',0,255,ntg)
cv.createTrackbar('LV','Tracking',0,255,ntg)
cv.createTrackbar('UH','Tracking',255,255,ntg)
cv.createTrackbar('US','Tracking',255,255,ntg)
cv.createTrackbar('HV','Tracking',255,255,ntg)
while(1):
    frame=cv.imread('smarties.png')
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    l_h=cv.getTrackbarPos('LH','Tracking')
    l_s=cv.getTrackbarPos('LS','Tracking')
    l_v=cv.getTrackbarPos('LV','Tracking')
    u_h=cv.getTrackbarPos('UH','Tracking')
    u_s=cv.getTrackbarPos('US','Tracking')
    u_v=cv.getTrackbarPos('UV','Tracking')
    lb=np.array([l_h,l_s,l_v])
    ub=np.array([u_h,u_s,u_v])
    mask=cv.inRange(hsv,lb,ub)
    res=cv.bitwise_and(frame,frame,mask=mask)
    cv.imshow('image',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k=cv.waitKey() & 0xFF
    if k==27:
        break
cv.destroyAllWindows()
