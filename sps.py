import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the default microphone
with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said: {}".format(text))
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech API; {0}".format(e))
