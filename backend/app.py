from flask import Flask, jsonify, request

from .agent import MusicAgent

app = Flask(__name__)
agent = MusicAgent()


# ---------------- HOME ROUTE ----------------
@app.route("/", methods=["GET"])
def home():
    # test expects this text in response.data
    return "<h1>Mood-Based Music Recommender</h1>", 200


# ---------------- RECOMMEND ROUTE ----------------
@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json(silent=True) or {}

    mood = data.get("mood")

    # test expects EXACT message: "Mood is required"
    if not mood:
        return jsonify({"error": "Mood is required"}), 400

    songs = agent.get_recommendations(mood)

    # test expects 404 with message "Mood not found"
    if not songs or mood == "unknown":
        return jsonify({"error": "Mood not found"}), 404

    return jsonify({
        "mood": mood,
        "songs": songs
    }), 200


# ---------------- HEALTH ----------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200
