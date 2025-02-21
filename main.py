from scripts.clean_data import DataCleaner
from scripts.create_db import PostgreSQLLoader

# Define paths & database details
DB_URL = 'postgresql+psycopg2://postgres:project1@localhost:5432/amazon_analysis'
RAW_CSV_PATH = r"C:\Users\ryanl\OneDrive\Desktop\Resume Projects\Amazon Product & Review Analysis\data\raw\amazon.csv"
CLEANED_CSV_PATH = r"C:\Users\ryanl\OneDrive\Desktop\Resume Projects\Amazon Product & Review Analysis\data\cleaned\final_cleaned_data.csv"
TABLE_NAME = "products"

# Step 1: Clean the Data
print("🔹 Cleaning Data...")
cleaner = DataCleaner(RAW_CSV_PATH)
cleaner.run_cleaning()
cleaner.save_data(CLEANED_CSV_PATH)
print("Data Cleaning Complete.")

# Step 2: Load Cleaned Data into PostgreSQL
print("🔹 Loading Data into PostgreSQL...")
loader = PostgreSQLLoader(DB_URL)
loader.load_csv_to_db(CLEANED_CSV_PATH, TABLE_NAME)
loader.close_connection()
print("Data Loaded Successfully.")

print("Execution Complete!")