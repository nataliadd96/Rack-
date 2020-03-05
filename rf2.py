import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
try:
        text = input('Nesw data:')
        print("Now plassce your tag to write")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()