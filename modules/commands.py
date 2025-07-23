from modules.tts import speak
import pywhatkit
import datetime
import pyjokes
import webbrowser
import wikipedia
import random
from modules.ai import ask_ai


def handle_command(command):
    if 'play' in command:
        song = command.replace('play', '').strip()
        pywhatkit.playonyt(song)
        return f"Playing {song} on YouTube."
    
    elif 'who is' in command or 'what is' in command or 'tell me about' in command:
        try:
            # Clean the command
            if 'tell me about' in command:
                topic = command.replace('tell me about', '').strip()
            elif 'who is' in command:
                topic = command.replace('who is', '').strip()
            elif 'what is' in command:
                topic = command.replace('what is', '').strip()
            else:
                topic = command

            # Get summary from Wikipedia
            summary = wikipedia.summary(topic, sentences=2)
            return summary
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Your query is too broad. Be more specific, like: {e.options[0]}"
        except wikipedia.exceptions.PageError:
            return "Sorry, I couldn't find anything on that topic."

    elif 'time' in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        return f"The current time is {time_now}."

    elif 'joke' in command:
        return pyjokes.get_joke()

    elif 'search' in command:
        search_query = command.replace('search', '').strip()
        pywhatkit.search(search_query)
        return f"Searching {search_query} on Google."

    elif 'open google' in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."
    
    

    elif 'exit' in command or 'stop' in command:
        return "Goodbye. Shutting down."
    
    
    else:
        response = ask_ai(command)
        speak(response)