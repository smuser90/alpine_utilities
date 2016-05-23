var sp = require("serialport");
var SerialPort = sp.SerialPort;
var serialPort = new SerialPort("/dev/tty.usbmodem14631", {
  baudrate: 115200,
  parser: sp.parsers.readline("\n")
  },
false);

serialPort.open(function (error) {
  if ( error ) {
    console.log('failed to open: '+error);
  } else {
    console.log('open');
    serialPort.on('data', function(data) {
      //console.log('data received: ' + data);
      if(data.includes('TL_StartPhoto')){
        console.log("Photo capture initiated at "+Date.now());
      }
      if(data.includes('tl_StopPhoto')){
        console.log("Photo capture completed at "+Date.now());
      }
    });
    serialPort.write("a", function(err, results) {
      console.log('err ' + err);
      console.log('results ' + results);
    });
  }
});
