
var port = process.argv[2];
var spLib = require('serialport')
var SerialPort = spLib.SerialPort;
var sp = new SerialPort("/dev/tty.usbmodem"+port, {
	baudrate: 115200,
	parser: spLib.parsers.readline("\n")
}, false);

sp.open(
	function(error){
		if(error)
			console.log("Failed to open serial port: "+error);
		else{
			sp.on('data', allocationListen);
		}
	}
);


function allocationListen(data){
	if(data.includes("Allocation")){
		console.log(data);
	}
}
