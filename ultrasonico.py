import time #se necesita para usar las funciones de tiempo
from subprocess import call #la necesitamos para la interrupcion de teclado
import RPi.GPIO as GPIO
import numpy as np

#---------------------------------------------------------------
try:
    import pyttsx

    engine = pyttsx.init()

    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume-0.25)
    engine.setProperty('rate', rate-50)
    voices = engine.getProperty('voices')
    engine.setProperty('voice','spanish-latin-am')
except:
    print "Error in tts"

#---------------------------------------------------------------

 
# GPIO.setmode(GPIO.BOARD) #Queremos usar la numeracion de la placa

out_data = list()
out_data.append('distance[cm]')
GPIO.setmode(GPIO.BCM) 
  
  #Definimos los dos pines del sensor que hemos conectado: Trigger y Echo
Trig = 23
Echo = 24
   
   #Hay que configurar ambos pines del HC-SR04
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)
    
def Ultrasonic():
        GPIO.output(Trig, GPIO.LOW)

        #time.sleep(2*10**-6) #esperamos dos microsegundos
        time.sleep(2) 
        GPIO.output(Trig, True) #encendemos el pin Trig
        time.sleep(0.00001) #esperamos diez microsegundos
        GPIO.output(Trig, GPIO.LOW)

        print 'Echo:',Echo
        
        while True:
            start = time.time()
            if GPIO.input(Echo) == GPIO.HIGH:
                break

        while True:
            end = time.time()
            if GPIO.input(Echo) == GPIO.LOW:
                break


                
        #print "Time ", start,end
        duracion = end-start
        distance = duracion*34300/2
        out_data.append(distance)   


        print "Distance %.2f [cm]" %distance

        if distance<10:
            try:
                engine.say(str(distance))
                engine.runAndWait()
            except:
                print "Error in ttsx"





while True:
        try:
            Ultrasonic()

        except KeyboardInterrupt:
            print ' Exiting'
            break

        #por ultimo hay que restablecer los pines GPIO
print "Cleaning"
GPIO.cleanup()       
print 'Saving DB ultra.csv'
np.savetxt('ultra.csv', (out_data), ['%s\t'],delimiter=',')

