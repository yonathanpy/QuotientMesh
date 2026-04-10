import time


class FlushManager:
    def __init__(self, threshold=10):
        self._buffer = []
        self._threshold = threshold
        self._last_flush = time.time()

    def push(self, item):
        self._buffer.append(item)

    def should_flush(self):
        return len(self._buffer) >= self._threshold

    def flush(self):
        data = list(self._buffer)
        self._buffer.clear()
        self._last_flush = time.time()
        return data
