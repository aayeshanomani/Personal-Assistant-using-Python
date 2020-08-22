import pyttsx3

def speak(string):
    engine = pyttsx3.init()
    engine.say(string)
    engine.runAndWait()