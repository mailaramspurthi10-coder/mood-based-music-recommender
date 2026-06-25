import random
from typing import Any


def mood_analyzer(text: str) -> str:
    if not text:
        return "relaxed"

    text = text.lower()

    if any(word in text for word in ["sad", "cry", "depress"]):
        return "sad"
    if any(word in text for word in ["happy", "joy", "excited"]):
        return "happy"
    if any(word in text for word in ["stress", "anxious", "calm"]):
        return "relaxed"
    if any(word in text for word in ["energy", "energetic", "gym", "pump"]):
        return "energetic"

    return "relaxed"


SONGS: dict[str, list[dict[str, str]]] = {
    "happy": [
        {"title": "Happy", "artist": "Pharrell Williams"},
        {"title": "Uptown Funk", "artist": "Mark Ronson"},
    ],
    "sad": [
        {"title": "Someone Like You", "artist": "Adele"},
        {"title": "Fix You", "artist": "Coldplay"},
    ],
    "relaxed": [
        {"title": "Weightless", "artist": "Marconi Union"},
        {"title": "Ocean Eyes", "artist": "Billie Eilish"},
    ],
    "energetic": [
        {"title": "Believer", "artist": "Imagine Dragons"},
        {"title": "Naatu Naatu", "artist": "Rahul Sipligunj"},
    ],
}


def get_song_recommendations(mood: str, provider: str = "none") -> list[dict[str, Any]]:
    _ = provider

    if not mood:
        return SONGS["relaxed"].copy()

    mood = mood.lower().strip()

    songs = SONGS.get(mood)

    # 🔥 important branch coverage
    if not songs:
        return SONGS["relaxed"].copy()

    songs = songs.copy()

    random.shuffle(songs)

    return songs
