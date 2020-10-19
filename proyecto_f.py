from influxdb import InfluxDBClient as influx
import requests as rq
from time import sleep
import json
cliente = influx(database='PACIENTE')
while 1:
    h=rq.get("https://api.thingspeak.com/channels/1191468/fields/1.json?api_key=3AC5EMFTJ4ZDXNFD&results=2")//OBTENER DATOS DE THINGSPEACK
    j=json.loads(h.content)
    temperatura=j["feeds"][1]["field1"]
    print(temperatura)
    
    data = []
    data.append("sensor,tag=0 lm35={}".format(temperatura))
    cliente.write_points(data, database='PACIENTE', time_precision='s', protocol='line')
    
    r = requests.get('https://maker.ifttt.com/trigger/sensor/with/key/cilbQn9_ISfxSloSJd2qe0PBo-kAtx0HCw1cjOo2c8B', params={"value1":temperatura})
    sleep(30)
