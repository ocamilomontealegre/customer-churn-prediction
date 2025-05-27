from os import getenv
from pandas import read_sql
from src.common.database.database import Database



def read_db():
    connection = Database.connect()
    df = read_sql(f"SELECT * FROM {getenv("POSTGRES_DB_NAME", 'customers')}", con=connection) # type: ignore
    print(df.head())
    
    connection.close()