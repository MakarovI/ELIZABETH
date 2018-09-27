import speech_recognition as sr
from playsound import playsound
from tkinter import *
import platform
import webbrowser
import subprocess
from gtts import gTTS
import os

class Window:
    def __init__(self, parent, Assistant):
        self.mainWindow = parent
        self.mainWindow.geometry("390x390")
        self.mainWindow.resizable(False, False)
        self.mainWindow.title("ELIZABETH")

        self.ai = Assistant

        self.make_label()


    def make_label(self):
        self.microphoneImage = PhotoImage(file="microphone.png")
        self.microphoneImage2 = PhotoImage(file="microphone2.png")

        self.microphone = Label(self.mainWindow, image=self.microphoneImage)
        self.microphone.pack()
        self.microphone.bind("<Button-1>", self.check)
        self.mainWindow.update()
        self.ai.say("Hello! My name is Elizabeth. I am voice assistant. Can I help you?")

    def check(self, event):
        self.microphone["image"] = self.microphoneImage2
        self.mainWindow.update()
        self.ai.work()
        self.microphone["image"] = self.microphoneImage


class Assistant:
    def __init__(self):
        self._recognizer = sr.Recognizer()
        self._microphone = sr.Microphone()
        print("\033[H\033[J")


    def work(self):
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
                self.say("I can't get access to google speech recognition service. Maybe you have some problems with internet conection.")
                break
    def process(self, statement):
        if "browser" in statement:
            webbrowser.open("https://www.google.com/")
        elif "weather" in statement:
            webbrowser.open("https://www.accuweather.com/")
        elif "calculator" in statement:
            self.osrun("gnome-calculator")
        elif "terminal" in statement or "console" in statement:
            self.osrun("gnome-terminal")
        elif "notepad" in statement or "text editor" in statement or "editor" in statement:
            self.osrun("gnome-text-editor")
        elif "sport" in statement:
            webbrowser.open("https://www.bbc.com/sport")
        elif "news" in statement or "new" in statement:
            webbrowser.open("https://www.bbc.com/news")
        elif "calendar" in statement:
            self.osrun("gnome-calendar")
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

    def osrun(self, cmd):
        PIPE = subprocess.PIPE
        subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)

    def say(self, text):
        tts = gTTS(text)
        tts.save("AssistantSpeech.mp3")
        playsound("AssistantSpeech.mp3")

def main():
    ai = Assistant()
    if platform.system() != "Linux":
        ai.say("Error. It is only for Linux")
        sys.exit()
    master = Tk()
    Window(master, ai)
    master.mainloop()


if __name__ == "__main__":
    main()

