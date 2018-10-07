"""
    class: Window(window.py) -> GUI

    class Window gets 2 arguments:
        1) parent -> parent window initialized in main.py
        2) assistant -> Assistant class(assistant.py) object
"""


from tkinter import *


class Window:
    def __init__(self, parent, assistant):
        self.mainWindow = parent
        self.mainWindow.geometry("390x390")
        self.mainWindow.resizable(False, False)
        self.mainWindow.title("ELIZABETH")

        self.voiceAssistant = assistant

        self.create_label()

    def create_label(self):
        self.microphoneNotActiveImage = PhotoImage(file="microphoneNotActiveImage.png")
        self.microphoneActiveImage = PhotoImage(file="microphoneActiveImage.png")

        self.microphone = Label(self.mainWindow, image=self.microphoneNotActiveImage)
        self.microphone.pack()
        self.microphone.bind("<Button-1>", self.check)
        self.mainWindow.update()
        try:
            self.voiceAssistant.say("Hello! My name is Elizabeth. I am voice assistant. Can I help you?")
        except:
            print("ERROR!")
            print("Check your INTERNET connection")

    def check(self, event):
        self.microphone["image"] = self.microphoneActiveImage
        self.mainWindow.update()
        self.voiceAssistant.listen()
        self.microphone["image"] = self.microphoneNotActiveImage

