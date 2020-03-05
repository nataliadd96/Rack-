from influxdb import InfluxDBClient as influx
import Adafruit_DHT as dht
from time import sleep as t
sensor = dht.DHT11
pin = 23
cliente = influx(database='dht11')
while 1:
    humedad, temperatura =dht.read_retry(sensor, pin)
    if humedad is not None and temperatura is not None:
        print("""temp={0}°C
humedad={1}%""".format(temperatura, humedad))
        data = []
        data.append("sensores,temperatura=100 y={}".format(temperatura))
        data1 = []
        data1.append("sensores,humedad=200 x={}".format(humedad))
        cliente.write_points(data, database='dht11', time_precision='s', protocol='line')
        cliente.write_points(data1, database='dht11', time_precision='s', protocol='line')    
    t(3)