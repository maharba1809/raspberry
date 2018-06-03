#!/usr/bin/python
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import os





import math
import sys
import csv
import pandas as pd
import os.path

class DsCase:

    def __init__(self, folder):
        self.folder = folder
                
    def readCase(self):
        try:
            print(self.folder)
            
            if os.path.isfile(self.folder):
                csv   = pd.read_csv(self.folder)
                self.mydate = csv['datetime'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f'))            
                self.tamb = csv['tamb']
                self.hum = csv['hum']
            else:            
                print('file does not exist')
                print('connecting to remote file instead...')
#                ssh = paramiko.SSHClient()
 #               ssh.connect('192.168.0.10', username='pi', password='')
  #              ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('scp pi@192.168.0.10:/home/pi/scripts/dht11/dht11.csv /home/maxwell/codes/raspberry/dht11/')

                quit() 
            
        except ValueError:
            print "parsing error in input"
            
        
            
    def calculations(self): 
        print('calculating')
        self.rolltamb = self.tamb.rolling(window=10,center=False).mean()
        self.rollhum = self.hum.rolling(window=10,center=False).mean()

        
        
        #------------------------------------------------------------------------------

    def plotCase(self):
        
        fig, (ax,ax2) = plt.subplots(2,1)
        
        #fig.subplots_adjust(left=0.1, wspace=0.1)
        np.random.seed(19680801)
        
        ax.plot_date(self.mydate, self.tamb,color = 'red', alpha = 0.2, marker = 'o')
        ax.plot(self.mydate, self.rolltamb,color = 'red')
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
        _=plt.xticks(rotation=90)    
        ax.grid(True)
        ax.set_xlabel('time')
        ax.set_ylabel('Temperature degC')
        plt.title('Bedroom Sensor DHT11', fontsize=20, color = 'gray',y = 2.3)        
        #ax2.plot(self.mydate, self.hum,color = 'blue',)
        ax2.plot_date(self.mydate, self.hum, color = 'blue', alpha = 0.2, marker = 's')
        ax2.plot(self.mydate, self.rollhum,color = 'blue')
        ax2.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
        #ax.xaxis.set_minor_formatter(mdates.DateFormatter('%M'))
        _=plt.xticks(rotation=90)    
        ax2.grid(True)
        ax2.set_xlabel('time')
        ax2.set_ylabel('Humidity')

        plt.show()

 

    def writeCase(self,outName):            
             
        print("Writing complete")
# # Hint: skiprows = 800 - 950
    def merge(self):
        global tb
        d = {'CASE' : [self.case],'dt' : [self.time],'N' : [self.Humidity], 'L' : [self.Temperature] }
                 
        df = pd.DataFrame(data = d)
        tb = tb.append( df )  
    
        
#tb = pd.DataFrame()
os.chdir('/home/maxwell/codes/raspberry/dht11')

p = DsCase('dht11.csv')
p.readCase()
p.calculations()
p.plotCase()
