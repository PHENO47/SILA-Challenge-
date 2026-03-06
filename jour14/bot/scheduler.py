from apscheduler.schedulers.blocking import BlockingScheduler
from bot.scraper import get_page
from bot.parser import parse_data
from bot.database import save_data


def start(url, interval):

    def job():

        print("\nScraping en cours...")

        html = get_page(url)

        df = parse_data(html)

        if not df.empty:

            save_data(df)

            # export CSV
            df.to_csv("data/export.csv", mode="a", index=False, header=False)

            print("Données trouvées :", len(df))

        else:

            print("Aucune donnée trouvée")

    scheduler = BlockingScheduler()

    scheduler.add_job(job, "interval", minutes=interval)

    print(f"Bot lancé : scraping toutes les {interval} minutes")

    scheduler.start()