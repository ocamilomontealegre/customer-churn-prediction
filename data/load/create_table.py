from os import environ
from psycopg2 import connect
from dotenv import load_dotenv

load_dotenv()

def create_table():
    with open("data/load/query.sql", "r") as f:
        create_table_sql = f.read()

    try:
        connection = connect(
            dbname=environ.get("POSTGRES_DB_NAME"),
            user=environ.get("POSTGRES_DB_USER"),
            password=environ.get("POSTGRES_DB_PASSWORD"),
            host=environ.get("POSTGRES_DB_HOST"),
            port=environ.get("POSTGRES_DB_PORT"),
        )
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        connection.commit()
        cursor.close()
        connection.close()
        print("✅ Table created successfully!")
    except Exception as e:
        print("❌ Failed to create table: ", e)
