import speech_recognition as sr
from playsound import playsound
import threading
import os
import time
r = sr.Recognizer()
m = sr.Microphone()
stack=[]
##class Audi:
##    def __init__(self,audio):
##        try:
##        # recognize speech using Google Speech Recognition and not Google Cloud Recognition
##            value = r.recognize_google(audio,"AIzaSyB9vh6DE_Dz-oMHutVn__G2EPc3PtzlPZ0")##Custom API key GIVEN!!!
##        ##print("You said {}".format(value))
##            print(value)
##        except sr.UnknownValueError:
##            return "Err-1"        
##        except sr.RequestError as e:
##            return "Err-2"
##        playsound("./Media/beep-10.mp3")
##        
def energy():
    try:
        with m as source: r.adjust_for_ambient_noise(source)            
    except KeyboardInterrupt:
        pass
def recd():
        playsound("./Media/robo-beep.mp3")
        with m as source: audio = r.listen(source,10,8)
        playsound("./Media/robo2-beep.mp3")

        stack.append(audio)
        
def translate(audio):
    try:
        # recognize speech using Google Speech Recognition and not Google Cloud Recognition
        value = r.recognize_google(audio,"AIzaSyB9vh6DE_Dz-oMHutVn__G2EPc3PtzlPZ0")##Custom API key GIVEN!!!
        ##print("You said {}".format(value))
        print(value)
    except sr.UnknownValueError:
        return "Err-1"        
    except sr.RequestError as e:
        return "Err-2"
        playsound("./Media/beep-10.mp3")

def callTranslate():
    if len(stack)!=0:
        translate(stack.pop(0))

class ass(threading.Thread):
    def run(self):
        for _ in range (20):
            recd()
class bs(threading.Thread):
    def run(self):
        while True:
            callTranslate()
energy()
t=ass()
q=bs()
t.start()
q.start()

        
