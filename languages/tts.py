import pyttsx3


class TTS:

    def __init__(self, language):
        self.tts = pyttsx3.init()
        self.tts.setProperty('rate', self.tts.getProperty('rate'))
        self.tts.setProperty('voice', language)

    def speak(self, message):
        self.tts.say(message)
        self.tts.runAndWait()

    def spell(self, message):
        letters = list(message)
        for letter in letters:
            self.speak(letter)

    def stop(self):
        self.tts.stop()

    def add_speak_hover(self, widget, message):
        widget.connect('enter-notify-event', lambda w, _: self.speak(message))
        widget.connect('leave-notify-event', lambda w, _: self.tts.stop())
