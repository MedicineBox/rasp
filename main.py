from flask import request
# from flask_restful import Resource, Api
from flask_api import FlaskAPI
import RPi.GPIO as GPIO
# from dosing import Dosing
import time

# app = Flask(__name__)
# api = Api(app)

# api.add_resource(Dosing, 0)

module = [6, 5, 12, 7, 8, 25]
app = FlaskAPI(__name__)

class Dosing(let slot) :
    GPIO.setwarnings(False)
    # GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(module[slot], GPIO.OUT)
    servo = GPIO.PWM(module[slot], 50)
    servo.start(12)

    if slot != -1 :
        try :
            servo.ChangeDutyCycle(9.0)
            time.sleep(0.5)
            servo.ChangeDutyCycle(12.5)
            time.sleep(0.5)

        except KeyboardInterrupt :
            servo.stop()
            GPIO.cleanup()



@app.route('/', methods=["GET"])
def api_root() :
    return {
        "servo_url": request.url
    }

@app.route('/servo', methods=["POST"])
def api_servo() :
    Dosing(0)
    return {"SUCCESS"}


if __name__ == "__main__" :
    app.run()


