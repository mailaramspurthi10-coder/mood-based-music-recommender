import os

from typing import Any, TypedDict

from flask import Flask, jsonify

import requests
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
        {"title": "Happy", "artist": "Pharrell Williams",
         "link": "https://www.youtube.com/results?search_query=Happy+Pharrell+Williams"},
        {"title": "Butta Bomma", "artist": "Armaan Malik",
         "link": "https://www.youtube.com/results?search_query=Butta+Bomma"},
        {"title": "Kesariya", "artist": "Arijit Singh",
         "link": "https://www.youtube.com/results?search_query=Kesariya"},
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


    "sad": [
        {"title": "Someone Like You", "artist": "Adele",
         "link": "https://www.youtube.com/results?search_query=Someone+Like+You+Adele"},
        {"title": "Let Her Go", "artist": "Passenger",
         "link": "https://www.youtube.com/results?search_query=Let+Her+Go+Passenger"},
        {"title": "Inkem Inkem Inkem Kaavaale", "artist": "Sid Sriram",
         "link": "https://www.youtube.com/results?search_query=Inkem+Inkem+Inkem+Kaavaale"},
    ],

    "relaxed": [
        {"title": "Weightless", "artist": "Marconi Union",
         "link": "https://www.youtube.com/results?search_query=Weightless+Marconi+Union"},
        {"title": "Samajavaragamana", "artist": "Sid Sriram",
         "link": "https://www.youtube.com/results?search_query=Samajavaragamana"},
    ],

    "energetic": [
        {"title": "Believer", "artist": "Imagine Dragons",
         "link": "https://www.youtube.com/results?search_query=Believer+Imagine+Dragons"},
        {"title": "Naatu Naatu", "artist": "Rahul Sipligunj",
         "link": "https://www.youtube.com/results?search_query=Naatu+Naatu"},
        {"title": "Jai Ho", "artist": "A.R. Rahman",
         "link": "https://www.youtube.com/results?search_query=Jai+Ho"},

    ],
}


@app.route("/")
<<<<<<< HEAD
def home() -> str:
    return "Mood-Based Music API is running!"


@app.route("/recommend/<mood>", methods=["GET"])
def recommend(mood: str) -> Any:
    mood = mood.capitalize()

def home():
    return jsonify({
        "message": "Mood-Based Music API is running"
    })


# -----------------------------
# 🧠 AI FUNCTION (CLEAN + SAFE)
# -----------------------------
def get_ai_recommendations(mood: str):
    try:
        print("🔥 AI FUNCTION CALLED")

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": f"""
Suggest 3 songs for {mood} mood.

Return format:
Song - Artist
Song - Artist
Song - Artist
""",
                "stream": False
            },
            timeout=60
        )

        if response.status_code != 200:
            print("❌ Ollama error:", response.status_code)
            return None

        data = response.json()
        result = data.get("response", "").strip()

        print("📦 AI RESPONSE:\n", result)

        if len(result) < 10:
            return None

        return result

    except Exception as e:
        print("🔥 OLLAMA ERROR:", e)
        return None


# -----------------------------
# 🎧 API ROUTE
# -----------------------------
@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    if not data or "mood" not in data:
        return jsonify({"error": "Mood is required"}), 400


    mood = data["mood"].strip().lower()

    # 1️⃣ Try AI first
    ai_result = get_ai_recommendations(mood)

    if ai_result:
        return jsonify({
            "mood": mood,
            "source": "ai",
            "recommendations": ai_result.split("\n")  # cleaner frontend output
        })

    # 2️⃣ fallback
    if mood in SONGS:
        return jsonify({
            "mood": mood,
            "source": "static",
            "recommendations": SONGS[mood]
        })

    return jsonify({"error": "Mood not found"}), 404


if __name__ == "__main__":

    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="127.0.0.1", port=5000, debug=debug)

    app.run(host="127.0.0.1", port=5000, debug=True)

