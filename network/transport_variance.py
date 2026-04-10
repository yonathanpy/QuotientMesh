import random
import time


class TransportVariance:
    def __init__(self):
        self._baseline = {
            "latency": (5, 50),
            "packet_loss": (0.0, 0.05),
            "burst": (1, 5)
        }

    def apply(self, payload: dict):
        latency = random.randint(*self._baseline["latency"])
        loss = random.uniform(*self._baseline["packet_loss"])
        burst = random.randint(*self._baseline["burst"])

        payload["latency"] = latency
        payload["packet_loss"] = loss
        payload["burst_factor"] = burst
        payload["timestamp"] = time.time()

        return payload
