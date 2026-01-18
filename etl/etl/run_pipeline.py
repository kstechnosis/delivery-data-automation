import os
import shutil
from datetime import datetime
import subprocess

RAW_FILE = "data/raw/deliveries_latest.csv"
ARCHIVE_DIR = "data/archive"

def archive_existing_file():
    if not os.path.exists(RAW_FILE):
        return

    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
    archive_name = f"deliveries_{timestamp}.csv"
    archive_path = os.path.join(ARCHIVE_DIR, archive_name)

    shutil.copy(RAW_FILE, archive_path)
    print(f"Archived previous file as {archive_name}")

def run_etl():
    subprocess.run(["python", "etl/load_raw_deliveries.py"], check=True)
    subprocess.run(["python", "etl/transform_clean_deliveries.py"], check=True)
    subprocess.run(["python", "etl/generate_daily_summary.py"], check=True)

def main():
    archive_existing_file()
    run_etl()
    print("Pipeline executed successfully.")

if __name__ == "__main__":
    main()
