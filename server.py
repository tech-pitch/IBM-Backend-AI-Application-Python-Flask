from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector  # Make sure this is the correct path

app = Flask("Emotion Detector")

@app.route('/')
def render_index_page():
    return render_template('index.html')

@app.route('/emotionDetector')
def get_emotion_response():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    # Format the response into a readable string
    emotions = ', '.join([f"'{key}': {value:.9f}" for key, value in response.items() if key != 'dominant_emotion'])
    dominant_emotion = response.get('dominant_emotion', 'No dominant emotion detected')
    formatted_response = f"For the given statement, the system response is {emotions}. The dominant emotion is {dominant_emotion}."
    
    return formatted_response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
