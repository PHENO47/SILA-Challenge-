import sqlite3
import os

# dossier de stockage
DATA_FOLDER = "data"

# chemin base de données
DB_PATH = os.path.join(DATA_FOLDER, "database.db")


def init_db():

    # créer dossier data automatiquement
    os.makedirs(DATA_FOLDER, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price TEXT,
        link TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_data(df):

    conn = sqlite3.connect(DB_PATH)

    df.to_sql("products", conn, if_exists="append", index=False)

    conn.close()