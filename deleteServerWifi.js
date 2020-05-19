const request = require('request');

var deviceInfo = {"device_id" : "a0001"}
var deleteurl = 'http://ec2-3-34-54-94.ap-northeast-2.compute.amazonaws.com:65004/wifi';

request.delete(
    {url: deleteurl,
        headers:{"Content-Type" : "application/json"},
        body: deviceInfo,
        json: true
    }, 
    function (error, res, body) {
        console.log("received data : " + JSON.stringify(body));
        console.log("received type : " + typeof(body));
        var result = body;
        if(!error && res.statusCode == 200) {
            console.log("DELETE 서버로부터 수신했음!");
            console.log("DELETE 결과 : " + result);
        }
    }
);


