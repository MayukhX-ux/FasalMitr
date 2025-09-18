from kivy.uix.boxlayout import BoxLayout
# ...existing code...
class TopPanel(BoxLayout):  # Changed SomeParentClass to BoxLayout for Kivy
	def __init__(self, t=None, **kwargs):
		from kivy.uix.button import Button
		super().__init__(**kwargs)
		if t is None:
			t = {}
		self.add_widget(Button(text=t.get('chatbot', 'CHATBOT'), on_press=lambda x: self.goto('chatbot')))