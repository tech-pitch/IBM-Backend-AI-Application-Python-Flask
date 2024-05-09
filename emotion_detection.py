import requests
import json
from requests.exceptions import SSLError

def get_emotion(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_json = {"raw_document": {"text": text_to_analyze}}
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    try:
        response = requests.post(url, json=input_json, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.text
    except SSLError as e:
        return f"SSL Error: {e}"
    except requests.RequestException as e:
        return str(e)  # Return the exception message as a string

