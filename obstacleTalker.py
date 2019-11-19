# here's something I ran in terminal to get the sensor to work:     apt-get install libffi-dev
# !/usr/bin/env python
# license removed for brevity

# 2019.11.19 12:53:25 PM This codes sends out the distance in milimeters.
# will output ~10 to max of 160
import rospy
# from std_msgs.msg import String
from std_msgs.msg import Float32
from rpisensors.proximity import VL6180X

def talker():
    pub = rospy.Publisher('obstacle', Float32, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        # rospy.loginfo(hello_str)
        sensor = VL6180X(1)
        distance = sensor.read_distance()
        print("publishing = {} mm".format(distance))
        pub.publish(distance)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
