import pandas as pd
import sqlite3

DB_PATH = "db/deliveries.db"
CSV_PATH = "data/raw/deliveries_latest.csv"

df = pd.read_csv(CSV_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

insert_query = """
INSERT INTO raw_deliveries (
    delivery_id,
    order_id,
    partner_name,
    customer_city,
    delivery_date,
    delivery_time,
    distance_km,
    delivery_status,
    amount_charged,
    payment_status
)
VALUES (?,?,?,?,?,?,?,?,?,?)
"""

for _, row in df.iterrows():
    cursor.execute(insert_query, (
        row["delivery_id"],
        row["order_id"],
        row["partner_name"],
        row["customer_city"],
        row["delivery_date"],
        row["delivery_time"],
        row["distance_km"],
        row["delivery_status"],
        row["amount_charged"],
        row["payment_status"]
    ))

conn.commit()
conn.close()

print("Raw delivery data loaded into SQLite.")
