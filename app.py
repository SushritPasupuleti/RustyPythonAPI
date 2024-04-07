import psycopg2
import os
from robyn import Robyn
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_HOST = "localhost"
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = "5432"

conn = psycopg2.connect(
    database=DB_NAME, host=DB_HOST, user=DB_USER, password=DB_PASS, port=DB_PORT
)

app = Robyn(__file__)

# create a route to fetch all users
@app.get("/users")
def get_users():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    all_users = cursor.fetchall()
    return {"users": all_users}


@app.get("/")
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8080)
