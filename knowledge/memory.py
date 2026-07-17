import json
import shutil
import re
from pathlib import Path

DATA_DIR = Path("data")
MEMORY_FILE = DATA_DIR / "memory.json"
BACKUP_FILE = DATA_DIR / "memory_backup.json"
class Memory:

    def __init__(self):
        DATA_DIR.mkdir(exist_ok=True)

    # ----------------------------
    # Default Memory
    # ----------------------------

    def default(self):
        return {
            "profile": {},
            "preferences": {},
            "pets": {},
            "projects": [],
            "goals": [],
            "notes": [],
            "reminders": []
        }

    # ----------------------------
    # Load
    # ----------------------------

    def load(self):

        if not MEMORY_FILE.exists():
            data = self.default()
            self.save(data)
            return data

        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)

        except Exception:
            data = self.default()
            self.save(data)
            return data

    # ----------------------------
    # Save
    # ----------------------------

    def save(self, data):

        if MEMORY_FILE.exists():
            shutil.copy(MEMORY_FILE, BACKUP_FILE)

        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    # ----------------------------
    # Merge
    # ----------------------------

    def merge(self, old, new):

        if not isinstance(new, dict):
            return old

        for key, value in new.items():

            if key not in old:
                old[key] = value
                continue

            if isinstance(value, dict):

                if not isinstance(old[key], dict):
                    old[key] = {}

                for k, v in value.items():
                    if v not in ("", None):
                        old[key][k] = v

            elif isinstance(value, list):

                if not isinstance(old[key], list):
                    old[key] = []

                for item in value:
                    if item not in old[key]:
                        old[key].append(item)

            else:

                if value not in ("", None):
                    old[key] = value

        return old

    # ----------------------------
    # Remember
    # ----------------------------

    def remember(self, new_memory):

        if not new_memory:
            return

        data = self.load()
        data = self.merge(data, new_memory)
        self.save(data)

    # ----------------------------
    # Recall
    # ----------------------------

    def recall(self):
        return self.load()

    # ----------------------------
    # Forget
    # ----------------------------

    def forget(self, category, key):

        data = self.load()

        if category in data and isinstance(data[category], dict):
            data[category].pop(key, None)

        self.save(data)

    # ----------------------------
    # Search (Whole Word Search)
    # ----------------------------
    def search(self, keyword):
        import re

        keyword = keyword.lower().strip()

        data = self.load()

        results = []

        def tokenize(text):
            """
            Split text into searchable words.

            favorite_editor
                -> favorite editor

            profile.favorite_editor
                -> profile favorite editor

            VS Code
                -> vs code
            """

            text = str(text).lower()

            text = text.replace("_", " ")
            text = text.replace(".", " ")
            text = text.replace("-", " ")

            return re.findall(r"[a-z0-9]+", text)

        def walk(obj, path=""):

            if isinstance(obj, dict):

                for k, v in obj.items():

                    new_path = f"{path}.{k}" if path else k

                    if keyword in tokenize(new_path):
                        results.append({
                            "path": new_path,
                            "value": v
                        })

                    walk(v, new_path)

            elif isinstance(obj, list):

                for i, item in enumerate(obj):
                    walk(item, f"{path}[{i}]")

            else:

                if keyword in tokenize(obj):
                    results.append({
                        "path": path,
                        "value": obj
                    })

        walk(data)

        return results

    # ----------------------------
    # Reset
    # ----------------------------

    def reset(self):
        self.save(self.default())


memory = Memory()
