"""
    class Assistant gets speech from microphone and process it.
    Library for converting a text into a speech -> gtts
    Library for getting speech by microphone and converting it to a text -> speech_recognition

"""

import speech_recognition as sr
import webbrowser
import subprocess
import os
import sys

from playsound import playsound
from gtts import gTTS


class Assistant:
    def __init__(self):
        self._recognizer = sr.Recognizer()
        self._microphone = sr.Microphone()
        print("\033[H\033[J")  # clear terminal screen from errors caused by sr.Microphone() function

    def listen(self):
        with self._microphone as source:
            self._recognizer.adjust_for_ambient_noise(source)

        while True:
            with self._microphone as source:
                audio = self._recognizer.listen(source)
            try:
                statement = self._recognizer.recognize_google(audio, language="en_EN")
                statement = statement.lower()
                self.process(statement)
                break

            except sr.UnknownValueError:
                self.say("Sorry.I did not understand you. Repeat it please.")
                break
            except sr.RequestError as e:
                self.say("I can't get access to google speech recognition service.")
                break

    def process(self, statement):
        if "browser" in statement:
            webbrowser.open("https://www.google.com/")
        elif "weather" in statement:
            webbrowser.open("https://www.accuweather.com/")
        elif "calculator" in statement:
            self.shell_command("gnome-calculator")
        elif "terminal" in statement or "console" in statement:
            self.shellCommand("gnome-terminal")
        elif "notepad" in statement or "text editor" in statement or "editor" in statement:
            self.shell_command("gnome-text-editor")
        elif "sport" in statement:
            webbrowser.open("https://www.bbc.com/sport")
        elif "news" in statement or "new" in statement:
            webbrowser.open("https://www.bbc.com/news")
        elif "calendar" in statement:
            self.shell_command("gnome-calendar")
        elif "shutdown" in statement:
            os.system('shutdown')
        elif "reboot" in statement or "restart" in statement:
            os.system('reboot')
        elif "bye" in statement or "by" in statement:
            self.say("Goodbye!")
            sys.exit()
        elif "name" in statement:
            self.say("My name is Elizabeth")
        elif "what's up" in statement or "what" in statement or "up" in statement:
            self.say("I am fine. What about you?")
        else:
            self.say("Sorry. I do not understand that command")

    @staticmethod
    def shell_command(cmd):
        pipe = subprocess.PIPE
        subprocess.Popen(cmd, shell=True, stdin=pipe, stdout=pipe, stderr=subprocess.STDOUT)

    @staticmethod
    def say(text):
        tts = gTTS(text)
        tts.save("AssistantSpeech.mp3")
        playsound("AssistantSpeech.mp3")

