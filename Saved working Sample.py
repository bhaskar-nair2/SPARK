import speech_recognition as sr
import speak as sp

r = sr.Recognizer()
m = sr.Microphone()


class rec:

    def recd():
        # key="AIzaSyB9vh6DE_Dz-oMHutVn__G2EPc3PtzlPZ0"
        try:
            print("A moment of silence, please...")
            with m as source:
                r.adjust_for_ambient_noise(source)
            print("Set \
                minimum energy threshold to {}".format(r.energy_threshold))
            # while True:
            print("Say something!")
            with m as source:
                audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_sphinx(audio)

                # this version of Python uses bytes for strings (Python 2)
                if str is bytes:
                    print(u"You said {}".format(value).encode("utf-8"))
                # this version of Python uses unicode for strings (Python 3+)
                else:
                    print("You said {}".format(value))
                    sp.spk.sayit("You said {}".format(value))
                    # We have to give output from here
            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print(
                    "Uh oh! Couldn't \
                        request results from Google Speech Recognition service; {0}".format(e))
        except KeyboardInterrupt:
            pass


rec.recd()
