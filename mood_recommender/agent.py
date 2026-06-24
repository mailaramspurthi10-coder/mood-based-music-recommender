"""Core agent logic for the mood-based music recommender."""

from memory import update_memory
from tools import get_song_recommendations, mood_analyzer


class MusicRecommendationAgent:
    """A simple simulated AI agent for song recommendations."""

    def __init__(self):
        self.name = "MoodMusicAgent"
        self.description = (
            "Simulated Google ADK-style agent that detects mood and selects songs "
            "based on user history and preferences."
        )

    def recommend(
        self,
        user_text,
        user_id="default_user",
        favorite_genre=None,
        favorite_artist=None,
        user_memory=None,
    ):
        """Recommend songs based on detected mood and stored user memory."""
        mood = mood_analyzer(user_text)
        songs = get_song_recommendations(
            mood,
            user_memory=user_memory,
            favorite_genre=favorite_genre,
            favorite_artist=favorite_artist,
        )

        if songs:
            recommended_titles = [song["title"] for song in songs]
            update_memory(
                user_id=user_id,
                favorite_genre=favorite_genre,
                favorite_artist=favorite_artist,
                recommended_titles=recommended_titles,
            )

        return {
            "agent_name": self.name,
            "mood": mood,
            "songs": songs,
        }
