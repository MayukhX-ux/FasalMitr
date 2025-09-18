from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.camera import Camera
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from ai.soil import ml_analyse_soil_image

class SoilAnalysis(Screen):
    def __init__(self, **kwargs):
        super(SoilAnalysis, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.layout.add_widget(Label(text='Soil Analysis (AI)', font_size=28))

        self.img_widget = Image(size_hint=(1, 0.4))
        self.layout.add_widget(self.img_widget)

        self.capture_btn = Button(text='Capture Photo')
        self.capture_btn.bind(on_press=self.open_camera)
        self.layout.add_widget(self.capture_btn)

        self.upload_btn = Button(text='Upload Photo')
        self.upload_btn.bind(on_press=self.open_filechooser)
        self.layout.add_widget(self.upload_btn)

        self.analyse_btn = Button(text='Analyse Image')
        self.analyse_btn.bind(on_press=self.run_analysis)
        self.layout.add_widget(self.analyse_btn)
        self.analyse_btn.disabled = True

        self.result_label = Label(text='', font_size=18)
        self.layout.add_widget(self.result_label)

        self.add_widget(self.layout)
        self.img_path = None

    def open_camera(self, instance):
        self.camera = Camera(play=True)
        self.camera.resolution = (640, 480)
        self.layout.add_widget(self.camera)
        self.capture_img_btn = Button(text='Take Photo')
        self.capture_img_btn.bind(on_press=self.capture_image)
        self.layout.add_widget(self.capture_img_btn)

    def capture_image(self, instance):
        filename = "soil_photo.png"
        self.camera.export_to_png(filename)
        self.img_path = filename
        self.img_widget.source = filename
        self.analyse_btn.disabled = False
        self.camera.play = False
        self.layout.remove_widget(self.camera)
        self.layout.remove_widget(self.capture_img_btn)

    def open_filechooser(self, instance):
        self.filechooser = FileChooserIconView()
        self.filechooser.bind(on_selection=self.select_file)
        self.layout.add_widget(self.filechooser)

    def select_file(self, instance, selection):
        if selection:
            self.img_path = selection[0]
            self.img_widget.source = self.img_path
            self.analyse_btn.disabled = False
            self.layout.remove_widget(self.filechooser)

    def run_analysis(self, instance):
        if self.img_path:
            result = ml_analyse_soil_image(self.img_path)
            self.result_label.text = "\n".join(result)