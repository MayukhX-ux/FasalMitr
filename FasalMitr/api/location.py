from plyer import gps

def get_location():
    try:
        gps.configure(on_location=lambda loc: loc, on_status=lambda *a: None)
        gps.start(minTime=1000, minDistance=0)
        # For demo, immediately stop and return Delhi
        gps.stop()
        return {'lat': 28.6139, 'lon': 77.2090}
    except Exception:
        return {'lat': 28.6139, 'lon': 77.2090}