from api.market_price import get_chemical_price

def ml_analyse_plant_image(img_path, region, language_code):
    # ... existing ML code ...
    # Suppose diagnosis gives "Fungal Infection"
    chemical = "Carbendazim"
    price = get_chemical_price(chemical, region)
    if language_code == 'hi':
        return [
            "• पौधे में फफूंदी संक्रमण पाया गया।",
            f"• अनुशंसित रासायनिक: {chemical}",
            f"• बाजार मूल्य: ₹{price}/किलो"
        ]
    elif language_code == 'mr':
        return [
            "• वनस्पतीत बुरशीचा संसर्ग आढळला.",
            f"• शिफारस केलेले रसायन: {chemical}",
            f"• बाजार किंमत: ₹{price}/किलो"
        ]
    else:
        return [
            "• Fungal infection detected in plant.",
            f"• Recommended chemical: {chemical}",
            f"• Market price: ₹{price}/kg"
        ]