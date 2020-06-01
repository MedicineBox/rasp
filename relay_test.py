import RPi.GPIO as GPIO
import time

relay = [21, 20, 16, 13, 19, 26]
GPIO.setmode(GPIO.BCM)
for i in relay :
    GPIO.setup(i, GPIO.OUT)


def open(slot) :
    slot = slot - 1
    GPIO.output(relay[slot], True)
    print("true")
    time.sleep(2)


    GPIO.output(relay[slot], False)
    print("false")

open(1)
open(2)
GPIO.cleanup()
