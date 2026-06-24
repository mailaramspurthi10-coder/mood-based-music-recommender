import json
import os
from typing import Any


class Memory:
    def __init__(self, file_path: str = "memory.json") -> None:
        self.file_path = file_path

        self.history: set[str] = set()
        self.mood_history: list[str] = []
        self.artist_history: set[str] = set()

        self._load()

    def _load(self) -> None:
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, encoding="utf-8") as f:
                    data = json.load(f)

                self.history = set(data.get("history", []))
                self.mood_history = data.get("moods", [])
                self.artist_history = set(data.get("artists", []))

            except Exception:
                self.history = set()
                self.mood_history = []
                self.artist_history = set()

    def _save_file(self) -> None:
        data = {
            "history": list(self.history),
            "moods": self.mood_history,
            "artists": list(self.artist_history),
        }

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def filter_new_songs(self, songs: list[dict[str, Any]]) -> list[dict[str, Any]]:
        new_songs: list[dict[str, Any]] = []

        for s in songs:
            title = s.get("title")

            if title and title not in self.history:
                new_songs.append(s)

        if not new_songs:
            self.history.clear()
            return songs

        return new_songs

    def save(self, mood: str, songs: list[dict[str, Any]]) -> None:
        self.mood_history.append(mood)

        if len(self.mood_history) > 50:
            self.mood_history = self.mood_history[-50:]

        for s in songs:
            title = s.get("title")
            artist = s.get("artist")

            if title:
                self.history.add(title)

            if artist:
                self.artist_history.add(artist)

        self._save_file()

    def clear(self) -> None:
        self.history.clear()
        self.mood_history = []
        self.artist_history.clear()
        self._save_file()
