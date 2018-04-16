import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
 
prev_input = 0

while True:
    input = GPIO.input(4)
    if ((not prev_input) and input):
        print 'Shuting Down'
        os.system("sudo halt")
    prev_input = input
    time.sleep(0.05)



