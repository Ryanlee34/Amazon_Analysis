import pandas as pd
import psycopg2
from sqlalchemy import create_engine

class PostgreSQLLoader:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.conn = self.engine.connect()

    def load_csv_to_db(self, csv_path, table_name):
        df = pd.read_csv(csv_path)
        df.to_sql(table_name, con=self.engine, if_exists='replace', index=False)
        print(f"Data inserted into '{table_name}' successfully.")

    def close_connection(self):
        self.conn.close()


