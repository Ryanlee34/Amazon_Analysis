import numpy as np
import pandas as pd

class DataCleaner:

    def __init__(self, filepath):
        self.df = pd.read_csv(filepath)

    def drop_unneeded_cols(self, cols: list[str]):
        self.df.drop(cols, axis=1, inplace=True)

    def numeric_cleaning(self, cols: list[str]):
        for col in cols:
            self.df[col] = self.df[col].replace({',':'','%':'','₹':'',r'\|': np.nan}, regex=True).astype(float).round(2)

    def numeric_conv(self, cols: list[str]):
        for col in cols:
            self.df[col] = (self.df[col] * 0.012).round(2)

    def discount_fix(self):
        self.df['discounted_price'] = (self.df['actual_price'] * (1 - (self.df['discount_percentage'] / 100))).round(2)

    def handle_duplicates(self):
        self.df = self.df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        self.df = self.df[~self.df.duplicated(keep='first')]

        self.df = self.df.groupby('product_id').agg({
            'product_name': 'first',
            'main_category': 'first',
            'sub-category': 'first',
            'actual_price': 'mean',
            'discounted_price': 'mean',
            'discount_percentage': 'mean',
            'rating': 'mean',
            'rating_count': 'mean',
        }).reset_index()

    def clean_text_cols(self, cols: list[str]):
        for col in cols:
            self.df[col] = self.df[col].str.strip().str.lower()

    def column_splitter(self, column):
        names = input('Enter Desired column names in order (2): ').strip().split(' ')
        self.df[[names[0], names[1]]] = self.df[column].str.split('|', expand=True, n=2).iloc[:, :2]
        self.df.drop(columns=[column], inplace=True)

    def handle_missing_values(self):
        pass  # Placeholder to prevent errors, define logic if needed

    def find_similar_names(self):
        duplicates = [(product, other_product)
                      for i, product in enumerate(self.df['product_name'])
                      for j, other_product in enumerate(self.df['product_name'])
                      if i != j and (product in other_product or other_product in product)]
        return duplicates

    def run_cleaning(self):
        self.drop_unneeded_cols([])
        self.numeric_cleaning([])
        self.numeric_conv([])
        self.discount_fix()
        self.handle_duplicates()
        self.clean_text_cols([])
        self.column_splitter('')
        self.find_similar_names()

    def save_data(self):
        self.df.to_csv(r"C:\Users\ryanl\OneDrive\Desktop\Resume Projects\Amazon Product & Review Analysis\data\cleaned\final_cleaned_data.csv", index=False)

    def __repr__(self):
        return f"DataCleaner with {self.df.shape[0]} rows and {self.df.shape[1]} columns"
