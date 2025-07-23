import pyttsx3

def speak(text):
    print(f"Jarvis: {text}")  # Debugging print
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Female voice, change index if needed
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"[ERROR in speak()] {e}")
