from os import environ
from psycopg2 import connect
from pandas import read_csv
from dotenv import load_dotenv

load_dotenv()


def load_data():
    df = read_csv("data/raw/Telco_Customer_Churn.csv")

    connection = connect(
        dbname=environ.get("POSTGRES_DB_NAME"),
        user=environ.get("POSTGRES_DB_USER"),
        password=environ.get("POSTGRES_DB_PASSWORD"),
        host=environ.get("POSTGRES_DB_HOST"),
        port=environ.get("POSTGRES_DB_PORT"),
    )
    cursor = connection.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO customers (
                customerID, gender, SeniorCitizen, Partner, Dependents, tenure,
                PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup,
                DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract,
                PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Churn
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))

    connection.commit()
    cursor.close()
    connection.close()

    print("✅ Data loaded successfully!")
