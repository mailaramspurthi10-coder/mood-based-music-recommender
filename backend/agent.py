import random

from memory import Memory
from tools import get_song_recommendations, mood_analyzer


class MusicAgent:
    def __init__(self):
        self.memory = Memory()

    def run(self, user_text: str, provider: str = "none"):
        # ---------------------------
        # 1. Mood Detection (NLP layer)
        # ---------------------------
        mood = mood_analyzer(user_text)

        # ---------------------------
        # 2. Get Songs from Tools
        # ---------------------------
        songs = get_song_recommendations(mood, provider)

        # Safety copy (avoid modifying original list)
        songs = songs.copy()

        # Shuffle for variation
        random.shuffle(songs)

        # ---------------------------
        # 3. Memory Filtering (No repeats)
        # ---------------------------
        filtered_songs = self.memory.filter_new_songs(songs)

        # ---------------------------
        # 4. Fallback if everything was already shown
        # ---------------------------
        if not filtered_songs:
            self.memory.clear()
            filtered_songs = songs

        # Limit output for UI stability
        filtered_songs = filtered_songs[:5]

        # ---------------------------
        # 5. Save to Memory
        # ---------------------------
        self.memory.save(mood, filtered_songs)

        # ---------------------------
        # 6. Build Response (Agent output)
        # ---------------------------
        return {
            "mood_detected": mood,
            "provider": provider,
            "songs": [
                {
                    "title": s["title"],
                    "artist": s["artist"],
                    "reason": (
                        f"This song matches your {mood} mood "
                        "and helps improve emotional balance."
                    ),
                }
                for s in filtered_songs
            ],
        }
