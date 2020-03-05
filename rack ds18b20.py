from w1thermsensor import W1ThermSensor as ds 
from time import sleep as t

while 1:
    ds18b20()   
    t(0.5)


def ds18b20():
    s1 = ds(ds.THERM_SENSOR_DS18B20,"030897943b31")
    t1 = int(s1.get_temperature())
    s2 = ds(ds.THERM_SENSOR_DS18B20,"03ff979418c9")
    t2 = int(s2.get_temperature())
    s3 = ds(ds.THERM_SENSOR_DS18B20,"0417c45487ff")
    t3 = int(s3.get_temperature())
    print("sensor1 {} C  sensor2 {} C sensor3 {} C".format(t1,t2,t3))
    return t1,t2,t3


