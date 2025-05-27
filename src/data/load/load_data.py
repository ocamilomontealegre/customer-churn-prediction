from pathlib import Path
from pandas import read_csv # type: ignore
from src.common.database.database import Database


def load_data():
    csv_path = Path(__file__).parent.parent.parent / "data" / "raw" / "Telco_Customer_Churn.csv"
    df = read_csv(csv_path)

    connection = Database.connect()
    cursor = connection.cursor()

    for _, row in df.iterrows(): # type: ignore
        cursor.execute("""
            INSERT INTO customers (
                customerID, gender, SeniorCitizen, Partner, Dependents, tenure,
                PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup,
                DeviceProtection, TechSupport, StreamingTV, StreamingMovies, Contract,
                PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges, Churn
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(row)) # type: ignore

    connection.commit()
    cursor.close()
    connection.close()

    print("✅ Data loaded successfully!")
