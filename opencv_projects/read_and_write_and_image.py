import cv2 as cv
#This file shows to read,wrie,show the image using open-cv
img=cv.imread('lena.jpg')
cv.imshow('image',img)
print(img)
k= cv.waitKey() &0XFF   #(TO MASK)
if k==27:
    cv.destroyAllWindows()
elif k==ord('s'):
    cv.imwrite('lena_copy.jpg',img)
    cv.destroyAllWindows()