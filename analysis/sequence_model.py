class SequenceModel:
    def __init__(self):
        self._history = {}

    def update(self, key: str, event: dict):
        if key not in self._history:
            self._history[key] = []

        self._history[key].append(event)

        if len(self._history[key]) > 50:
            self._history[key].pop(0)

    def pattern_score(self, key: str):
        events = self._history.get(key, [])
        if not events:
            return 0.0

        score = 0.0

        for ev in events:
            if ev.get("protocol") == "ssh":
                score += 0.05
            if ev.get("packet_loss", 0) > 0.03:
                score += 0.02

        return min(score, 1.0)
