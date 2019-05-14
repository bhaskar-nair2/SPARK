import listen as ls
# import Head
import speak as sp
import threading as th
from playsound import playsound
import functions as fn

sp.spk("Voice, Ready")
ls.energy()
sp.spk("System, Ready")
words = []
voice = ""


def lis():
    voice = ls.recd()
    if (voice == "Err-1"):
        playsound("./Media/beep-10.mp3")
        sp.spk("Couldn't get that")
    elif (voice == 'Err-2'):
        playsound("./Media/beep-10.mp3")
        sp.spk("Connection to Google Broken")
    else:
        words = voice.split(' ')
        fn.search(words[0], words[1])


def extract(words):
    print(words)


lis()

# threads=[]
# for i in range(5):
#    t= th.Thread(target=lis)
# threads.append(t)
# t.start()
