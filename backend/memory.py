import json
import os


class Memory:
    def __init__(self, file_path="memory.json"):
        self.file_path = file_path

        self.history = set()
        self.mood_history = []
        self.artist_history = set()

        self._load()

    def _load(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path) as f:
                    data = json.load(f)

                self.history = set(data.get("history", []))
                self.mood_history = data.get("moods", [])
                self.artist_history = set(data.get("artists", []))

            except Exception:
                self.history = set()
                self.mood_history = []
                self.artist_history = set()

    def _save_file(self):
        data = {
            "history": list(self.history),
            "moods": self.mood_history,
            "artists": list(self.artist_history),
        }

        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def filter_new_songs(self, songs):
        new_songs = []

        for s in songs:
            title = s.get("title")

            if title and title not in self.history:
                new_songs.append(s)

        # ✅ IMPORTANT FIX: if all songs are repeated, reset cycle
        if not new_songs:
            self.history.clear()
            return songs

        return new_songs

    def save(self, mood, songs):
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

    def clear(self):
        self.history.clear()
        self.mood_history = []
        self.artist_history.clear()
        self._save_file()
