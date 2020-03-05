from w1thermsensor import W1ThermSensor
from time import sleep
import requests
while 1:
    sensor = W1ThermSensor()
    temperatura = int(sensor.get_temperature())
    if temperatura>30:
        requests.get(https://maker.ifttt.com/trigger/temp/with/key/cwbxuhMuF3jRywplziNM7c",params={"value1":temperatura,"value2":"none","value3":"none"})           
        sleep(5)
    print(temperatura)
    sleep(1)