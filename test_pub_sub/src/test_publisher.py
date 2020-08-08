#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import time 
from datetime import datetime
def publisher():

	pub	= rospy.Publisher('string_publish',String,queue_size=10)

	rate	= rospy.Rate(1)

	msg_to_publish	= String()
#	now = datetime.now()
#	servertime = time.strftime("%X")

	while not rospy.is_shutdown():
		now = datetime.now()
		servertime = now.strftime("%Y-%m-%d %H:%M:%S")
		string_to_publish = "%s"%servertime
                servertime = time.strftime("%X")
		msg_to_publish.data = string_to_publish
		pub.publish(msg_to_publish)

		rospy.loginfo(string_to_publish)

		rate.sleep()

if __name__ == "__main__":
	rospy.init_node("simple_publihser")
	publisher()
