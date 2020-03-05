from gpiozero import LED
led = LED(6)
led.blink(0.5,0.5,5)