#sudo pip3 install Adafruit_DHT

import Adafruit_DHT as dht
from time import sleep as t
sensor = dht.DHT22
pin = 21
while 1:
    humedad, temperatura =dht.read_retry(sensor, pin)
    if humedad is not None and temperatura is not None:
        print("""temp={0}°C
humedad={1}%""".format(temperatura, humedad))
    t(3)
 