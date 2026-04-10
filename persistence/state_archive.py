import json
import os


class StateArchive:
    def __init__(self, path="archive.json"):
        self._path = path
        self._buffer = []

    def append(self, state: dict):
        self._buffer.append(state)

        if len(self._buffer) >= 20:
            self.flush()

    def flush(self):
        if not self._buffer:
            return

        if not os.path.exists(self._path):
            with open(self._path, "w") as f:
                json.dump([], f)

        with open(self._path, "r+") as f:
            data = json.load(f)
            data.extend(self._buffer)
            f.seek(0)
            json.dump(data, f, indent=2)

        self._buffer.clear()
