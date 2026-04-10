import asyncio


class RuntimeGuard:
    def __init__(self, interval=0.1):
        self._interval = interval
        self._active = False

    async def start(self):
        self._active = True

    async def stop(self):
        self._active = False

    async def cycle(self, fn):
        while self._active:
            try:
                await fn()
            except Exception:
                pass
            await asyncio.sleep(self._interval)
