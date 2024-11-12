from sqlalchemy import create_engine
import pandas as pd

def fetch_data():
    engine = create_engine('mssql+pymssql://username:password@server/database')
    query = "SELECT * FROM Patients"
    df = pd.read_sql(query, engine)
    return df

if __name__ == "__main__":
    data = fetch_data()
    data.to_csv("patients_data.csv", index=False)