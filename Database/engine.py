from os import getenv

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

engine = create_engine(
    '{DB}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'.format(
        DB=getenv("DB"),
        DB_USER=getenv("DB_USER"),
        DB_PASS=getenv("DB_PASS"),
        DB_HOST=getenv("DB_HOST"),
        DB_PORT=getenv("DB_PORT"),
        DB_NAME=getenv("DB_NAME")
    ), echo=True
)
