from gpiozero import LEDBoard
from time import sleep
a=0.5

leds = LEDBoard(5, 6, 13, 19, 26, pwm=True)

while True:
    leds.value = ( 1, 1, 1, 1)
    sleep(1)
    leds.value = ( 0, 0, 0, 0)
    sleep(1)
