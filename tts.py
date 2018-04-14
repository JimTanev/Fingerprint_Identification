import pyttsx3


class TTS:

    def __init__(self):
        self.tts = pyttsx3.init()
        self.tts.setProperty('rate', self.tts.getProperty('rate') - 40)
        self.tts.setProperty('voice', 'bulgarian')

    def speak(self, message):
        self.tts.say(message)
        self.tts.runAndWait()

    def stop(self):
        self.tts.stop()

    def add_speak_hover(self, widget, message):
        widget.connect("enter-notify-event", lambda w, _: self.speak(message))
        widget.connect("leave-notify-event", lambda w, _: self.tts.stop())
