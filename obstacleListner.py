#!/usr/bin/env python
import rospy

from std_msgs.msg import Float32

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # code taken from https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def callback(data):
    rangeMin = 10
    rangeMax = 160
    servoMin = 7.5
    servoMax = 12.5
    heardData = data.data # data comes in ~10 to a max of 160
    # this needs to be mapped to 7.5 for servo at 0
    # and 12.5 for servo at 180
    mappedData = translate(heardData, rangeMin, rangeMax, servoMin, servoMax)
    p.ChangeDutyCycle(mappedData)
    rospy.loginfo(rospy.get_caller_id() + "I heard %f, mapped to %f", heardData, mappedData)
    time.sleep(1)



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