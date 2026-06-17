import os
from typing import TypedDict, List, Dict

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


class Song(TypedDict):
    title: str
    artist: str
    link: str


SONGS: Dict[str, List[Song]] = {
    "happy": [
        {
            "title": "Happy",
            "artist": "Pharrell Williams",
            "link": "https://www.youtube.com/results?search_query=Happy+Pharrell+Williams",
        },
        {
            "title": "Butta Bomma",
            "artist": "Armaan Malik",
            "link": "https://www.youtube.com/results?search_query=Butta+Bomma",
        },
    ],
    "sad": [
        {
            "title": "Someone Like You",
            "artist": "Adele",
            "link": "https://www.youtube.com/results?search_query=Someone+Like+You+Adele",
        },
    ],
    "relaxed": [
        {
            "title": "Weightless",
            "artist": "Marconi Union",
            "link": "https://www.youtube.com/results?search_query=Weightless+Marconi+Union",
        },
    ],
    "energetic": [
        {
            "title": "Believer",
            "artist": "Imagine Dragons",
            "link": "https://www.youtube.com/results?search_query=Believer+Imagine+Dragons",
        },
    ],
}


@app.route("/")
def home():
    return jsonify({"message": "Mood-Based Music API is running"})


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    if not data or "mood" not in data:
        return jsonify({"error": "Mood is required"}), 400

    mood = data["mood"].strip().lower()

    if mood not in SONGS:
        return jsonify({"error": "Mood not found"}), 404

    return jsonify({
        "mood": mood,
        "songs": SONGS[mood]
    })


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="127.0.0.1", port=5000, debug=debug)