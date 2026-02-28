import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential

def async_retry():
    return retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True,
    )

class RateLimiter:
    def __init__(self, calls_per_second):
        self._semaphore = asyncio.Semaphore(calls_per_second)

    async def __aenter__(self):
        await self._semaphore.acquire()

    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.sleep(1)
        self._semaphore.release()