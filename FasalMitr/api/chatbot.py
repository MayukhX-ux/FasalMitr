def get_bot_response(user_msg, translations):
    # Basic rule-based responses for demo
    msg_lower = user_msg.lower()
    if "weather" in msg_lower:
        return "You can check the latest weather updates in the Weather section."
    if "government scheme" in msg_lower or "yojana" in msg_lower:
        return "Visit the 'Government Schemes' page for the latest schemes."
    if "market rate" in msg_lower:
        return "Check the 'Market Rates' page for daily crop prices."
    if "soil" in msg_lower:
        return "Use our Soil Analysis section for soil testing and crop recommendations."
    # Add more rules as needed
    
    # For advanced: connect to GPT or other APIs here
    # return get_gpt_response(user_msg, language_code)
    
    return "Sorry, I am not sure about that. Please explore the app's sections or rephrase your question."