from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from components.top_panel import TopPanel
from api.agri_history import fetch_historical_data, compare_crops

class HistoricalData(Screen):
    def __init__(self, translations, language_code, **kwargs):
        super(HistoricalData, self).__init__(**kwargs)
        self.translations = translations
        self.language_code = language_code
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(TopPanel(self.manager, translations))

        self.crop_spinner = Spinner(text=translations.get('select_crop', 'Select Crop'), values=['Wheat', 'Rice', 'Maize'])
        self.interval_spinner = Spinner(text=translations.get('select_interval', 'Select Interval'), values=['1 Year', '5 Years', '10 Years'])
        self.region_input = Spinner(text=translations.get('select_region', 'Select Region'), values=['Delhi', 'Punjab', 'Odisha', 'Maharashtra'])

        layout.add_widget(self.crop_spinner)
        layout.add_widget(self.interval_spinner)
        layout.add_widget(self.region_input)

        compare_btn = Button(text=translations.get('compare', 'Compare'))
        compare_btn.bind(on_press=self.compare)
        layout.add_widget(compare_btn)

        self.result_label = Label(text='', font_size=18)
        layout.add_widget(self.result_label)
        self.add_widget(layout)

    def compare(self, instance):
        crop = self.crop_spinner.text
        interval = self.interval_spinner.text
        region = self.region_input.text
        data = compare_crops(crop, interval, region, self.language_code)
        self.result_label.text = data