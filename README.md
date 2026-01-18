# Delivery Data Automation Pipeline

## Overview

This project demonstrates how a small logistics or service-based business can
automate daily data ingestion, cleaning, and reporting using a lightweight,
cost-efficient data pipeline.

The system is designed to eliminate manual Excel-based reporting and provide
near real-time, reliable business metrics whenever new data arrives.

---

## Business Problem

A small logistics company receives daily delivery data as CSV files from
multiple partners.

### Challenges

- Data files arrive daily with updates and corrections
- Manual cleanup and reporting takes 2–3 hours per day
- Duplicate records and missing values are common
- No centralized data store exists
- Historical files are overwritten and lost
- Management lacks real-time visibility into operations

---

## Solution Summary

A fully automated, file-driven data pipeline was implemented with the following goals:

- Automatically process updated data files
- Preserve historical files for audit and reprocessing
- Centralize data in a relational database
- Apply business rules consistently
- Generate reporting-ready daily metrics with zero manual effort

---

## Architecture

Updated CSV File
↓
File Archive (Timestamped Backup)
↓
Raw Data Storage
↓
Cleaned & Validated Data
↓
Daily Summary Metrics

---

## Key Features

### 1. Automated File-Based Trigger

- Data arrives daily using the same filename: `deliveries_latest.csv`
- When the file is updated:
  - The previous file is archived with a timestamp
  - The full data pipeline is executed automatically
  - Reports are refreshed with the latest data

### 2. Raw Data Preservation

- Incoming data is first stored as-is
- Enables auditability and safe reprocessing
- Prevents accidental data loss

### 3. Data Cleaning & Validation

- Duplicate deliveries are removed
- Missing values are handled consistently
- Business rules are applied centrally

### 4. Reporting-Ready Outputs

- Daily summary metrics are precomputed
- Reports require zero manual intervention
- Designed for dashboards or API consumption

---

## Business Rules Implemented

- Duplicate records are deduplicated using `delivery_id`
- Missing distance values are treated as zero
- Only successful deliveries contribute to revenue
- Failed and cancelled deliveries are retained for analysis
- Historical input files are archived automatically

---

## Tech Stack

- Python
- Pandas
- SQLite (demo and local testing)
- PostgreSQL (recommended for production)
- File-based automation (cron / event-ready design)

---

## Demo vs Production Notes

SQLite is used in this repository to ensure anyone can run the project locally
with minimal setup.

In production environments, the same schema and logic can be deployed on
PostgreSQL for improved scalability, concurrency, and data integrity.

---

## Project Structure

delivery-data-automation/
│
├── data/
│ ├── raw/
│ │ └── deliveries*latest.csv
│ └── archive/
│ └── deliveries*<timestamp>.csv
│
├── etl/
│ ├── load_raw_deliveries.py
│ ├── transform_clean_deliveries.py
│ ├── generate_daily_summary.py
│ └── run_pipeline.py
│
├── db/
│ ├── schema.sql
│ ├── init_db.py
│ └── deliveries.db
│
└── README.md

---

## How to Run the Pipeline (Step-by-Step)

### 1. Prerequisites

- Python 3.9 or higher
- No external database setup required

---

### 2. Clone the Repository

    git clone <repository-url>
    cd delivery-data-automation

### 3. Create a Virtual Environment (Optional)

    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate

### 4. Install Dependencies

    pip install pandas

### 5. Initialize the Database

    This creates the SQLite database and required tables.
    python db/init_db.py

    Expected output:
    SQLite database initialized.

### 6. Prepare Input Data

    Place the latest delivery data file at:
    data/raw/deliveries_latest.csv

The pipeline assumes this file is updated daily using the same filename.

### 7. Run the Full Pipeline

    python etl/run_pipeline.py

    This will:
    Archive the previous data file (if present)
    Load raw data into the database
    Clean and validate records
    Refresh daily summary metrics

    Expected output:

    Archived previous file as deliveries_<timestamp>.csv
    Raw delivery data loaded into SQLite.
    Clean deliveries table refreshed.
    Daily delivery summary generated.
    Pipeline executed successfully.

### 8. Verify Results

    Open SQLite:
    sqlite3 db/deliveries.db

    Run:
    SELECT * FROM daily_delivery_summary;

    You should see updated metrics reflecting the latest data.

### 9. Simulate New Data Arrival

    To simulate updated or new daily data:
    Replace deliveries_latest.csv with new data

    Run:
    python etl/run_pipeline.py

    The previous file will be archived automatically and reports will refresh.

### 10. Outcomes

 - Manual reporting effort reduced by ~80%
 - Centralized and reliable data storage
 - Automated, near real-time reporting
 - Audit-friendly historical data retention
 - Scalable design suitable for production systems

### 11. Future Improvements

 - Scheduling via cron or workflow orchestration
 - Dashboard integration (e.g., Superset)
 - Containerized deployment using Docker Compose
 - Cloud storage triggers (S3 / Blob / GCS)
