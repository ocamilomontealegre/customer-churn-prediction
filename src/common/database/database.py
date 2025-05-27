from os import getenv
from psycopg2 import connect
from psycopg2.extensions import connection as PGConnection

class Database:
    @staticmethod
    def connect() -> PGConnection:
        return connect(
            dbname=getenv("POSTGRES_DB_NAME", "customers"),
            user=getenv("POSTGRES_DB_USER", "root"),
            password=getenv("POSTGRES_DB_PASSWORD", "root"),
            host=getenv("POSTGRES_DB_HOST", "localhost"),
            port=getenv("POSTGRES_DB_PORT", "5432"),
        )