import speech_recognition as sr

def activate_speech_recognition(keyword="hello"):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print(f"Listening for activation keyword: '{keyword}'")
        audio_data = recognizer.listen(source)

    try:
        activation_phrase = recognizer.recognize_google(audio_data, key="YOUR_GOOGLE_API_KEY").lower()
        if keyword in activation_phrase:
          print(f"Activation keyword '{keyword}' detected. Listening for command...")
          process_command()
        else:
         print("Activation keyword not detected. Please try again.")
         activate_speech_recognition(keyword)

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio. Please try again.")
        activate_speech_recognition(keyword)
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")

def process_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for command...")
        audio_data = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio_data).lower()
        print(f"Command received: '{command}'")
        # Add your logic to process the command here

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio. Please try again.")
        process_command()
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")

if __name__ == "__main__":
    activate_speech_recognition()
