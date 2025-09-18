def fetch_historical_data(crop, interval, region):
    # Use government agri APIs or CSVs
    # Return historical yield/price for the crop, region, interval
    # Example output:
    return {
        'Wheat': [2050, 2100, 2200],  # prices over years
        'Rice': [1800, 1750, 1900],
        # ...
    }

def compare_crops(crop, interval, region, language_code):
    # Fetch and compare crops for given region and interval
    data = fetch_historical_data(crop, interval, region)
    # For demo, just return a formatted string in user's language
    # Expand for other crops
    if language_code == 'hi':
        return f"{crop} की पिछली {interval} में औसत कीमत: ₹{sum(data[crop])/len(data[crop])}\nअन्य फसलों से तुलना करें।"
    elif language_code == 'mr':
        return f"{crop} ची गेल्या {interval} मधील सरासरी किंमत: ₹{sum(data[crop])/len(data[crop])}\nइतर पिकांसोबत तुलना करा."
    else:
        return f"Average price of {crop} in last {interval}: ₹{sum(data[crop])/len(data[crop])}\nCompare with other crops."