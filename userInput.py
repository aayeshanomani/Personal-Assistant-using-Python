import speech_recognition as sr
import pyaudio

def userInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now....")
        audio = r.listen(source)
        query = r.recognize_google(audio)
    return query