from kivy.uix.popup import Popup
from kivy.uix.label import Label

def show_popup_alert(message):
    popup = Popup(title="Weather Calamity Alert",
                  content=Label(text=message),
                  size_hint=(0.8, 0.2))
    popup.open()