from bot.database import init_db
from bot.scheduler import start

def main():

    print("\n=== BOT AUTOMATISATION WEB ===\n")

    url = input("Entrer l'URL du site à scraper : ")

    interval = int(input("Intervalle de scraping (minutes) : "))

    init_db()

    start(url, interval)

if __name__ == "__main__":
    main()