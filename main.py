import speech_recognition as speech
import pyttsx3
import pyaudio
import pywhatkit
import datetime
import wikipedia


listener = speech.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with speech.Microphone() as source:
            print('Listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                talk(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('the current time is' + time)
    elif 'tell me about' in command:
        subject = command.replace('tell me about','')
    try:
        # Attempt to get the Wikipedia summary
        info = wikipedia.summary(subject, sentences=6)
        print(subject)  # For debugging
        talk(info)  # Speak the summary

    except wikipedia.exceptions.PageError:
        # Handle PageError exception
        suggestions = wikipedia.suggest(subject)
        if suggestions:
            talk("Could not find an exact match for '{}'. Here are some suggestions:".format(subject))
            for suggestion in suggestions:
                talk(suggestion)



while True:
    run_alexa()
