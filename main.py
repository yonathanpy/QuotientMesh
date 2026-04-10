import asyncio
from control.runtime_surface import RuntimeSurface


async def main():
    runtime = RuntimeSurface()
    await runtime.start()

    await runtime.ingest("node-1", {"origin": "test"})
    await runtime.ingest("node-2", {"origin": "test"})

    await runtime.loop()


if __name__ == "__main__":
    asyncio.run(main())
