from gpiozero import LED
led = LED(18)
while 1:
    led.off()
    print ("h")