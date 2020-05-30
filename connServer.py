import requests 
import json
import subprocess




device_id = subprocess.check_output("script/device_info", shell=True)
device_id = device_id.replace("\n", "")

apiUrl = 'http://ec2-3-34-54-94.ap-northeast-2.compute.amazonaws.com:65004'
deviceInfo = {"device_id" : device_id }
# print "device_id : ", device_id

def sendServer(param, sendJson) :
    requestUrl = "/".join([apiUrl, param])
    res = requests.post(url=requestUrl, json=sendJson, 
        headers={"Content-Type" : "application/json"})
    if res.status_code == 200 :
        print(res.text)
        return res.text
    print requestUrl




# sendServer("test", "asd")
