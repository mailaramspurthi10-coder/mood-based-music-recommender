from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

songs = {
    "Happy": [
        {"title": "Happy", "artist": "Pharrell Williams"},
        {"title": "Uptown Funk", "artist": "Bruno Mars"}
    ],
    "Sad": [
        {"title": "Someone Like You", "artist": "Adele"},
        {"title": "Let Her Go", "artist": "Passenger"}
    ],
    "Relaxed": [
        {"title": "Weightless", "artist": "Marconi Union"}
    ],
    "Energetic": [
        {"title": "Believer", "artist": "Imagine Dragons"}
    ]
}

@app.route("/recommend/<mood>")
def recommend(mood):
    return jsonify(songs.get(mood, []))

if __name__ == "__main__":
    app.run(debug=True)