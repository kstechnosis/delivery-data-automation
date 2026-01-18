import sqlite3
import pandas as pd

DB_PATH = "db/deliveries.db"

conn = sqlite3.connect(DB_PATH)

# Load clean data
df = pd.read_sql_query("""
    SELECT *
    FROM clean_deliveries
""", conn)

# Convert delivery_date to datetime
df["delivery_date"] = pd.to_datetime(df["delivery_date"])

# Group and aggregate
summary_df = df.groupby("delivery_date").agg(
    total_deliveries=("delivery_id", "count"),
    delivered_count=("delivery_status", lambda x: (x == "Delivered").sum()),
    failed_count=("delivery_status", lambda x: (x == "Failed").sum()),
    cancelled_count=("delivery_status", lambda x: (x == "Cancelled").sum()),
    total_distance_km=("distance_km", "sum"),
    total_revenue=("amount_charged", "sum")
).reset_index()

# Convert date back to string for SQLite
summary_df["delivery_date"] = summary_df["delivery_date"].dt.strftime("%Y-%m-%d")

# Load into summary table
summary_df.to_sql(
    "daily_delivery_summary",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Daily delivery summary generated.")
