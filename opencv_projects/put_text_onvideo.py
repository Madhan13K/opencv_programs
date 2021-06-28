import cv2
import datetime
# This file shows how to open videocamera and capture the images/videos using open-cv
cap=cv2.VideoCapture(0) #to open video camera and set to given system camera attribute
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))                                  # cap.get(3)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.isOpened())
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1208)  #  OR WE CAN USE THE ASSOCIATED NUMBERS  cap.set(3,1208)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,720) #                                           cap.set(4,720
while(cap.isOpened()):
    ret,frame=cap.read()    #ret shows true/false and cap stores the frames that are read
    if ret==True:
        font=cv2.FONT_HERSHEY_COMPLEX
        text='WIDTH: '+ str(cap.get(3)) + 'HEIGHT: ' + str(cap.get(4))
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame,datet,(10,50),font,1,(0,255,255),1,cv2.LINE_AA)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
