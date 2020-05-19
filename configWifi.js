const gpio = require('node-wiring-pi');
const BUTTON = 29;

const initWifi = function() {
    let data = gpio.digitalRead(BUTTON);
    if(!data) 
        console.log("Node js : Button was pressed!");
    setTimeout(initWifi, 300);
}


process.on('SIGINT', function() {
    console.log("Program Exit...");
    process.exit();
});

gpio.setup('wpi');
gpio.pinMode(BUTTON, gpio.INPUT);
setImmediate(initWifi);