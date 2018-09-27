import assistant
import window
import platform

from tkinter import *


def main():
    voiceAssistant = assistant.Assistant()
    if platform.system() != "Linux":
        voiceAssistant.say("Error. It is only for Linux")
        sys.exit()
    master = Tk()
    window.Window(master, voiceAssistant)
    master.mainloop()


if __name__ == "__main__":
    main()
