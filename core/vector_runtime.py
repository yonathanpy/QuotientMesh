import asyncio
import time
from typing import Dict, Any
from core.state_entropy import StateEntropy
from core.surface_synthesis import SurfaceSynthesis


class VectorRuntime:
    def __init__(self):
        self.entropy = StateEntropy()
        self.surface = SurfaceSynthesis()
        self.active_vectors: Dict[str, Any] = {}
        self._running = False

    async def initialize(self):
        await self.entropy.prime()
        await self.surface.construct()
        self._running = True

    async def register_vector(self, key: str, metadata: Dict[str, Any]):
        self.active_vectors[key] = {
            "meta": metadata,
            "state": self.entropy.sample(),
            "created": time.time()
        }

    async def evolve(self, key: str):
        vector = self.active_vectors.get(key)
        if not vector:
            return None

        next_state = self.entropy.transform(vector["state"])
        projection = self.surface.project(next_state)

        vector["state"] = next_state
        return projection

    async def run_loop(self):
        while self._running:
            for key in list(self.active_vectors.keys()):
                await self.evolve(key)
            await asyncio.sleep(0.05)
