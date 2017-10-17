import pyttsx3 as py

engine=py.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
engine.setProperty('rate',130)
def spk(st):
    engine.say(st)
    engine.runAndWait()



