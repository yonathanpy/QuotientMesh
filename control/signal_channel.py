import asyncio


class SignalChannel:
    def __init__(self):
        self._queue = asyncio.Queue()

    async def emit(self, signal: dict):
        await self._queue.put(signal)

    async def consume(self):
        return await self._queue.get()

    async def drain(self):
        items = []
        while not self._queue.empty():
            items.append(await self._queue.get())
        return items
