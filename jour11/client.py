import aiohttp
from utils import async_retry, RateLimiter

rate_limiter = RateLimiter(5)


class APIClient:
    """
    Client API asynchrone.
    Les clés API sont injectées dynamiquement au moment de l’instanciation.
    """

    def __init__(self, weather_key, news_key):
        self.session = None
        self.weather_key = weather_key
        self.news_key = news_key

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    # -------------------------
    # GitHub API
    # -------------------------
    @async_retry()
    async def fetch_github(self, username):
        async with rate_limiter:
            url = f"https://api.github.com/users/{username}/repos"
            async with self.session.get(url) as resp:
                return await resp.json()

    # -------------------------
    # OpenWeather API
    # -------------------------
    @async_retry()
    async def fetch_weather(self, city):
        async with rate_limiter:
            url = (
                f"http://api.openweathermap.org/data/2.5/weather?"
                f"q={city}&appid={self.weather_key}&units=metric"
            )
            async with self.session.get(url) as resp:
                return await resp.json()

    # -------------------------
    # NewsAPI
    # -------------------------
    @async_retry()
    async def fetch_news(self, country, category):
        async with rate_limiter:
            url = (
                f"https://newsapi.org/v2/top-headlines?"
                f"country={country}&category={category}&apiKey={self.news_key}"
            )
            async with self.session.get(url) as resp:
                return await resp.json()