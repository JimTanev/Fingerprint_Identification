from .messages.messages_bg import BG
from .messages.messages_en import EN
from .tts import TTS


class LanguageProperties:
    __bulgarian = BG()
    __english = EN()

    def __init__(self):
        self.messages = self.__bulgarian
        self.tts = TTS('bulgarian')

    def change_language(self):
        if self.messages is self.__bulgarian:
            self.messages = self.__english
            self.tts = TTS('english')
        else:
            self.messages = self.__bulgarian
            self.tts = TTS('bulgarian')
