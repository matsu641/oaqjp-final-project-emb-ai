from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Invalid input. 'text' field is required."}), 400

    text = data["text"]
    response = emotion_detector(text)

    try:
        response_json = response
        anger = response_json['anger']
        disgust = response_json['disgust']
        fear = response_json['fear']
        joy = response_json['joy']
        sadness = response_json['sadness']
        dominant = response_json['dominant_emotion']


        message = f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant}."

        return jsonify({"response": message}), 200
    except Exception as e:
        return jsonify({"error": "Failed to parse response", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
