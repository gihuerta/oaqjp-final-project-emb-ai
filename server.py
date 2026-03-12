"""
The following module executes an app using the Flask framework.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detection

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detect():
    """
    The following function uses the imported function emotion_detection to
    retrieve a dictionary of emotion percents and the dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detection(text_to_analyze)

    if response['dominant_emotion'] is None:
        message = "Invalid text! Please try again!"
    else:
        message = (f"For the given statement, the system response is 'anger': "
        f"{response['anger']},'disgust': {response['disgust']}, 'fear': "
        f"{response['fear']}, 'joy': {response['joy']},and 'sadness': "
        f"{response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}.")

    return message

@app.route("/")
def render_index_page():
    """
    The following function executes the html file index.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
