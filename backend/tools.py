import random


# -------------------------
# MOOD ANALYZER (text → mood)
# -------------------------
def mood_analyzer(text: str):
    text = text.lower()

    if any(word in text for word in ["sad", "cry", "depress"]):
        return "sad"

    elif any(word in text for word in ["happy", "joy", "excited"]):
        return "happy"

    elif any(word in text for word in ["stress", "anxious", "calm"]):
        return "relaxed"

    elif any(word in text for word in ["energy", "energetic", "gym", "pump"]):
        return "energetic"

    else:
        return "relaxed"


# -------------------------
# SONG DATABASE
# -------------------------
SONGS = {
    "happy": [
        {"title": "Happy", "artist": "Pharrell Williams"},
        {"title": "Can't Stop the Feeling", "artist": "Justin Timberlake"},
        {"title": "Uptown Funk", "artist": "Mark Ronson"},
        {"title": "Kesariya", "artist": "Arijit Singh"},
        {"title": "Butta Bomma", "artist": "Armaan Malik"},
        {"title": "On Top of the World", "artist": "Imagine Dragons"},
        {"title": "Love You Zindagi", "artist": "Amit Trivedi"},
    ],
    "sad": [
        {"title": "Someone Like You", "artist": "Adele"},
        {"title": "Let Her Go", "artist": "Passenger"},
        {"title": "Fix You", "artist": "Coldplay"},
        {"title": "Adiga Adiga", "artist": "Sid Sriram"},
        {"title": "Agar Tum Saath Ho", "artist": "Alka Yagnik"},
        {"title": "Channa Mereya", "artist": "Arijit Singh"},
        {"title": "Tears in Heaven", "artist": "Eric Clapton"},
    ],
    "relaxed": [
        {"title": "Weightless", "artist": "Marconi Union"},
        {"title": "Perfect", "artist": "Ed Sheeran"},
        {"title": "Bloom", "artist": "The Paper Kites"},
        {"title": "Raataan Lambiyan", "artist": "Jubin Nautiyal"},
        {"title": "Inkem Inkem", "artist": "Sid Sriram"},
        {"title": "Night Owl", "artist": "Galimatias"},
        {"title": "Ocean Eyes", "artist": "Billie Eilish"},
    ],
    "energetic": [
        {"title": "Believer", "artist": "Imagine Dragons"},
        {"title": "Thunder", "artist": "Imagine Dragons"},
        {"title": "Naatu Naatu", "artist": "Rahul Sipligunj"},
        {"title": "Malhari", "artist": "Vishal Dadlani"},
        {"title": "Eye of the Tiger", "artist": "Survivor"},
        {"title": "Till I Collapse", "artist": "Eminem"},
        {"title": "Jai Ho", "artist": "A.R. Rahman"},
    ],
}


# -------------------------
# SONG RECOMMENDER
# -------------------------
def get_song_recommendations(mood: str, provider: str = "none"):
    mood = mood.lower().strip()  # clean input

    songs = SONGS.get(mood, []).copy()

    # safety: if mood not found
    if not songs:
        return SONGS["relaxed"].copy()

    # shuffle for variety
    random.shuffle(songs)

    return songs
