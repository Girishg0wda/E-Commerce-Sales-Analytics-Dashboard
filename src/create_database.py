import pandas as pd
import sqlite3

df = pd.read_csv(
    "data/processed/cleaned_sales_data.csv"
)

conn = sqlite3.connect(
    "database/sales.db"
)

df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database created successfully!")