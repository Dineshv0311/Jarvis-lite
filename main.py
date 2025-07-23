from modules.tts import speak
from modules.commands import handle_command
import speech_recognition as sr 
import wikipedia
from modules.ai import ask_ai

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting.")
        return ""

def main():
    while True:
        command = listen()
        if command:
            response = handle_command(command)
            if response:
                speak(response)
            if 'exit' in command or 'stop' in command:
                break

if __name__ == "__main__":

    # Welcome Message
    speak("Hello, this is Jarvis, how can I help you sir?")
    
    # Now enter the main assistant loop
    main()
