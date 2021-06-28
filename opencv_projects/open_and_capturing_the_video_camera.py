import cv2
# This file shows how to open videocamera and capture the images/videos using open-cv
cap=cv2.VideoCapture(0) #to open video camera and set to given system camera attribute
fourcc=cv2.VideoWriter_fourcc('X','V','A','Q')
out=cv2.VideoWriter('output.mp4',fourcc,20,(640,480))

print(cap.isOpened())
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1208)  #  OR WE CAN USE THE ASSOCIATED NUMBERS  cap.set(3,1208)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,720) #                                           cap.set(4,720
while(cap.isOpened()):
    ret,frame=cap.read()    #ret shows true/false and cap stores the frames that are read
    if ret==True:
      print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))                                  # cap.get(3)
      print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))                                   # cap.get(4)
      out.write(frame)  # to write in out file
      gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',gray)

      if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    else:
        break
cap.release()
out.release() #to release all the frames
cv2.destroyAllWindows()
