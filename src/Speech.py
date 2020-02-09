# Sean Kunz
# Speech

import time

import speech_recognition as sr

class Speech:
    def __init__(self, db, lbl):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        self.lbl = lbl

        self.database = db
        self.swears = ['test', 'shit', 'ass', 'hell', 'dam', 'fuck']

    def recognize_speech_from_mic(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        response = { "success": True, "error": None, "transcription": None }

        try:
            response["transcription"] = self.recognizer.recognize_google_cloud(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"

        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"

        return response

    def calculate(self, guess, label):
        for w in self.swears:
            num = guess["transcription"].count(w)
            if num:
                for i in range(num):
                    self.database.setProgress()

        txt = "$" + str("{0:.2f}".format(self.database.getProgress()))
        label.config(text=txt)


    def listen(self, label):
        for j in range(10):
            guess = self.recognize_speech_from_mic()
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")

        print("You said: " + guess["transcription"])
        txt = "You said: " + guess["transcription"]
        self.lbl.config(text=txt)
        self.calculate(guess, label)
