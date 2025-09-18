from api.voice_assistant import listen, speak
from kivy.uix.screenmanager import Screen

class Chatbot(Screen):
    def __init__(self, translations, language_code, **kwargs):
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.button import Button
        from kivy.uix.floatlayout import FloatLayout
        super().__init__(**kwargs)
        self.translations = translations
        self.language_code = language_code
        layout = FloatLayout()
        voice_row = BoxLayout(size_hint_y=0.1)
        listen_btn = Button(text=translations.get('voice_listen', '🎤 Listen'))
        speak_btn = Button(text=translations.get('voice_speak', '🔊 Speak'))
        listen_btn.bind(on_press=self.voice_listen)
        speak_btn.bind(on_press=self.voice_speak)
        voice_row.add_widget(listen_btn)
        voice_row.add_widget(speak_btn)
        layout.add_widget(voice_row)
        self.add_widget(layout)
        # ...rest...

    def voice_listen(self, instance):
        user_msg = listen(self.language_code)
        self.input_box.text = user_msg

    def voice_speak(self, instance):
        if self.messages:
            text = self.messages[-1]['text']
            speak(text, self.language_code)