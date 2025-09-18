from api.weather_alert import fetch_weather_alerts
from api.alarm import play_alarm_sound
def send_push_notification(title, message):
    print(f"Push Notification - {title}: {message}")
from api.popup import show_popup_alert
from api.sms import send_sms_alert

def check_weather_calamity(self, *args):
    calamities = fetch_weather_alerts(self.lat, self.lon, self.api_key)
    if calamities:
        alarm_text = "⚠️ WEATHER ALERT!\n"
        for c in calamities:
            alarm_text += f"{c['event']}: {c['description']}\n"
        self.alarm_label.text = alarm_text
        self.alarm_label.color = (1, 0, 0, 1)  # Red

        # Sound alarm
        play_alarm_sound()
        # Push notification
        send_push_notification("Weather Alert", alarm_text)
        # Popup
        show_popup_alert(alarm_text)
        # SMS (if mobile number set in Profile)
        if hasattr(self, 'user_mobile') and self.user_mobile:
            send_sms_alert(
                self.user_mobile,
                alarm_text,
                account_sid="YOUR_TWILIO_SID",
                auth_token="YOUR_TWILIO_TOKEN",
                from_number="YOUR_TWILIO_NUMBER"
            )
    else:
        self.alarm_label.text = ''