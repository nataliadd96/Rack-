from w1thermsensor import W1ThermSensor
from time import sleep
import requests

while 1:
    sensor = W1ThermSensor()
    temperatura = int(sensor.get_temperature())
    requests.get("https://api.thingspeak.com/update?api_key=P6OA7ICN48CRGC3W&field1="+str(temperatura))
    

