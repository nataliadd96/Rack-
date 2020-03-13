from gpiozero import LED
from time import sleep as t
led= LED(12)


led.off()
t(1)
led.on()
t(1)