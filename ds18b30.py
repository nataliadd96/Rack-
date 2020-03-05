from w1thermsensor import W1ThermSensor as ds 
from time import sleep as t
from influxdb import InfluxDBClient as influx
from gpiozero import LED
i=1
m=1
led = LED(18)
cliente = influx(database='rack')

def ds18b20():
    s1 = ds(ds.THERM_SENSOR_DS18B20,"030897943b31")
    s2 = ds(ds.THERM_SENSOR_DS18B20,"03ff979418c9")
    s3 = ds(ds.THERM_SENSOR_DS18B20,"0417c45487ff")
    t3 = float(s1.get_temperature())
    t2 = float(s2.get_temperature())
    t1 = float(s3.get_temperature())
    data1=[]
    data2=[]
    data3=[]
    data1.append("ds18b20,tag=1 temp={}".format(t1))
    cliente.write_points(data1, database='rack', time_precision='s', protocol='line')
    data2.append("ds18b20,tag=2 temp={}".format(t2))
    cliente.write_points(data2, database='rack', time_precision='s', protocol='line') 
    data3.append("ds18b20,tag=3 temp={}".format(t3))
    cliente.write_points(data3, database='rack', time_precision='s', protocol='line')
    print("sensor1 {} C  sensor2 {} C sensor3 {} C".format(t1,t2,t3))
    return t1,t2,t3

def relay():
    global i,m
    i=i+1
    if i>30:
        m=m+1
        i=1
    if m<3:
        led.off()
    elif m==3 and i<15:
        led.on()
    else:
        m=1
    
    print("seg:{} min:{}".format(i,m))
while 1:
    relay()
    ds18b20()
    t(0.7)
    
   
    
