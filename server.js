const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json())

app.post('/', function(req, res) {
    console.log("Server Data Received!!!")
})




app.listen(60002, () => {
    console.log('server listening on port 68002')
});