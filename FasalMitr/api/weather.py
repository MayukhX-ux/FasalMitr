import requests

def fetch_weather(lat, lon):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # <-- Replace with your key
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={lat}&lon={lon}&units=metric&appid={api_key}"
    )
    try:
        r = requests.get(url)
        data = r.json()
        if "weather" in data and "main" in data:
            return {
                "description": data["weather"][0]["description"],
                "temp": data["main"]["temp"]
            }
    except Exception:
        return None