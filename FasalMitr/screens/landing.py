from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.screenmanager import Screen

class LandingPage(Screen):
    def __init__(self, translations, **kwargs):
        super(LandingPage, self).__init__(**kwargs)
        t = translations
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.layout.add_widget(Label(text=t['welcome'], font_size=32))
        self.layout.add_widget(Label(text=t['register_profile'], font_size=24))

        self.name_input = TextInput(hint_text=t['name'], multiline=False)
        self.layout.add_widget(self.name_input)

        self.age_input = TextInput(hint_text=t['age'], multiline=False, input_filter='int')
        self.layout.add_widget(self.age_input)

        self.layout.add_widget(Label(text=t['are_you'], font_size=20))

        self.btn_existing = ToggleButton(text=t['existing_farmer'], group="farmer_type")
        self.btn_beginner = ToggleButton(text=t['beginner'], group="farmer_type")
        # ... rest of the code using t['...'] for UI strings

        self.add_widget(self.layout)