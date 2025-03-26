from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    emotion_scores = emotion_detector(text_to_analyze)

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
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)