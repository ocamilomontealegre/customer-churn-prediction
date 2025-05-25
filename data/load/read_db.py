from os import environ
from psycopg2 import connect
from pandas import read_sql


def read_db():
    connection = connect(
        dbname=environ["POSTGRES_DB_NAME"],
        user=environ["POSTGRES_DB_USER"],
        password=environ["POSTGRES_DB_PASSWORD"],
        host=environ["POSTGRES_DB_HOST"],
        port=environ["POSTGRES_DB_PORT"]
    )

    df = read_sql(f"SELECT * FROM {environ["POSTGRES_DB_NAME"]}", con=connection) # type: ignore
    print(df.head())
    connection.close()