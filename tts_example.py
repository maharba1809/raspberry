import pyttsx
engine = pyttsx.init()

#engine.say('Sally sells seashells by the seashore.')
#engine.say('1 2 3.5')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.25)


engine.setProperty('rate', rate-50)



voices = engine.getProperty('voices')
engine.setProperty('voice','spanish-latin-am')
engine.say('23')

#for i in voices:
#       print(i)
engine.runAndWait()

