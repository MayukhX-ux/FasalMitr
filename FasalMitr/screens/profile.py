from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from components.top_panel import TopPanel

class Profile(Screen):
    def __init__(self, translations, **kwargs):
        super(Profile, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(TopPanel(self.manager, translations))
        layout.add_widget(Label(text=translations.get('profile', 'PROFILE'), font_size=32))
        self.add_widget(layout)