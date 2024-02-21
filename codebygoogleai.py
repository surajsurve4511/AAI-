import speech_recognition as sr
import webbrowser
import pyttsx3

# Create a speech recognition object
r = sr.Recognizer()

# Create a pyttsx3 object to control the text-to-speech engine
engine = pyttsx3.init()

# Define the function to listen to the user's voice and convert it to text
def listen_and_convert_to_text():
    # Prompt the user to speak
    print("Speak now:")

    # Record the user's voice
    with sr.Microphone() as source:
        audio = r.listen(source)

    # Recognize the user's voice
    try:
        text = r.recognize_google(audio)
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
    except sr.UnknownValueError:
        print("Could not understand the audio")

    # Return the recognized text
    return text

# Define the function to search the web for the user's query
def search_the_web(query):
    # Create a webbrowser object
    browser = webbrowser.Chrome()

    # Search the web for the user's query
    browser.open("https://www.google.com/search?q=" + query)

# Define the function to read the search results aloud
def read_the_search_results():
    # Get the search results from the web
    results = browser.get_element_by_id("search")

    # Read the search results aloud
    for result in results:
        engine.say(result.text)

# Main function
def main():
    # Listen to the user's voice and convert it to text
    text = listen_and_convert_to_text()

    # Search the web for the user's query
    search_the_web(text)

    # Read the search results aloud
    read_the_search_results()

# Call the main function
if __name__ == "__main__":
    main()mport speech_recognition as sr
import webbrowser
import pyttsx3

# Create a speech recognition object
r = sr.Recognizer()

# Create a pyttsx3 object to control the text-to-speech engine
engine = pyttsx3.init()

# Define the function to listen to the user's voice and convert it to text
def listen_and_convert_to_text():
    # Prompt the user to speak
    print("Speak now:")

    # Record the user's voice
    with sr.Microphone() as source:
        audio = r.listen(source)

    # Recognize the user's voice
    try:
        text = r.recognize_google(audio)
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
    except sr.UnknownValueError:
        print("Could not understand the audio")

    # Return the recognized text
    return text

# Define the function to search the web for the user's query
def search_the_web(query):
    # Create a webbrowser object
    browser = webbrowser.Chrome()

    # Search the web for the user's query
    browser.open("https://www.google.com/search?q=" + query)

# Define the function to read the search results aloud
def read_the_search_results():
    # Get the search results from the web
    results = browser.get_element_by_id("search")

    # Read the search results aloud
    for result in results:
        engine.say(result.text)

# Main function
def main():
    # Listen to the user's voice and convert it to text
    text = listen_and_convert_to_text()

    # Search the web for the user's query
    search_the_web(text)

    # Read the search results aloud
    read_the_search_results()

# Call the main function
if __name__ == "__main__":
    main()
""" To  run this code run this command in command prompt """
""" <span class="markdown-code-block-delimiter">```</span>python program.py<span class="markdown-code-block-delimiter">```</span>"""