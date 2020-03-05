from influxdb import InfluxDBClient as influx
import Adafruit_DHT
from time import sleep as t
sensor = Adafruit_DHT.DHT22
pin = '21'
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
cliente = influx(database='rack')
def dht22():
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        dh=[]
        dh1=[]
        dh.append("dht22,tag=22 temp={}".format(temperature))
        cliente.write_points(dh, database='rack', time_precision='s', protocol='line')
        dh1.append("dht22,tag=23 temp={}".format(humidity))
        cliente.write_points(dh1, database='rack', time_precision='s', protocol='line')
    else:
        print('Failed to get reading. Try again!')
    

    
while 1:
    dht22()
    t(2)