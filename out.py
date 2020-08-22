import userInput
import wikipedia
import speak

def out():
    query = userInput.userInput().lower()
    print("User said: "+query)
    results = wikipedia.summary(query, sentences = 3)
    print(results)
    speak.speak("Wikipedia said: ")
    speak.speak(results)
    