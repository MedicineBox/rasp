const http = require('http')
const url = require('url')
const fs = require('fs')
const querystring = require('querystring')

const server = http.createServer((req, res) => {

    console.log("URL: "+req.url);
    console.log("METHOD: "+req.method);
    console.log(req.headers);
    console.log(req.read);

    var uri = req.url;
    var query = url.parse(uri, true).query;             // get 방식에서 파라미터값 가져옴



    res.write('<html><body><h2>Its raspberryPi Server</h2>');
    res.write('<h1>'+query.val+'</h1>');

    if(req.method == 'POST') {                          // post 방식에서 파라미터 값 가져옴
        req.on('data', function(chuck) {
            var data = querystring.parse(chuck.toString());
            res.writeHead(200, {'Content-Type':'text/html'});
            res.write('<h1>'+val+'</h1>');
        });
    }

    res.write('</body></html>');

    res.end();
});

server.listen(3000);

