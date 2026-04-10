import random


class SurfaceSynthesis:
    def __init__(self):
        self._profiles = []

    async def construct(self):
        self._profiles = [
            {"latency": 10, "jitter": 2, "protocol": "http"},
            {"latency": 40, "jitter": 10, "protocol": "ssh"},
            {"latency": 5, "jitter": 1, "protocol": "dns"},
        ]

    def project(self, state: str):
        profile = random.choice(self._profiles)
        return {
            "state_fragment": state[:16],
            "latency": profile["latency"] + random.randint(0, profile["jitter"]),
            "protocol": profile["protocol"]
        }
