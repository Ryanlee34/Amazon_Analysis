from api import openexchange as ex
import os
from src.clean_data import DataCleaner
from src.create_db import PostgreSQLLoader

ex.configure()



# Define paths & database details
DB_URL = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
RAW_CSV_PATH = r"{}".format(os.getenv('RAW_CSV'))
CLEANED_CSV_PATH = r"{}".format(os.getenv('CLEAN_CSV'))
TABLE_NAME = "products"

# Step 1: Clean the Data
print("Cleaning Data...")
cleaner = DataCleaner(RAW_CSV_PATH)
cleaner.run_cleaning()
cleaner.save_data()
print("Data Cleaning Complete.")


# Step 2: Load Cleaned Data into PostgreSQL
print("Loading Data into PostgreSQL...")
loader = PostgreSQLLoader(DB_URL)
loader.load_csv_to_db(CLEANED_CSV_PATH, TABLE_NAME)
loader.close_connection()
print("Data Loaded Successfully.")

print("Execution Complete!")
