# Import required modules
import os
import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser

# Create engine for text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 175)

# Speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Take command from microphone
def take_command() -> str:
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, there was a problem with the speech service.")
            return ""

# Run assistant logic
def run_assistant():
    command = take_command()

    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif 'open notepad' in command:
        speak("Opening Notepad")
        os.system('notepad')

    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("http://youtube.com")

    elif 'hey siri' in command:
        query = command.replace("hey siri", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query}"
            speak(f"Searching for {query}")
            webbrowser.open(url)
        else:
            speak("I'm here to assist you")

    elif 'bye' in command or 'stop' in command:
        speak("Okay, bye bye. See you soon!")
        exit()

    else:
        speak("I'm here to assist you. Try saying something like 'open YouTube', 'open Notepad', or 'what's the time'.")

# Main function
if __name__ == "__main__":
    speak("Hey hi, Lahari. I'm here to assist you. Try saying something like 'open YouTube', 'open Notepad', or 'what's the time'.")
    while True:
        run_assistant()