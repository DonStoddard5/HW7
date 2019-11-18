# Demo of reading the range and lux from the VL6180x distance sensor and
# printing it every second.
# Author: Tony DiCola

#! /usr/bin/python

from gpiozero import Servo

import time

import board
import busio

import adafruit_vl6180x


# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create sensor instance.
sensor = adafruit_vl6180x.VL6180X(i2c)

servoPIN = 17  # this must be the GPIO# not the physical pin #. e.g. to use pin 11 (GPIO17), this must be 17
moveDelay = 0.75
myCorrection = 0.2  # used to correct the motion of the servo. It is servo specific
maxPW = (2.0 + myCorrection) / 1000
minPW = (1.0 - myCorrection - .1) / 1000

servo = Servo(servoPIN, min_pulse_width=minPW, max_pulse_width=maxPW)  # initalize a servo

# swings the arm back and forth, because it feels like there should be some sort of startup sequence
servo.value = -1
time.sleep(moveDelay)
servo.value = 1
time.sleep(moveDelay)
servo.value = 0
time.sleep(moveDelay)

delay = .1 # delay time

def remap( x, oMin, oMax, nMin, nMax ):

    #range check
    if oMin == oMax:
        print ("Warning: Zero input range")
        return None

    if nMin == nMax:
        print ("Warning: Zero output range")
        return None

    #check reversed input range
    reverseInput = False
    oldMin = min( oMin, oMax )
    oldMax = max( oMin, oMax )
    if not oldMin == oMin:
        reverseInput = True

    #check reversed output range
    reverseOutput = False
    newMin = min( nMin, nMax )
    newMax = max( nMin, nMax )
    if not newMin == nMin :
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result

# Main loop prints the range and lux every delay:
while True:
    # Read the range in millimeters and print it.
    range_mm = sensor.range #goes from 0 to 255
    #print('Range: {0}mm'.format(range_mm))
    servoPos = remap(range_mm, 0, 255, -1, 1)
    servo.value = servoPos
    print('Range: {}mm, servoPos: {}'
          .format(range_mm, servoPos))

    time.sleep(delay)

servo.stop()
GPIO.cleanup();