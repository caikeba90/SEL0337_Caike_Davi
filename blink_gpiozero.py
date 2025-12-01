from gpiozero import LED
from time import sleep

led = LED(18) 

while True:
	led.on()
	print("LED on")
	sleep(1)
	led.off()
	print("LED off")
	sleep(1)
