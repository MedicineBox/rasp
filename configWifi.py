import RPi.GPIO as GPIO
import time
import requests 
import json
import subprocess
import os
import sys

BUTTON = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
flag = 0
longpush = 0
device_id = subprocess.check_output("script/device_info", shell=True)
device_id = device_id.replace("\n", "")


apiUrl = 'http://ec2-3-34-54-94.ap-northeast-2.compute.amazonaws.com:65004/wifi'
deviceInfo = {"device_id" : device_id }
print "device_id : ", device_id
 

def getWifiInfo() :
    res = requests.get(url=apiUrl+"?device_id="+device_id,  
        headers={"Content-Type" : "application/json"})
    if res.status_code == 200 :
        return res.json()[0]

def deleteServerWifiInfo() :
    res = requests.delete(url=apiUrl, json=deviceInfo, 
        headers={"Content-Type" : "application/json"})
    if res.status_code == 200 :
        print(res.text)
        return res.text

try :
    print "push BUTTON double tap or long push"
    while True:
        if GPIO.input(BUTTON) != True:
            print("Pushed!!!")
            if flag == 0 or flag == 2:
                flag += 1
            longpush += 1
        elif flag == 1 :
            flag += 1


        if longpush >= 15 :
            print("Long Pushed!!!")      
            break
        if flag == 3 :
            print("Double tapped!!")
            break
        
        time.sleep(0.2)

    if longpush >= 15 :
        print("NETWORK INITIALIZATION!!!")
        os.system("script/init_wifi.sh")
        print("NETWORK RESTART!!!")
        os.system("script/network_restart.sh")
        longpush = 0
        flag = 0
    
    elif flag == 3 :
        wifiData = getWifiInfo()
        wifi_id = wifiData['wifi_id']
        wifi_pw = wifiData['wifi_pw']
        command = "script/configure_wifi.sh \'" + wifi_id + "\' \'" + wifi_pw + "\'"
        print command
        subprocess.call("script/configure_wifi.sh \"" + wifi_id + "\" \"" + wifi_pw + "\"", shell=True)
        network_state = subprocess.check_output("script/network_check_state.sh", shell=True)
        print "network connected to : " + network_state
        longpush = 0
        flag = 0
        loopNum = 0
        while True :
            if network_state != "off/any\n" :
                result = deleteServerWifiInfo()
                print result
                break
            else :
                print "Not Connected yet.."
                network_state = subprocess.check_output("script/network_check_state.sh", shell=True)
                time.sleep(3)
                if loopNum > 20 :
                    print "ERROR: CAN'T NOT CONNECT TO ",wifi_id
                    break
                loopNum = loopNum + 1
        network_state = ""
        
except KeyboardInterrupt :
    GPIO.cleanup()
