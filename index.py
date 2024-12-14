import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to listen to the user's command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print(
                "Could not request results from Google Speech Recognition service.")
            return ""


# Function to tell the current time
def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    speak(f"The current time is {current_time}")


# Function to set a reminder
def set_reminder(reminder):
    speak(f"Reminder set for {reminder}")


# Function to search the web
def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Searching the web for {query}")


# Main function to run the voice assistant
def main():
    speak("Hello! I am your voice assistant. How can I help you today?")

    while True:
        command = listen()

        if "time" in command:
            tell_time()

        elif "remind me to" in command:
            reminder = command.replace("remind me to", "").strip()
            set_reminder(reminder)

        elif "search" in command:
            query = command.replace("search", "").strip()
            search_web(query)

        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

        else:
            speak(
                "I can help you with telling the time, setting reminders, or searching the web.")


if __name__ == "__main__":
    main()
