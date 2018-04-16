#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

my_data = genfromtxt('/home/pi/scripts/ultra.csv', delimiter=',')

#import urllib2
#response = urllib2.urlopen('http://192.168.0.10:8000/ultra.csv')
#my_data = response.read()

print(type(my_data))

plt.plot(my_data, 'r')
plt.show()

