import RPi.GPIO as GPIO
import time

servo = 6
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo, GPIO.OUT)
servo=GPIO.PWM(servo, 50)
servo.start(0)
cnt=0

try:
    while True:
        servo.ChangeDutyCycle(12.5)
        time.sleep(1)
        servo.ChangeDutyCycle(10.0)
        time.sleep(1)
        servo.ChangeDutyCycle(7.5)
        time.sleep(1)
        servo.ChangeDutyCycle(5.0)
        time.sleep(1)
        servo.ChangeDutyCycle(2.5)
        time.sleep(1)
except KeyboardInterrupt:
    servo.stop()

GPIO.cleanup()
