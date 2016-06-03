import os
import signal

from time import sleep
from subprocess import Popen, PIPE, STDOUT, check_output
from gpiozero import LED

led = LED(4)
scanCommand = "hcitool lescan"
connectCommand = "hcitool lecc FE:ED:BA:BE:BE:EF"
monitorCommand = "sudo btmon"

def ListenForDisconnect():
	proc = Popen(monitorCommand.split(), stdout=PIPE, stderr=STDOUT, bufsize=1, universal_newlines=True)

	while proc.poll() is None:
		print 'Reading output from monitor...'
		sleep(1)
		output = proc.stdout.read(1)
		print "Read Line: ",output
		if "Disconnect" in output:
			return True

	print 'Process is not running'
	return False

while True:
	led.on()
	print "Start Scan"
	process = Popen(scanCommand.split(), stdout=PIPE)

	sleep(1)
	print "End Scan"

	os.kill(process.pid, signal.SIGINT)
	output = process.communicate()[0]

	if("Pulse-Test-0" in output):
		print "Located Pulse! \nRestarting validation process in 5 seconds..."
		sleep(5)


	led.off()
	sleep(1)
	os.system('clear')
	


