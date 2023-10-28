import pyttsx3
import os


def get_platform():
    if os.name == 'nt':
        return 'Windows'
    elif os.name == 'posix':
        return 'macOS/Linux'
    else:
        return 'Unknown'


if (get_platform() == 'Windows'):
    engine = pyttsx3.init("sapi5")
else:
    engine = pyttsx3.init("nsss")


voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)
engine.setProperty("rate", 160)


def say(Text):
    engine.say(text=Text)
    engine.runAndWait()