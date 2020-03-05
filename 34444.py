from gpiozero import LED
from time import sleep as t 

led = LED(4)
led = LED(6)

while 1:
    print(led.is_lit)
    led.on()
    t(10)
    print(led.is_lit)
    led.off()
    t(10)
