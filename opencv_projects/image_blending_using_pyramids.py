import cv2 as cv
import  numpy as np
apple=cv.imread('apple.jpg')
orange=cv.imread('orange.jpg')
print(apple.shape)
print(orange.shape)
apple_orange=np.hstack((apple[:,:256],orange[:, 256:]))
# guassian pyramid fo apple
apple_copy=apple.copy()
gp_apple=[apple_copy]
for i in range(6):
    apple_copy=cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)
# guassian pyramid fo orange
orange_copy=orange.copy()
gp_orange=[orange_copy]
for i in range(6):
    orange_copy=cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)
# laplacian pyramid fo apple
apple_copy=gp_apple[5]
lp_apple=[apple_copy]
for i in range(5,0,-1):
    guassian_extended=cv.pyrUp(gp_apple[i])
    laplacian=cv.subtract(gp_apple[i-1],guassian_extended)
    lp_apple.append(laplacian)
#laplacian pyramid for orange
orange_copy=gp_orange[5]
lp_orange=[orange_copy]
for i in range(5,0,-1):
    guassian_extended=cv.pyrUp(lp_orange[i])
    laplacian=cv.subtract(lp_orange[i-1],guassian_extended)
    lp_orange.append(laplacian)

apple_orange_pyramid=[]
n=0
for apple_lap,orange_lap in zip(lp_apple,lp_orange):
    n+=1
    cols,rows,ch=apple_lap.shape
    laplacian=np.hstack(apple_lap[:,0:int(cols/2)],orange_lap[:,int(cols/2)])
    apple_orange_pyramid.append(laplacian)
apple_orange_reconstruct=apple_orange_pyramid[0]
for i in range(1,6):
    apple_orange_reconstruct=cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct=cv.add(apple_orange_reconstruct,apple_orange_pyramid)

cv.imshow('apple',apple)
cv.imshow('orange',orange)
cv.imshow('apple_orange',apple_orange)
cv.imshow('apple_orange',apple_orange_reconstruct)
cv.waitKey()
cv.destroyAllWindows()