from typing import Any

from .memory import Memory
from .tools import get_song_recommendations, mood_analyzer


class MusicAgent:
    def __init__(self) -> None:
        self.memory = Memory()

    def get_recommendations(self, mood: str) -> list[dict[str, Any]]:
        """
        Returns song recommendations for a given mood.
        Returns empty list if mood is not supported.
        """

        # optional: validate mood using analyzer (if your tool supports it)
        analyzed_mood = mood_analyzer(mood)

        songs = get_song_recommendations(analyzed_mood)

        if not songs:
            return []

        # optionally store in memory
        self.memory.save(mood=analyzed_mood, songs=songs)

        return songs
