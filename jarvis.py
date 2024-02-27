import pyttsx3
import spech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',150)

def speak(audio):
    engine.say(audio)
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recogniser
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try: 
        print("Reconizing...") 
        query = r.recoognize_google(audio,language='en-in')
        print(f("User said:{querry}\n"))

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query               
if __name__== "_main_"
    while True:
        query = takeCommand().lower()
        if 'jarvis'in query :
            print(" yes sir")
            speak("yes sir") 
