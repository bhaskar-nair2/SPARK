#IMPORTS
import speech_recognition as sr
import pyttsx
import os
import time
import urllib2 as ul
import functions

#global VAriABLES
r=sr.Recognizer()
m=sr.Microphone()
flag=0
flagNet=False #false means offline
statCheck=False #false means check not performed yet or Recheck is on
unknowErr=False #false means no error
reqErr=False #false means no error
timeErr=False #false means no error
voiceRec=False #false means not recieved
errType=0
voice="not Defined"
engine=pyttsx.init()
spk=functions.speaker()
nt=functions.net()
ln=functions.listen()

#Function DEFINATIONS
  
#MAin Structure
spk.speak('Welcome back sir')
   

#Define if we r online of offline
while flagNet==False:
    if nt.netCheck():
        spk.speak("We are online")
        flagNet=True
        statCheck=False
    else:
        if statCheck==False:
            
            spk.speak("We are offline Sir, I'll have to be on stand by")
            statCheck=True
        time.sleep(5)
        
#now we start listening
    while flagNet==True:
        try:
            voice=ln.voice()
            voiceRec=True
        except sr.UnknownValueError:
            print "err 1"
            errType=1
            voiceRec=False
            pass
        except sr.RequestError:
            print "err 2"
            errType=2
            voiceRec=False
            pass
        except ul.URLError:
            print "err 2"
            errType=2
            voiceRec=False
            pass
        except sr.WaitTimeoutError:
            print "err3"
            errType=3
            voiceRec=False
            pass
        if voiceRec==True:
            print ("You said {}".format(voice).encode("utf-8"))
            spk.speak("You said {}".format(voice).encode("utf-8"))
        elif errType==2:
            flagNet=nt.netCheck()
                 

