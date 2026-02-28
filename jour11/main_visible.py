import asyncio
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from client import APIClient

console = Console()


def validate_country(code: str) -> str:
    """
    Vérifie que le code pays contient exactement 2 lettres.
    """
    code = code.strip().lower()
    if len(code) != 2:
        console.print("[red]Code pays invalide. Utilisation par défaut : us[/red]")
        return "us"
    return code


async def main():
    console.print("\n[bold cyan]=== Async API Dashboard PRO ===[/bold cyan]\n")

    # 🔑 Clés API visibles
    weather_key = input("Clé OpenWeather: ").strip()
    news_key = input("Clé NewsAPI: ").strip()

    # 👤 Infos utilisateur
    username = input("Username GitHub: ").strip()
    city = input("Ville: ").strip()
    country = validate_country(input("Code pays (ex: us, fr, cm): "))
    category = input("Catégorie news: ").strip().lower()

    async with APIClient(weather_key, news_key) as api:

        tasks = [
            api.fetch_github(username),
            api.fetch_weather(city),
            api.fetch_news(country, category),
        ]

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}")
        ) as progress:

            progress.add_task(description="Chargement des APIs...", total=None)
            github_data, weather_data, news_data = await asyncio.gather(*tasks)

        table = Table(title="🌍 Résultats API")
        table.add_column("Source", style="cyan", no_wrap=True)
        table.add_column("Résultat", style="magenta")

        # GitHub
        if isinstance(github_data, list):
            total_repos = len(github_data)
            total_stars = sum(repo.get("stargazers_count", 0) for repo in github_data)
            github_result = f"{total_repos} repos | ⭐ {total_stars} stars"
        else:
            github_result = github_data.get("message", "Erreur GitHub")

        # Météo
        if "main" in weather_data:
            temp = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            description = weather_data["weather"][0]["description"]
            weather_result = f"{temp}°C | 💧 {humidity}% | {description}"
        else:
            weather_result = weather_data.get("message", "Erreur météo")

        # News
        if "articles" in news_data and len(news_data["articles"]) > 0:
            article = news_data["articles"][0]
            title = article.get("title", "No title")
            source = article.get("source", {}).get("name", "Unknown")
            news_result = f"{title} ({source})"
        else:
            news_result = news_data.get("message", "Erreur News")

        table.add_row("GitHub", github_result)
        table.add_row("Météo", weather_result)
        table.add_row("Top News", news_result)

        console.print(table)


if __name__ == "__main__":
    asyncio.run(main())