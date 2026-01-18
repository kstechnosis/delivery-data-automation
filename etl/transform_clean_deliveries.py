import sqlite3
import pandas as pd

DB_PATH = "db/deliveries.db"

conn = sqlite3.connect(DB_PATH)

# Load raw data
raw_df = pd.read_sql_query("""
    SELECT *
    FROM raw_deliveries
    ORDER BY ingested_at DESC
""", conn)

# Deduplicate and EXPLICITLY copy
clean_df = raw_df.drop_duplicates(
    subset=["delivery_id"],
    keep="first"
).copy()

# Handle missing distance safely
clean_df.loc[:, "distance_km"] = clean_df["distance_km"].fillna(0)

# Revenue rule
clean_df.loc[
    clean_df["delivery_status"] != "Delivered",
    "amount_charged"
] = 0

# Select final columns
clean_df = clean_df[[
    "delivery_id",
    "order_id",
    "partner_name",
    "customer_city",
    "delivery_date",
    "delivery_time",
    "distance_km",
    "delivery_status",
    "amount_charged",
    "payment_status"
]]

# Load into clean_deliveries
clean_df.to_sql(
    "clean_deliveries",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Clean deliveries table refreshed.")
