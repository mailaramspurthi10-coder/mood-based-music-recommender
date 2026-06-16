import os
from typing import TypedDict

from flask import Flask, Response, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


class Song(TypedDict):
    title: str
    artist: str
    link: str


SONGS: dict[str, list[Song]] = {
    "Happy": [
        {
            "title": "Happy",
            "artist": "Pharrell Williams",
            "link": "https://www.youtube.com/results?search_query=Happy+Pharrell+Williams",
        },
        {
            "title": "Uptown Funk",
            "artist": "Bruno Mars",
            "link": "https://www.youtube.com/results?search_query=Uptown+Funk+Bruno+Mars",
        },
    ],
    "Sad": [
        {
            "title": "Someone Like You",
            "artist": "Adele",
            "link": "https://www.youtube.com/results?search_query=Someone+Like+You+Adele",
        },
        {
            "title": "Let Her Go",
            "artist": "Passenger",
            "link": "https://www.youtube.com/results?search_query=Let+Her+Go+Passenger",
        },
    ],
    "Relaxed": [
        {
            "title": "Weightless",
            "artist": "Marconi Union",
            "link": "https://www.youtube.com/results?search_query=Weightless+Marconi+Union",
        }
    ],
    "Energetic": [
        {
            "title": "Believer",
            "artist": "Imagine Dragons",
            "link": "https://www.youtube.com/results?search_query=Believer+Imagine+Dragons",
        }
    ],
}


@app.route("/")
def home():
    return "Mood-Based Music API is running!"


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    mood = data.get("mood", "").capitalize()

    if mood not in SONGS:
        return jsonify({"error": "Mood not found"}), 404

    return jsonify(SONGS[mood])


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="127.0.0.1", port=5000, debug=debug)