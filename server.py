''' Final task server.py file
'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion analysis over it using emotion_detector()
        function.
    '''

    text_to_analyze = request.args.get('textToAnalyze')

    emotion_scores = emotion_detector(text_to_analyze)

    if emotion_scores["dominant_emotion"] is None:
        response_text = "Invalid text! Please try again!"
    else:
        response_text = (
            f"For the given statement, the system response is "
            f"'anger': {emotion_scores['anger']}, "
            f"'disgust': {emotion_scores['disgust']}, "
            f"'fear': {emotion_scores['fear']}, "
            f"'joy': {emotion_scores['joy']} and "
            f"'sadness': {emotion_scores['sadness']}. "
            f"The dominant emotion is <b>{emotion_scores['dominant_emotion']}</b>."
        )

    return response_text

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
