import sys
import time
import Adafruit_DHT
import datetime as dtt
import numpy as np
import matplotlib.pyplot as plt
from subprocess import call 
import pandas as pd

def dht_run(db_dht):
    time.sleep(60) 


    humidity, temperature = Adafruit_DHT.read_retry(11, 17)
    datetime = dtt.datetime.now()
    #print "Temp: {0:0.1f} C  Humidity: {1:0.1f} %".format(temperature, humidity),datetime

    data=pd.DataFrame( {'datetime':[datetime], 'tamb':[temperature], 'hum':[humidity]})
    print(data)

    db_dht = db_dht.append(data)
    #    plt.plot(temperature)
    #    plt.show()
    return db_dht




db_dht = pd.DataFrame(columns=['datetime','tamb','hum'])

while True:
    try:
        db_dht = dht_run(db_dht)

    except KeyboardInterrupt:
        if True:
            print 'writing db.csv'
            db_dht.to_csv('db.csv', sep=',')
            print 'Exiting dht'
            break

