from gpiozero import LED
from time import sleep

led = LED(18) 

while True:
        led.on()

