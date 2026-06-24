"""Memory helpers for storing and retrieving user preferences and history."""

import json
from pathlib import Path

USER_MEMORY_FILE = Path(__file__).parent / "user_memory.json"


def _load_storage():
    if not USER_MEMORY_FILE.exists():
        return {}
    try:
        with USER_MEMORY_FILE.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError):
        return {}


def _save_storage(storage):
    with USER_MEMORY_FILE.open("w", encoding="utf-8") as handle:
        json.dump(storage, handle, indent=2)


def get_memory(user_id="default_user"):
    """Return the stored memory for a user."""
    storage = _load_storage()
    if user_id not in storage:
        storage[user_id] = {
            "history": [],
            "preferences": {
                "favorite_genre": None,
                "favorite_artist": None,
            },
        }
    return storage[user_id]


def update_memory(
    user_id="default_user",
    favorite_genre=None,
    favorite_artist=None,
    recommended_titles=None,
):
    """Update user memory with preferences and recommended songs."""
    storage = _load_storage()
    if user_id not in storage:
        storage[user_id] = {
            "history": [],
            "preferences": {
                "favorite_genre": None,
                "favorite_artist": None,
            },
        }

    user_record = storage[user_id]
    if favorite_genre:
        user_record["preferences"]["favorite_genre"] = favorite_genre
    if favorite_artist:
        user_record["preferences"]["favorite_artist"] = favorite_artist

    if recommended_titles:
        for title in recommended_titles:
            if title not in user_record["history"]:
                user_record["history"].append(title)

    _save_storage(storage)
    return user_record
