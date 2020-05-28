import RPi.GPIO as GPIO
import time
import math

GPIO.setwarnings(False)
Trig = [11, 10, 27, 24, 4, 15]
Echo = [9, 22, 17, 23, 3, 18]

print Trig[0], ", ", Echo[0]
# result = [[0 for col in range(10)] for row in range(6)]
result = []




GPIO.setmode(GPIO.BCM)
for i in Trig :
    GPIO.setup(i, GPIO.OUT)
    # print "TRIG : ", i
for j in Echo :
    GPIO. setup(j, GPIO.IN)
    # print "ECHO : ", j


try :
    for slot in range(0, 2) :
        # while True:
        sum = 0
        measure = []
        for num in range (0, 100):
            GPIO.output(Trig[slot], False)
            time.sleep(0.1)
            GPIO.output(Trig[slot], True)
            time.sleep(0.00001)
            GPIO.output(Trig[slot], False)
            while GPIO.input(Echo[slot]) == 0:
                start = time.time()             
            while GPIO.input(Echo[slot]) == 1:
                stop = time.time()
            time_interval = stop - start
            distance = time_interval * 17000
            distance = round(distance, 2)
            # result[slot][num] = distance
            # sum = sum + distance
            # print "result[", slot, "][", num, "] : ", result[slot][num]
            print "distance : " + str(distance)
            measure.append(distance)

        
        sort = sorted(measure)[9:60]
        print "sort : ", str(sort)
        result.append(round(math.fsum(sort) / 50, 1))
        print "result : ", str(result)
except KeyboardInterrupt :
    GPIO.cleanup()
    print "Exit..."