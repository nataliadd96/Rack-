from w1thermsensor import W1ThermSensor
from time import sleep
import requests
while 1:
    sensor = W1ThermSensor()
    temperatura = int(sensor.get_temperature())
    sleep(1)
    requests.get("https://api.thingspeak.com/update?api_key=ZLIV2L5H504FXXTO&field1="+str(temperatura))

