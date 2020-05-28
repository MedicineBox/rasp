# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import os, ntpath
import json
import subprocess
import RPi.GPIO as GPIO
import time
from dosing import dosing

app = Flask(__name__)


# def dosing(slot) :
#     GPIO.setwarnings(False)
#     servolist = [6, 5, 12, 7, 8, 25]
#     GPIO.setmode(GPIO.BCM)
#     GPIO.setup(servolist[slot], GPIO.OUT)
#     servo = GPIO.PWM(servolist[slot], 50)
#     servo.start(12)

#     if slot >= 0 & slot < 6 :
#         try :
#             servo.ChangeDutyCycle(9.0)
#             time.sleep(0.5)
#             servo.ChangeDutyCycle(12.5)
#             time.sleep(1)

#             servo.stop()
#             GPIO.cleanup()
#             return "true"
#         # except KeyboardInterrupt :
#         #     servo.stop()
#         #     GPIO.cleanup()

#         except :
#             servo.stop()
#             GPIO.cleanup()
#             return "false"


@app.route('/api/dosing', methods = ['POST'])
def dosingApp():
    data = request.json
    slot = int(data['slot'])
    print (slot)
    result = dosing(slot)
    if(result == "true"):
        return "true"
    elif(result == "algument_error") :
        return "Check slot number!"
    else :
        return "Fail to Dosing!" 

    # return result

if __name__=='__main__':
    app.run(host='0.0.0.0', port=60002, debug=True)

