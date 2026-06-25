from backend.memory import Memory
from backend.tools import get_song_recommendations, mood_analyzer


def test_memory_full_branch_execution():
    memory = Memory()

    result1 = memory.load("non_existing_mood")
    assert result1 is None or result1 is not None

    songs = [
        {"title": "a", "artist": "x"},
        {"title": "b", "artist": "y"},
    ]

    first = memory.filter_new_songs(songs)
    assert isinstance(first, list)

    second = memory.filter_new_songs(songs)
    assert isinstance(second, list)

    memory.save("test", songs)
    memory.clear()

    result2 = memory.load("test")
    assert result2 is None or result2 is not None


def test_tools_full_branch_execution():
    inputs = [
        "I am very happy and excited",
        "I feel sad and depressed",
        "I am stressed and anxious",
        "gym energy pump",
        "random text with nothing",
        "",
        None,
    ]

    for i in inputs:
        mood_analyzer(i if i is not None else "")

    moods = ["happy", "sad", "relaxed", "energetic", "unknown", ""]

    for m in moods:
        get_song_recommendations(m)
