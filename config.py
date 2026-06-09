import os
import psycopg2

def connect_db():
    database_url = os.getenv("DATABASE_URL")

    # Kalau di Railway
    if database_url:
        return psycopg2.connect(database_url)

    # Kalau di laptop lokal
    return psycopg2.connect(
        host="localhost",
        database="lelang_db",
        user="postgres",
        password="admin",
        port=5432,
        options="-c timezone=Asia/Jakarta"
    )

def get_cursor():
    conn = connect_db()
    return conn, conn.cursor()