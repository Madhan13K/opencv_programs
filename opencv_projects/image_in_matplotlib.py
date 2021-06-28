import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread('lena.jpg',-1)
cv.imshow('image',img)
print(img.shape)
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.xticks([])
plt.yticks([])

plt.show()
cv.waitKey()
cv.destroyAllWindows()