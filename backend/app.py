from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

songs = {
    "Happy": [
        {
            "title": "Happy",
            "artist": "Pharrell Williams",
            "link": "https://www.youtube.com/results?search_query=Happy+Pharrell+Williams"
        },
        {
            "title": "Uptown Funk",
            "artist": "Bruno Mars",
            "link": "https://www.youtube.com/results?search_query=Uptown+Funk+Bruno+Mars"
        }
    ],
    "Sad": [
        {
            "title": "Someone Like You",
            "artist": "Adele",
            "link": "https://www.youtube.com/results?search_query=Someone+Like+You+Adele"
        },
        {
            "title": "Let Her Go",
            "artist": "Passenger",
            "link": "https://www.youtube.com/results?search_query=Let+Her+Go+Passenger"
        }
    ],
    "Relaxed": [
        {
            "title": "Weightless",
            "artist": "Marconi Union",
            "link": "https://www.youtube.com/results?search_query=Weightless+Marconi+Union"
        }
    ],
    "Energetic": [
        {
            "title": "Believer",
            "artist": "Imagine Dragons",
            "link": "https://www.youtube.com/results?search_query=Believer+Imagine+Dragons"
        }
    ]
}

@app.route("/")
def home():
    return "🎵 Mood-Based Music API is running!"

@app.route("/recommend/<mood>")
def recommend(mood):
    mood = mood.capitalize()

    if mood not in songs:
        return jsonify({"error": "Mood not found"}), 404

    return jsonify(songs[mood])

if __name__ == "__main__":
    app.run(debug=True)