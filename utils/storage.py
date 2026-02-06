import json
import os

BASE_DIR = os.path.dirname(f"{os.getcwd()}/data/")
def load_previous(path):
    full_path = os.path.join(BASE_DIR, path)

    if not os.path.exists(full_path):
        return set()

    with open(full_path, "r") as f:
        return set(json.load(f))


def save_current(path, data):
    full_path = os.path.join(BASE_DIR, path)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w") as f:
        json.dump(sorted(list(data)), f, indent=2)
