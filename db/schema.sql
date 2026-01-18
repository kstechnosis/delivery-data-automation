CREATE TABLE IF NOT EXISTS raw_deliveries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    delivery_id TEXT,
    order_id TEXT,
    partner_name TEXT,
    customer_city TEXT,
    delivery_date TEXT,
    delivery_time TEXT,
    distance_km REAL,
    delivery_status TEXT,
    amount_charged REAL,
    payment_status TEXT,
    ingested_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS clean_deliveries (
    delivery_id TEXT PRIMARY KEY,
    order_id TEXT,
    partner_name TEXT,
    customer_city TEXT,
    delivery_date TEXT NOT NULL,
    delivery_time TEXT,
    distance_km REAL DEFAULT 0,
    delivery_status TEXT NOT NULL,
    amount_charged REAL DEFAULT 0,
    payment_status TEXT,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS daily_delivery_summary (
    delivery_date TEXT PRIMARY KEY,
    total_deliveries INTEGER,
    delivered_count INTEGER,
    failed_count INTEGER,
    cancelled_count INTEGER,
    total_distance_km REAL,
    total_revenue REAL,
    generated_at TEXT DEFAULT CURRENT_TIMESTAMP
);
