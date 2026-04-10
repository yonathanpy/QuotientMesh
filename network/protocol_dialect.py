import random


class ProtocolDialect:
    def __init__(self):
        self._dialects = ["http/1.1", "http/2", "ssh-2.0", "dns"]

    async def initialize(self):
        return True

    def mutate(self, payload: dict):
        payload["dialect"] = random.choice(self._dialects)
        payload["entropy_tag"] = random.randint(1000, 9999)
        return payload
