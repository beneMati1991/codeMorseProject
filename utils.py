import json
import winsound
import time

# Specifying time lengths and beep frequency
DOT = 150  # in milliseconds
DASH = 450  # in milliseconds
WAIT_TIME_UNIT = 0.35  # in seconds
FREQ = 1700  # in HZ

class Utils:
    #develop
    def __init__(self, word):
        self.word = word
        self.data = {}
        self.listChar = []

    def openJson(self):
        with open("code-morse.json","r") as code:
            self.data = json.load(code)

    def transformCaracter(self):
        self.listChar = list(self.word)

    def translate(self):
        listMorse = []
        self.transformCaracter()
        self.openJson()
        for letter in self.listChar:
            listMorse.append(list(self.data[f"{letter}"]))
        return listMorse

    def soundMorse(self):
        listSound = self.translate()
        for item in listSound:
            for caracter in item:
                if (caracter == '.'):
                    winsound.Beep(FREQ, DOT)
                else:
                    winsound.Beep(FREQ, DASH)
                time.sleep(WAIT_TIME_UNIT)
