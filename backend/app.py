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
        data = request.get_json()

        # Validate request
        if not data or "mood" not in data:
            return jsonify({"error": "Mood is required"}), 400

        mood_text = data["mood"].strip()
        provider = data.get("provider", "none")

        # -------------------------
        # MAIN AGENT CALL
        # -------------------------
        result = agent.run(mood_text, provider)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
