from flask import Flask, jsonify, render_template, request
from flask.typing import ResponseReturnValue
from flask_cors import CORS

from agent import MusicAgent

app = Flask(__name__)
CORS(app)

agent = MusicAgent()


# -------------------------
# HOME PAGE
# -------------------------
@app.route("/")
def home() -> str:
    return render_template("index.html")


# -------------------------
# RECOMMEND API
# -------------------------
@app.route("/recommend", methods=["POST"])
def recommend() -> ResponseReturnValue:
    try:
        data = request.get_json(silent=True) or {}

        mood_text = data.get("mood", "").strip()
        provider = data.get("provider", "none")

        if not mood_text:
            return jsonify({"error": "Mood is required"}), 400

        result = agent.run(mood_text, provider)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(port=5000, debug=False)