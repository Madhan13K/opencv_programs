import numpy as np
import cv2 as cv
# events=[i for i in dir(cv) if'EVENT' in i]  to get events in opencv
# print(events)
def click_event(event,x,y,flags,param):
    if event==cv.EVENT_FLAG_LBUTTON:
        # cv.circle(img,(x,y),3,(0,0,255),-1)
        # points.append((x,y))                                   for joning of two points through line in open cv
        # if len(points)>=2:
        #     cv.line(img,points[-1],points[-2],(0,255,0),5)
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        cv.circle(img,(x,y),3,(0,0,255),-1)
        mycolor_image=np.zeros([512,512,3],np.uint8)
        mycolor_image[:]=[blue,green,red]                          # for getting the color throughout the window using opencv
        cv.imshow('color_image',mycolor_image)


#img=np.zeros([512,512,3],np.uint8)
img=cv.imread('lena_copy.jpg')
cv.imshow('image',img)
points=[]
cv.setMouseCallback('image',click_event)
cv.waitKey()
cv.destroyAllWindows()