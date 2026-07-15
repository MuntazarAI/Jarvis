import json
import shutil
from pathlib import Path

DATA_DIR = Path("data")
MEMORY_FILE = DATA_DIR / "memory.json"
BACKUP_FILE = DATA_DIR / "memory_backup.json"


def default_memory():
    return {
        "profile": {},
        "preferences": {},
        "pets": {},
        "projects": [],
        "goals": [],
        "notes": [],
        "reminders": []
    }


def load_memory():
    DATA_DIR.mkdir(exist_ok=True)

    if not MEMORY_FILE.exists():
        memory = default_memory()
        save_memory(memory)
        return memory

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:
        memory = default_memory()
        save_memory(memory)
        return memory


def save_memory(memory):
    DATA_DIR.mkdir(exist_ok=True)

    if MEMORY_FILE.exists():
        shutil.copy(MEMORY_FILE, BACKUP_FILE)

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4, ensure_ascii=False)


def merge_memory(old, new):
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


def remember(new_memory):
    if not new_memory:
        return

    memory = load_memory()
    memory = merge_memory(memory, new_memory)
    save_memory(memory)


def recall():
    return load_memory()


def forget(category, key):
    memory = load_memory()

    if category in memory and isinstance(memory[category], dict):
        memory[category].pop(key, None)

    save_memory(memory)


def search(keyword):
    """
    Search both memory keys and memory values.
    """

    keyword = keyword.lower().strip()

    memory = load_memory()
    results = []

    def walk(obj, path=""):

        if isinstance(obj, dict):

            for key, value in obj.items():

                new_path = f"{path}.{key}" if path else key

                # Search the key/path
                if keyword in new_path.lower():
                    results.append({
                        "path": new_path,
                        "value": value
                    })

                # Continue searching inside the value
                walk(value, new_path)

        elif isinstance(obj, list):

            for i, item in enumerate(obj):
                walk(item, f"{path}[{i}]")

        else:

            # Search the value
            if keyword in str(obj).lower():
                results.append({
                    "path": path,
                    "value": obj
                })

    walk(memory)

    return results

def reset_memory():
    save_memory(default_memory())
