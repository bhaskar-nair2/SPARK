import speech_recognition as sr
import pyttsx
import os
import time

r = sr.Recognizer()
m=sr.Microphone()
flag=0

engine = pyttsx.init()

engine.say('Welcome Back Sir')

engine.say('How are You?')
engine.runAndWait()



with m as source:
    audio = r.listen(source)
    try:
        voice=r.recognize_google(audio)       
    except sr.UnknownValueError:
        flag=1
        engine.say("Hmmm..")
        engine.runAndWait()
    except sr.RequestError:
        flag=2
        engine.say("Could not connect")
        engine.runAndWait()
    except WaitTimeoutError:
        flag=3
        engine.say("Hmmm..")
        
if flag==0:
    if voice=="I am fine":
        engine.say("Very well sir")
        engine.runAndWait()
    
    elif voice=="I m not feeling well":
        engine.say("How can I help you?")
        engine.runAndWait()

    
    elif voice=="Hi":
        engine.say("Hi")
        engine.runAndWait()

    else:
        engine.say("Hmmm..")
        engine.runAndWait()

else:
    engine.say("Hmmm..")
    engine.runAndWait()
x=2 
def callback(recognizer, audio):
    
    try:
        recognizer.recognize_google(audio)
        x=0
    except sr.UnknownValueError:
        engine.say("Excuse me!")
        x=1
    except sr.RequestError as e:
        engine.say("Unable to conect!")
        x=1

       
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)
    if x==0:
            
        if recognizer.recognize_google(audio) =="Wake up":
            os.startfile("try2.py")

stop_listening = r.listen_in_background(m, callback)



import time
for _ in range(50): time.sleep(0.1) 
while True: time.sleep(0.1)

#add functionality to serch for negetive and positive responses
#group in for multiple responses
#use inbuilt api insted of google voice recognition
