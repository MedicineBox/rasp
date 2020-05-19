const request = require('request');


var deviceInfo = {"device_id" : "a0001"}
var geturl = 'http://ec2-3-34-54-94.ap-northeast-2.compute.amazonaws.com:65004/wifi';


request.get(
    {url: geturl,
        headers:{"Content-Type" : "application/json"},
        body: deviceInfo,
        json: true
    },
    function (error, res, body) {
        console.log("received data : " + JSON.stringify(body));
        console.log("received type : " + typeof(body));
        var data = JSON.parse(JSON.stringify(body));
        if(!error && res.statusCode == 200) {
            console.log("GET 서버로부터 수신했음!");
            console.log("Wifi_id : " + data[0].wifi_id);
            console.log("wifi_pw : " + data[0].wifi_pw);
        }
    }
);









