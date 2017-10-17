import speech_recognition as sr
from playsound import playsound

r = sr.Recognizer()
m = sr.Microphone()

def energy():
    try:
        with m as source: r.adjust_for_ambient_noise(source)            
    except KeyboardInterrupt:
        pass
def recd():
        playsound("./Media/robo-beep.mp3")
        with m as source: audio = r.listen(source,10,8)
        playsound("./Media/robo2-beep.mp3")
        try:
            # recognize speech using Google Speech Recognition and not Google Cloud Recognition
            value = r.recognize_google(audio,"AIzaSyB9vh6DE_Dz-oMHutVn__G2EPc3PtzlPZ0")##Custom API key GIVEN!!!
            ##print("You said {}".format(value))
            return value
            ##We are giving output from here
        except sr.UnknownValueError:
            return "Err-1"
            
        except sr.RequestError as e:
            return "Err-2"
            playsound("./Media/beep-10.mp3")

