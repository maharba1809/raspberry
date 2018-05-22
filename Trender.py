#!/usr/bin/python
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime



import math
import sys
import csv
import pandas as pd

class DsCase:

    def __init__(self, folder):
        self.folder = folder
                
    def readCase(self):
        try:
            print(self.folder)
            #csv = np.loadtxt( self.folder, skiprows=0)
            csv   = pd.read_csv(self.folder)
            
        except ValueError:   
            print "That was no valid path.  Try again..."
        self.mydate = csv['datetime'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f'))            
        self.tamb = csv['tamb']
        self.hum = csv['hum']
            
    def calculations(self): 
        print('calculating')
        
        
        #------------------------------------------------------------------------------

    def plotCase(self):
        title_plot = "Schlafzimmer 21 May 2018, sensor DHT11"     
        
        #plt.figure(1)   
        #plt.subplot(311)
        #plt.plot(self.datetime, self.tamb)
#        

        #plt.title(title_plot, fontsize=15, color= "gray")
        #plt.xlabel("time")
        #plt.ylabel("Temperature degC")

        #plt.subplot(312)
        #plt.plot(self.datetime, self.hum, color = 'green')
        #plt.xlabel('Time')
        #plt.ylabel('Humidity')
        
        #plt.show() 
        
        fig, (ax,ax2) = plt.subplots(2,1)
        #fig.subplots_adjust(left=0.1, wspace=0.1)
        np.random.seed(19680801)
        ax.plot(self.mydate, self.tamb,color = 'red')
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
        _=plt.xticks(rotation=90)    
        ax.grid(True)
        ax.set_xlabel('time')
        ax.set_ylabel('Temperature degC')


        ax2.plot(self.mydate, self.hum,color = 'blue')
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

p = DsCase('dht11.csv')
p.readCase()
p.plotCase()
