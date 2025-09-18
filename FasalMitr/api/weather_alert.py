import requests

def fetch_weather_alerts(lat, lon, api_key):
    # OpenWeatherMap One Call API provides alerts if available
    url = (
        f"https://api.openweathermap.org/data/3.0/onecall?"
        f"lat={lat}&lon={lon}&appid={api_key}"
    )
    try:
        r = requests.get(url)
        data = r.json()
        alerts = data.get('alerts', [])
        calamities = []
        for alert in alerts:
            # Check for keywords like storm, cyclone, flood, etc.
            if any(x in alert['event'].lower() for x in ['storm', 'cyclone', 'flood', 'heatwave', 'heavy rain', 'thunder']):
                calamities.append({
                    'event': alert['event'],
                    'description': alert.get('description', ''),
                    'start': alert.get('start', ''),
                    'end': alert.get('end', ''),
                    'sender': alert.get('sender_name', '')
                })
        return calamities
    except Exception as e:
        return []