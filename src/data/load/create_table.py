from pathlib import Path
from src.common.database.database import Database

def create_table():
    query_path = Path(__file__).parent / "query.sql"
    
    with open(query_path, "r") as f:
        create_table_sql = f.read()

    try:
        connection = Database.connect()
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
        connection.commit()
        cursor.close()
        connection.close()
        print("✅ Table created successfully!")
    except Exception as e:
        print("❌ Failed to create table: ", e)
