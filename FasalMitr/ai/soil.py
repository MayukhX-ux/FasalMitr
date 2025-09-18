from api.market_price import get_chemical_price

def ml_analyse_soil_image(img_path, region, language_code):
    # ... existing ML code ...
    # Suppose diagnosis gives "Nitrogen Deficiency"
    chemical = "Urea"
    price = get_chemical_price(chemical, region)
    if language_code == 'hi':
        return [
            f"• रासायनिक: {chemical}",
            f"• क्षेत्रीय बाजार मूल्य: ₹{price}/किलो",
            "• अनुशंसा: मिट्टी में यूरिया डालें।"
        ]
    elif language_code == 'mr':
        return [
            f"• रसायन: {chemical}",
            f"• स्थानिक बाजार किंमत: ₹{price}/किलो",
            "• शिफारस: मातीमध्ये यूरिया वापरा."
        ]
    else:
        return [
            f"• Chemical: {chemical}",
            f"• Regional market price: ₹{price}/kg",
            "• Recommendation: Apply urea to the soil."
        ]