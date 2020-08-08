#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import subprocess
def subscriber():
	sub = rospy.Subscriber('string_publish', String, callback_function)

	rospy.spin()

def callback_function(message):
	#rospy.loginfo("I received: %s"%message.data)
	#p = subprocess.Popen(["echo",message.data],stdout=subprocess.PIPE)
#	p = subprocess.Popen(["date","+%T","-s",message.data],stdout=subprocess.PIPE)
	p = subprocess.Popen(["date","-s",message.data],stdout=subprocess.PIPE)
	output,err=p.communicate()
	print output
	
if __name__ == "__main__":
	rospy.init_node("simple_subscriber")
	subscriber()
