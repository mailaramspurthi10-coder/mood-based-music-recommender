import os
from typing import Any, TypedDict

from flask import Flask, jsonify
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
            "title": "Butta Bomma",
            "artist": "Armaan Malik",
            "link": "https://www.youtube.com/results?search_query=Butta+Bomma",
        },
        {
            "title": "Kesariya",
            "artist": "Arijit Singh",
            "link": "https://www.youtube.com/results?search_query=Kesariya",
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
        {
            "title": "Inkem Inkem Inkem Kaavaale",
            "artist": "Sid Sriram",
            "link": "https://www.youtube.com/results?search_query=Inkem+Inkem+Inkem+Kaavaale",
        },
    ],

    "Relaxed": [
        {
            "title": "Weightless",
            "artist": "Marconi Union",
            "link": "https://www.youtube.com/results?search_query=Weightless+Marconi+Union",
        },
        {
            "title": "Samajavaragamana",
            "artist": "Sid Sriram",
            "link": "https://www.youtube.com/results?search_query=Samajavaragamana",
        },
    ],

    "Energetic": [
        {
            "title": "Believer",
            "artist": "Imagine Dragons",
            "link": "https://www.youtube.com/results?search_query=Believer+Imagine+Dragons",
        },
        {
            "title": "Naatu Naatu",
            "artist": "Rahul Sipligunj",
            "link": "https://www.youtube.com/results?search_query=Naatu+Naatu",
        },
        {
            "title": "Jai Ho",
            "artist": "A.R. Rahman",
            "link": "https://www.youtube.com/results?search_query=Jai+Ho",
        },
    ],
}


@app.route("/")
def home() -> str:
    return "Mood-Based Music API is running!"


@app.route("/recommend/<mood>", methods=["GET"])
def recommend(mood: str) -> Any:
    mood = mood.capitalize()

    if mood not in SONGS:
        return jsonify({"error": "Mood not found"}), 404

    return jsonify(SONGS[mood])


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="127.0.0.1", port=5000, debug=debug)
