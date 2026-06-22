"""Entry point for the Mood-Based Music Recommendation project."""

from agent import MusicRecommendationAgent
from memory import get_memory


def print_welcome():
    print("\nWelcome to Mood-Based Music Recommendation!")
    print("Tell the system how you are feeling, and it will suggest songs based on your mood.")
    print("Type 'quit' or 'exit' to stop.\n")


def ask_optional(prompt):
    answer = input(prompt).strip()
    return answer if answer else None


def main():
    agent = MusicRecommendationAgent()
    user_id = "default_user"
    print_welcome()

    while True:
        mood_text = input("User mood: ").strip()
        if mood_text.lower() in ["quit", "exit"]:
            print("Goodbye! Keep listening to music that makes you feel better.")
            break

        favorite_genre = ask_optional("Favorite genre (optional): ")
        favorite_artist = ask_optional("Favorite artist (optional): ")

        user_memory = get_memory(user_id)
        print("\nDetecting mood and personalizing your recommendations...")

        recommendation = agent.recommend(
            mood_text,
            user_id=user_id,
            favorite_genre=favorite_genre,
            favorite_artist=favorite_artist,
            user_memory=user_memory,
        )

        print(f"\nMood detected: {recommendation['mood'].capitalize()}")
        print("Recommendations:")
        for index, song in enumerate(recommendation["songs"], start=1):
            print(f"- {song['title']} by {song['artist']} ({song['reason']})")

        print("\nYour preferences and history are saved for more personal songs next time.\n")


if __name__ == "__main__":
    main()
