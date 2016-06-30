from time import sleep
from gpiozero import LED
import sys

led = LED(4)
duration = sys.argv[1]

led.on()

sleep(float(duration))

led.off()
