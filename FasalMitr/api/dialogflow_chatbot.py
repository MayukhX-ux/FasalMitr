import os
from google.cloud import dialogflow_v2 as dialogflow

# Set Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcloud-service-account.json"

def get_dialogflow_response(user_message, session_id, language_code="en"):
    project_id = "YOUR_DIALOGFLOW_PROJECT_ID"  # Replace with your project ID
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(text=user_message, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text