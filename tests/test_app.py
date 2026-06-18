from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from backend.app import app  # noqa: E402


def test_home_returns_running_message() -> None:
    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    assert b"Mood-Based Music Recommender" in response.data


def test_recommend_happy_returns_songs() -> None:
    with app.test_client() as client:
        response = client.post("/recommend", json={"mood": "happy"})

    assert response.status_code == 200
    data = response.get_json()
    assert data is not None
    assert data["mood"] == "happy"
    assert any(song["title"] == "Happy" for song in data["songs"])


def test_recommend_unknown_mood_returns_404() -> None:
    with app.test_client() as client:
        response = client.post("/recommend", json={"mood": "unknown"})

    assert response.status_code == 404
    assert response.get_json() == {"error": "Mood not found"}


def test_recommend_missing_mood_returns_400() -> None:
    with app.test_client() as client:
        response = client.post("/recommend", json={})

    assert response.status_code == 400
    assert response.get_json() == {"error": "Mood is required"}
