# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
# yolo=cv.dnn.readNet('yolov3.weights','yolov3.cfg')
# def ally(n):
#     n=int(n)
#     a=[]
#     b=[]
#     for i in range(1,n+1):
#         a.append(i)
#     for i in range(n):
#          c=reverse_num(a[i])
#          b.append(c)
#     #print(b)
#     c=list(set(b))
#     return len(c)
#
#
#
# def reverse_num(num):
#     reverse1=0
#     while (num>0):
#         rem=num%10
#         reverse1=reverse1*10 +rem
#         num=num//10
#     return reverse1
#
#
#
#
# def ally(n):
#    n=int(n)
#    str1=list()
#    count=0
#    for i in range(1,n+1):
#        str1=str(i)
#        res=check(str1)
#        if res==1:
#          count+=1
#    return count
#
# def check(num):
#     l1=[]
#     l2=[]
#     for i in num:
#         l1.append(i)
#     l2=sorted(l1)
#     if l1==l2:
#         return 1
#     else:
#         return 0
#
#
#
#
#
# print(ally(input('enter the sequence')))



import numpy as np
import cv2 as cv
import utlis
def getLaneCurve(img):
    imgThreshold=utlis.thresholding(img)
    cv.imshow('imthresh',imgThreshold)
    return None






if __name__=='__main__':
    cap=cv.VideoCapture('vid.mp4')
    while True:
        success, img=cap.read()
        img= cv.resize(img,(480,240))
        getLaneCurve(img)
        cv.imshow('vid',img)
        cv.waitKey()
