# Sean Kunz
# Speech

import time

import speech_recognition as sr

class Speech:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.currAmt = 0.0

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

    def listen(self):
        time.sleep(1)
        for j in range(10):
            print("Attempt " + str(j+1) + ".")
            guess = self.recognize_speech_from_mic()
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")

        print("You said: " + guess["transcription"])
        if "test" in guess["transcription"]:
            self.currAmt += 0.25
        print("Curr Amt: $" + str(self.currAmt))
