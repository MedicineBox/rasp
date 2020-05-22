import RPi.GPIO as GPIO
import time

Trig = 11
Echo = 9

GPIO.setmode(GPIO.BCM)
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

print "Press SW or inpur Ctrl+c to quit"

try:
    while True:
        GPIO.output(Trig, False)
        time.sleep(0.5)

        GPIO.output(Trig, True)
        time.sleep(0.00001)
        GPIO.output(Trig, False)

        while GPIO.input(Echo) == 0:
            start = time.time()             

        while GPIO.input(Echo) == 1:
            stop = time.time()

        time_interval = stop - start
        distance = time_interval * 17000
        dictance = round(distance, 2)

        print "Distance => ", distance, " cm"

except KeyboardInterrupt:
    GPIO.cleanup()
    print "Exit..."

