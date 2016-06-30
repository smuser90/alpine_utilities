from time import sleep
from gpiozero import LED

led = LED(4)
duration = sys.argv[1]

led.on()

sleep(duration)

led.off()
