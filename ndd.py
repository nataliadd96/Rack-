from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on(3)
    sleep(1)
    led.off()
    sleep(2)