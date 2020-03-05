from influxdb import InfluxDBClient as influx
import Adafruit_DHT as dht
from time import sleep as t
sensor = dht.DHT11
pin = 2
cliente = influx(database='dht11')
while 1:
    humedad, temperatura =dht.read_retry(sensor, pin)
    if humedad is not None and temperatura is not None:
        print("""temp={0}°C
humedad={1}%""".format(temperatura, humedad))
        data = []
        data.append("temperatura,tag1=2 temp={}".format(temperatura))
        data1 = []
        data1.append("humedad,tag2=2 hum={}".format(humedad))
        cliente.write_points(data, database='dht11', time_precision='s', protocol='line')
        cliente.write_points(data1, database='dht11', time_precision='s', protocol='line')    
    t(3)