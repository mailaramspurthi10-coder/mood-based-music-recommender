"""Helper tools for mood detection and song recommendations."""

MOOD_KEYWORDS = {
    "happy": ["happy", "joy", "good", "great", "excited", "optimistic"],
    "sad": ["sad", "down", "blue", "unhappy", "depressed", "melancholy"],
    "relaxed": ["relaxed", "calm", "chill", "peaceful", "serene", "rested"],
    "energetic": ["energetic", "pumped", "active", "alive", "lively", "excited"],
    "stressed": ["stressed", "anxious", "worried", "tense", "nervous", "overwhelmed"],
}

MOOD_SONG_LIBRARY = {
    "happy": [
        {
            "title": "Sunshine Smile",
            "artist": "Bright Beats",
            "genre": "pop",
            "reason": "uplifting melody and cheerful lyrics",
        },
        {
            "title": "Warm Morning",
            "artist": "Easy Tunes",
            "genre": "acoustic",
            "reason": "light rhythm that feels joyful",
        },
    ],
    "sad": [
        {
            "title": "Blue Reflections",
            "artist": "Soul Echo",
            "genre": "indie",
            "reason": "gentle piano and emotional vocals",
        },
        {
            "title": "Rainy Window",
            "artist": "Quiet Strings",
            "genre": "ambient",
            "reason": "soft soundscapes to support calm release",
        },
    ],
    "relaxed": [
        {
            "title": "Quiet Breeze",
            "artist": "Calm Collective",
            "genre": "ambient",
            "reason": "slow tempo and soothing atmosphere",
        },
        {
            "title": "Evening Glow",
            "artist": "Sofa Sessions",
            "genre": "chill",
            "reason": "warm instrumentation that eases tension",
        },
    ],
    "energetic": [
        {
            "title": "Running Free",
            "artist": "Power Pulse",
            "genre": "electronic",
            "reason": "fast beat and motivating energy",
        },
        {
            "title": "Jump Start",
            "artist": "Firebeats",
            "genre": "pop",
            "reason": "high tempo and strong rhythm to lift your mood",
        },
    ],
    "stressed": [
        {
            "title": "Soft Horizon",
            "artist": "Ease Ensemble",
            "genre": "ambient",
            "reason": "calming textures to reduce stress",
        },
        {
            "title": "Gentle Waves",
            "artist": "Ocean Pulse",
            "genre": "relaxation",
            "reason": "steady, soothing sound that helps you breathe",
        },
    ],
}


def mood_analyzer(text):
    """Analyze text and return one of the supported moods."""
    text_lower = text.lower()
    mood_scores = {mood: 0 for mood in MOOD_KEYWORDS}

    for mood, keywords in MOOD_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text_lower:
                mood_scores[mood] += 1

    best_mood = max(mood_scores, key=mood_scores.get)
    if mood_scores[best_mood] == 0:
        return "relaxed"
    return best_mood


def get_song_recommendations(mood, user_memory=None, favorite_genre=None, favorite_artist=None):
    """Return a list of songs that match the mood and avoid repeats."""
    available_songs = MOOD_SONG_LIBRARY.get(mood, [])
    if not available_songs:
        return []

    history = []
    if user_memory:
        history = user_memory.get("history", [])

    filtered = []
    for song in available_songs:
        if song["title"] in history:
            continue
        if favorite_genre and song["genre"].lower() != favorite_genre.lower():
            continue
        if favorite_artist and song["artist"].lower() != favorite_artist.lower():
            continue
        filtered.append(song)

    if not filtered:
        filtered = [song for song in available_songs if song["title"] not in history]

    if not filtered:
        filtered = available_songs

    return filtered[:2]
