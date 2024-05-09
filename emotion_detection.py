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

        # Parse the JSON resp into a dict
        response_json = response.json()
        # Return the dic
        return response_json
    except SSLError as e:
        return f"SSL Error: {e}"
    except requests.RequestException as e:
        return str(e)  # Return the exception message as a string

def get_emotion_scores(text_to_analyze):
    emotion_response = get_emotion(text_to_analyze)  # This function must be defined elsewhere as you're using it here.

    emotion_predictions = emotion_response.get("emotionPredictions")  # Use .get() to avoid KeyError if the key is not found.

    if emotion_predictions:  # Check if the list is not empty.
        # Access the first item's 'emotion' dictionary.
        first_prediction_emotions = emotion_predictions[0]['emotion']  
        # Determine the dominant emotion
        dominant_emotion = max(first_prediction_emotions, key=first_prediction_emotions.get)  # Finds the key with the highest value

        responses = {
            'anger': first_prediction_emotions['anger'],
            'disgust': first_prediction_emotions['disgust'],
            'fear': first_prediction_emotions['fear'],
            'joy': first_prediction_emotions['joy'],
            'sadness': first_prediction_emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }

        return responses
    else:
        return {}  # Return an empty dictionary if there are no predictions.

    