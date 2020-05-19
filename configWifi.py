import RPi.GPIO as GPIO
import time
import requests 
import json
import subprocess
import os

BUTTON = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
flag = 0
longpush = 0

apiUrl = 'http://ec2-3-34-54-94.ap-northeast-2.compute.amazonaws.com:65005/wifi'
deviceInfo = {"device_id" : "a0001"}

# def setWifi() :
    # result = os.system('ls -al | grep set*')
    # result = subprocess.check_output("ls -al | grep set*", shell=True)
    # print wifi_id
    # p = subprocess.Popen("script/configure_wifi.sh"+wifi_id+wifi_pw)
    # print result
    # print(result)

def getWifiInfo() :
    res = requests.get(url=apiUrl, json=deviceInfo, 
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
            # longpush = 0      
            break
        if flag == 3 :
            print("Double tapped!!")
            # flag = 0
            break
        
        time.sleep(0.2)

    if longpush >= 15 :
        print("NETWORK RESTART!!!")
        # subprocess.call(["script/network_restart.sh"])
        os.system("script/network_restart.sh")
        longpush = 0
        flag = 0
    
    elif flag == 3 :
        wifiData = getWifiInfo()
        wifi_id = wifiData['wifi_id']
        wifi_pw = wifiData['wifi_pw']
        subprocess.call("script/configure_wifi.sh " + wifi_id + " " + wifi_pw, shell=True)
        network_state = subprocess.check_output("script/network_check_state.sh", shell=True)
        print "network connected to : " + network_state
        longpush = 0
        flag = 0
        if network_state != "off/any" :
            result = deleteServerWifiInfo()
            print result

except KeyboardInterrupt :
    GPIO.cleanup()
