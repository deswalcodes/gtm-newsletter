import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def save_newsletter(edition, title, content):
    try:
        conn = psycopg2.connect(os.getenv("NEON_DB_URL"))
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO newsletters (edition, title, content) VALUES (%s, %s, %s)",
            (edition, title, content)
        )
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Saved to Neon Postgres")
    except Exception as e:
        print("[Error saving to Neon]:", e)
