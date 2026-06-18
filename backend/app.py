import requests
import os
import json
from typing import TypedDict

from flask import Flask, jsonify, render_template, request
from flask.typing import ResponseReturnValue
from flask_cors import CORS

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)


class Song(TypedDict):
    title: str
    artist: str
    link: str


SONGS: dict[str, list[Song]] = {
    "happy": [
        {"title": "Happy", "artist": "Pharrell Williams",
         "link": "https://www.youtube.com/results?search_query=Happy+Pharrell+Williams"},
        {"title": "Butta Bomma", "artist": "Armaan Malik",
         "link": "https://www.youtube.com/results?search_query=Butta+Bomma"},
        {"title": "Samajavaragamana", "artist": "Sid Sriram",
         "link": "https://www.youtube.com/results?search_query=Samajavaragamana"},
        {"title": "Kesariya", "artist": "Arijit Singh",
         "link": "https://www.youtube.com/results?search_query=Kesariya"},
    ],
    "sad": [
        {"title": "Someone Like You", "artist": "Adele",
         "link": "https://www.youtube.com/results?search_query=Someone+Like+You+Adele"},
        {"title": "Agar Tum Saath Ho", "artist": "Alka Yagnik",
         "link": "https://www.youtube.com/results?search_query=Agar+Tum+Saath+Ho"},
        {"title": "Adiga Adiga", "artist": "Sid Sriram",
         "link": "https://www.youtube.com/results?search_query=Adiga+Adiga"},
    ],
    "relaxed": [
        {"title": "Weightless", "artist": "Marconi Union",
         "link": "https://www.youtube.com/results?search_query=Weightless+Marconi+Union"},
        {"title": "Inkem Inkem Inkem Kaavaale", "artist": "Sid Sriram",
         "link": "https://www.youtube.com/results?search_query=Inkem+Inkem+Inkem+Kaavaale"},
        {"title": "Raataan Lambiyan", "artist": "Jubin Nautiyal",
         "link": "https://www.youtube.com/results?search_query=Raataan+Lambiyan"},
    ],
    "energetic": [
        {"title": "Believer", "artist": "Imagine Dragons",
         "link": "https://www.youtube.com/results?search_query=Believer+Imagine+Dragons"},
        {"title": "Naatu Naatu", "artist": "Rahul Sipligunj",
         "link": "https://www.youtube.com/results?search_query=Naatu+Naatu"},
        {"title": "Malhari", "artist": "Vishal Dadlani",
         "link": "https://www.youtube.com/results?search_query=Malhari"},
    ],
}


def get_ollama_songs(mood: str):
    prompt = f"""
You are a music recommendation system.

Return ONLY valid JSON.

Mood: {mood}

Format:
[
  {{"title": "Song name", "artist": "Artist name"}},
  {{"title": "Song name", "artist": "Artist name"}},
  {{"title": "Song name", "artist": "Artist name"}},
  {{"title": "Song name", "artist": "Artist name"}},
  {{"title": "Song name", "artist": "Artist name"}}
]

Do not include explanation or extra text.
Only return JSON.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    ai_text = response.json()["response"]

    try:
        songs = json.loads(ai_text)
        return songs
    except Exception:
        return []


@app.route("/")
def home() -> ResponseReturnValue:
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend() -> ResponseReturnValue:
    data = request.get_json()

    if not data or "mood" not in data:
        return jsonify({"error": "Mood is required"}), 400

    mood = data["mood"].strip().lower()
    provider = data.get("provider", "static")

    # 🤖 OLLAMA MODE
    if provider == "ollama":
        songs = get_ollama_songs(mood)

        # fallback if AI fails
        if not songs:
            songs = SONGS.get(mood, [])

        return jsonify({
            "mood": mood,
            "provider": "ollama",
            "songs": songs
        })

    # 📌 STATIC MODE
    if mood not in SONGS:
        return jsonify({"error": "Mood not found"}), 404

    return jsonify({
        "mood": mood,
        "provider": "static",
        "songs": SONGS[mood]
    })


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="127.0.0.1", port=5000, debug=debug)