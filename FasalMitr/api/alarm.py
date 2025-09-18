from kivy.core.audio import SoundLoader

def play_alarm_sound():
    sound = SoundLoader.load('assets/alarm.wav')
    if sound:
        sound.play()