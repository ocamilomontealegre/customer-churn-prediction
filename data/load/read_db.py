from os import environ
from psycopg2 import connect
from pandas import read_sql
from dotenv import load_dotenv

load_dotenv()


def read_db():
    connection = connect(
        dbname=environ.get("POSTGRES_DB_NAME"),
        user=environ.get("POSTGRES_DB_USER"),
        password=environ.get("POSTGRES_DB_PASSWORD"),
        host=environ.get("POSTGRES_DB_HOST"),
        port=environ.get("POSTGRES_DB_PORT"),
    )

    df = read_sql(f"SELECT * FROM {environ["POSTGRES_DB_NAME"]}", con=connection) # type: ignore
    print(df.head())
    connection.close()