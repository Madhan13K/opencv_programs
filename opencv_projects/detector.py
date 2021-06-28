import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

def region_of_intrest(img,vertices):
    mask=np.zeros_like(img)
    # channel=img.shape[2]
    match_mask_colour=(255,)
    cv.fillPoly(mask,vertices,match_mask_colour)
    masked_images=cv.bitwise_and(img,mask)
    return masked_images


def drawlines(image,lines):
    img=np.copy(image)
    line_image=np.zeros((image.shape[0],image.shape[1],3),dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv.line(line_image,(x1,y1),(x2,y2),(0,255,0),1)


    image=cv.addWeighted(image,0.8,line_image,1,0.0)
    return image
def process(image):

# img=cv.imread('road.jpg')
# image=cv.cvtColor(img,cv.COLOR_BAYER_BG2RGB)
 height=image.shape[0]
 width=image.shape[1]
 region_of_intrest_vertices=[ (0,height),(width/2,height/2),(width,height)]



 gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
 canny_image=cv.Canny(gray,100,200)
 cropped_image=region_of_intrest(canny_image,np.array([region_of_intrest_vertices],np.int32))
 lines=cv.HoughLinesP(cropped_image,rho=6,theta=np.pi/60,threshold=160,lines=np.array([]),minLineLength=40,maxLineGap=25)
 image_with_lines=drawlines(image,lines)
 #cv.imshow('cany',canny_image)
# plt.imshow(image_with_lines)
# plt.show()


cap=cv.VideoCapture('test.mp4')
while cap.isOpened():
    ret,frame=cap.read()
    frame=process(frame)
    cv.imshow('frame',frame)
    if cv.waitKey(1) &0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()