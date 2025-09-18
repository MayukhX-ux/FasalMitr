def get_language_from_location(lat, lon):
    # You can use a geocoding API to get the region/state (e.g., Google Maps Geocoding)
    # For demo: Simple rule-based logic
    # Delhi/Mumbai = Hindi, Kolkata = Bengali, default = English

    # For full solution, use a geocoding API response
    if lat is None or lon is None:
        return 'en'
    if 22 <= lat <= 29 and 77 <= lon <= 78:
        return 'hi' # Hindi belt (Delhi, UP, Bihar)
    if 22 <= lat <= 24 and 88 <= lon <= 89:
        return 'bn' # Bengali (Kolkata region)
    # Add more rules for other states/languages
    return 'en'