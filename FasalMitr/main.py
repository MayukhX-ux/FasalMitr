
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.chatbot import Chatbot

class FasalMitrApp(App):
    def build(self):
        sm = ScreenManager()
        # Detect language as before, store in self.language and self.translations
        sm.add_widget(Chatbot(name='chatbot', translations=self.translations, language_code=self.language))
        return sm