import RPi.GPIO as GPIO
import time


def dosing(accept) :
    GPIO.setwarnings(False)
    module = [6, 5, 12, 7, 8, 25]
    # GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(module[accept], GPIO.OUT)
    servo = GPIO.PWM(module[accept], 50)
    servo.start(12)

    if accept >= 0 & accept < 6 :
        try :
            servo.ChangeDutyCycle(9.0)
            time.sleep(0.5)
            servo.ChangeDutyCycle(12.5)
            time.sleep(0.5)

            servo.stop()
            GPIO.cleanup()
            return True
        except KeyboardInterrupt :
            servo.stop()
            GPIO.cleanup()

        except :
            servo.stop()
            GPIO.cleanup()
            return False

dosing(0)