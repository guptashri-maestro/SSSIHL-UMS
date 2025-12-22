import os
from core.aws import get_secret
from sqlalchemy.engine import URL
from dotenv import load_dotenv

load_dotenv()

SECRET_NAME = os.getenv("SECRET_NAME")

secrets = get_secret(SECRET_NAME)

def get_database_url() -> str:
    username = secrets["username"]
    password = secrets["password"]
    host = secrets["host"]
    port = secrets["port"]
    dbname = secrets["dbname"]
    return URL.create(
        drivername="postgresql+asyncpg",
        username=username,
        password=password,  # safe even with @, :, /
        host=host,
        port=int(port),
        database=dbname,
    ).render_as_string(hide_password=False)