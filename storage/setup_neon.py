import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(os.getenv("NEON_DB_URL"))
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS newsletters (
    id SERIAL PRIMARY KEY,
    edition INT NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
)
""")

conn.commit()
cur.close()
conn.close()
print("✅ Neon table created")
