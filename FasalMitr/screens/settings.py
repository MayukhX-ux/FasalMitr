from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class Settings(Screen):
    def __init__(self, translations, **kwargs):
        super(Settings, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text=translations.get('settings', 'SETTINGS'), font_size=32))

        self.sound_switch = Switch(active=True)
        layout.add_widget(Label(text="Enable Sound Alarm"))
        layout.add_widget(self.sound_switch)

        self.push_switch = Switch(active=True)
        layout.add_widget(Label(text="Enable Push Notification"))
        layout.add_widget(self.push_switch)

        self.sms_switch = Switch(active=False)
        layout.add_widget(Label(text="Enable SMS Alert"))
        layout.add_widget(self.sms_switch)

        self.mobile_input = TextInput(hint_text="Your Mobile Number (for SMS)", multiline=False)
        layout.add_widget(self.mobile_input)

        self.add_widget(layout)