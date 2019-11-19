# code taken from https://projectiot123.com/2019/02/01/raspberry-pi-gpio-programming-example-for-servo-motor-using-python/

#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(7.5)


p.ChangeDutyCycle(12.5)  # turn towards 180 degree
time.sleep(1)  # sleep 1 second
p.ChangeDutyCycle(2.5)  # turn towards 0 degree
time.sleep(1)  # sleep 1 second
p.ChangeDutyCycle(7.5)  # turn towards 90 degree
time.sleep(1)  # sleep 1 second

try:
    while True:
        p.ChangeDutyCycle(12.5)  # turn towards 180 degree
        time.sleep(1)  # sleep 1 second
        p.ChangeDutyCycle(2.5)  # turn towards 0 degree
        time.sleep(1)  # sleep 1 second
        p.ChangeDutyCycle(7.5)  # turn towards 90 degree
        time.sleep(1)  # sleep 1 second
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()