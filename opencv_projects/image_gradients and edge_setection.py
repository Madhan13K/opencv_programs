import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('messi5.jpg',cv.IMREAD_GRAYSCALE)
lap=cv.Laplacian(img,cv.CV_64F,ksize=1)
lap=np.uint8(np.absolute(lap))
sobalX=cv.Sobel(img,cv.CV_64F,1,0)
sobelX=np.uint8(np.absolute(sobalX))
sobelY=cv.Sobel(img,cv.CV_64F,0,1)
sobelY=np.uint8(np.absolute(sobelY))
sobelXY=cv.bitwise_or(sobelX,sobelY)
canny_edge=cv.Canny(img,100,200)
titles=['image','laplacian','sobelX','sobelY','sobelXY','canny_edge']
img=[img,lap,sobalX,sobelY,sobelXY,canny_edge]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(img[i])
    plt.title([titles[i]])
    plt.xticks(),plt.yticks()
plt.show()