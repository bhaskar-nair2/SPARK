#imports
import urllib2
import speech_recognition as sr
import pyttsx
import os
import time
import urllib2 as ul

#global Variables
engine=pyttsx.init()
#global VAriABLES
r=sr.Recognizer()
m=sr.Microphone()
flag=0
flagNet=False #false means offline
statCheck=False #false means check not performed yet or Recheck is on
st=["",""]

#functions
class net():
    def netCheck(self): #checks if net is connected
        try:
            check=urllib2.urlopen('http://www.google.com',timeout=1)
            return True
        except urllib2.URLError as er: pass
        return False

def uvError(typ):
    return typ
class listen():
    def voice(self): #record Recognize and give back audio
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as ob:
            r.adjust_for_ambient_noise(ob)

        try:
        
            with m as source:
              
                while True:
                    try:
                        audio = r.listen(source,3)
                    except sr.WaitTimeoutError:
                        raise sr.WaitTimeoutError
                        uvError(3)
                        continue
                        pass            
                    
                    try:
                        if net().netCheck==False:
                            raise sr.RequestError
                            continue
                        
                        value = r.recognize_google(audio,key="AIzaSyB55R1xXklGJOGbYh_UpQ31MRWv_5LlG5c")


                        # we need some special handling here to correctly print unicode characters to standard output
                        if value is bytes:
                            return format(value).encode("utf-8")
                        else: 
                            return format(value)
                    except sr.UnknownValueError:
                        raise sr.UnknownValueError
                        uvError(1)
                        pass
                    except sr.RequestError:
                        raise sr.RequestError
                        pass
                    except ul.URLError:
                        raise ul.URLError
                        uvError(2)
                        pass
                    except AttributeError:
                        raise sr.RequestError
                        uvError(2)
                        pass
        except KeyboardInterrupt:
            pass


    def getKeyWords(self,st):

        waste=[""]
        for i in range(len(waste)):
            try:
                    st.pop(st.index(waste[i]))
            except ValueError:
                    pass
    
class speaker():
    def speak(self,stri):
        engine.say(stri)
        engine.runAndWait()


