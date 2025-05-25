from os import environ
from psycopg2 import connect


def create_table():
    with open("data/load/query.sql", "r") as f:
        create_table_sql = f.read()

    try:
        connection = connect(
            dbname=environ["POSTGRES_DB_NAME"],
            user=environ["POSTGRES_DB_USER"],
            password=environ["POSTGRES_DB_PASSWORD"],
            host=environ["POSTGRES_DB_HOST"],
            port=environ["POSTGRES_DB_PORT"]
        )
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        connection.commit()
        cursor.close()
        connection.close()
        print("✅ Table created successfully!")
    except Exception as e:
        print("❌ Failed to create table: ", e)
