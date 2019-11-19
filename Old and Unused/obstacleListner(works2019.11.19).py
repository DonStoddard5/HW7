# as of 12:58:33 PM 2019.11.19 this code works to read the data from the talker

#!/usr/bin/env python
import rospy
#from std_msgs.msg import String
from std_msgs.msg import Float32



def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %f", data.data)



def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("obstacle", Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()