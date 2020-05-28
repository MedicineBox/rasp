import RPi.GPIO as GPIO
import time

module = [6, 5, 12, 7, 8, 25]

# select = 0
def dosing(slot) :


    if slot >= 0 and slot < 6 :
        GPIO.setwarnings(False)
        # GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(module[slot], GPIO.OUT)
        servo = GPIO.PWM(module[slot], 50)
        servo.start(12)
        try :
            servo.ChangeDutyCycle(9.0)
            time.sleep(0.5)
            servo.ChangeDutyCycle(12.5)
            time.sleep(1)

            servo.stop()
            GPIO.cleanup()
            return "true"
        except :
            servo.stop()
            GPIO.cleanup()
            return "false"
    else :
        return "algument_error"

