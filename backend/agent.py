import random
from typing import Any

from memory import Memory
from tools import get_song_recommendations, mood_analyzer


class MusicAgent:
    def __init__(self) -> None:
        self.memory = Memory()

    def run(self, user_text: str, provider: str = "none") -> dict[str, Any]:
        mood = mood_analyzer(user_text)

        songs = get_song_recommendations(mood, provider)
        songs = songs.copy()

        random.shuffle(songs)

        filtered_songs = self.memory.filter_new_songs(songs)

        if not filtered_songs:
            self.memory.clear()
            filtered_songs = songs

        filtered_songs = filtered_songs[:5]

        self.memory.save(mood, filtered_songs)

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
