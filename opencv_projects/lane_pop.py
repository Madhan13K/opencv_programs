import roslib
import sys
import rospy
import cv2
import numpy as np 
from cv_bridge import CvBridge , CvBridgeError
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image

class LineFollower(object):

	def __init__(self):

		self.bridge_object = CvBridge()
		self.image_sub = rospy.Subscriber("/camera1/image_raw" , Image, self.camera_callback )

	def camera_callback(self,data):

		try:
			#we select brg8 because its the opencv encoding by default
			cv_image = self.bridge_object.imgmsg_to_cv2(data, desired_encoding= "bgr8")
		except CvBridgeError as e:
			print(e)
        height,width,channels=cv_image.shape
	    descentre=160
	    rows_to_watch=20
        crop_image=cv_image[(height)/2+descentre:(height)/2+(descentre+rows_to_watch)][1:width]
		hsv=cv2.cvtColor(crop_image,cv2.COLOR_BGR2HSV)
		lower_yellow=np.array([20,100,100])
		higher_value=np.array([50,255,255])
		mask=cv2.inRange(hsv,lower_yellow,higher_value)
		res=cv2.bitwise_and(crop_image,crop_image,mask=mask)
		m=cv2.moments(mask,False)
		try:
			cx,cy=m['m10']/m['m00'],m['m01']/m['m00']
        except ZeroDivisionError:
            cx,cy=height/2,width/2
	    error_x=cx-width/2
		twist_object=Twist()
		twist_object.linear.x=0.2
        twist_object.angular.z=-error/100
		rospy.loginfo('ANGULAR VALUE SENT '+str(twist_object.angular.z))
		self.lanebot_object.move_robot(twist_object)
		cv2.imshow("Image Window" , res)
		cv2.waitKey()

def main():
	line_follower_object = LineFollower()
	rospy.init_node('line_follower_node',anonymous = True)
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("shutting down")
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()