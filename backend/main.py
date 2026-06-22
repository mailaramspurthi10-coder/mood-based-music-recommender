from agent import MusicAgent

agent = MusicAgent()

print("🎵 Mood Music CLI")

while True:
    user_input = input("\nEnter mood (or 'exit'): ")

    if user_input == "exit":
        break

    result = agent.run(user_input)

    print("\nMood detected:", result["mood_detected"])
    print("Recommendations:")

    for s in result["songs"]:
        print(f"- {s['title']} by {s['artist']}")
        print("  Reason:", s["reason"])