import os
from api.openexchange import configure, OpenExchangeClient
import pandas as pd

configure()
ex = OpenExchangeClient(os.getenv('api_key'))

class DataCleanerError(Exception):
    pass


class DataCleaner:

    def __init__(self, filepath):
        if isinstance(filepath, str) and filepath.endswith('.csv'):
            if os.path.exists(filepath):
                self.df = pd.read_csv(filepath)
            else:
                raise FileNotFoundError(f"Invalid File path:{filepath}")
        elif isinstance(filepath, pd.DataFrame):
            self.df = filepath
        else:
            raise TypeError("Filepath must be a string or a DataFrame")

    def drop_unneeded_cols(self, cols: list[str]):
        try:
            self.df.drop(cols, axis=1, inplace=True)
            return f"Columns dropped: {cols}"

        except (ValueError, TypeError) as e:
            raise DataCleanerError(f"Error Occurred: {e}")
        except KeyError as e:
            raise DataCleanerError(f"Columns not found: {e}")

    def numeric_cleaning(self, cols: list[str]):
        try:
            for col in cols:
                self.df[col] = self.df[col].replace({r'[^0-9.]': '', r'\.(?=.*\.)': ''}, regex=True)
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')

        except (ValueError, TypeError) as e:
            raise DataCleanerError(f"Error Occurred: {e}")
        except KeyError as e:
            raise DataCleanerError(f"Columns not found: {e}")


    def numeric_conv(self, cols: list[str]):
        try:
            for col in cols:
                self.df[col] = ex.convert(self.df[col], 'INR')

        except (ValueError, TypeError) as e:
            raise DataCleanerError(f"Error Occurred: {e}")
        except KeyError as e:
            raise DataCleanerError(f"Columns not found: {e}")


    def discount_fix(self):
        try:
            self.df['discounted_price'] = (self.df['actual_price'] * (1 - (self.df['discount_percentage'] / 100))).round(2)

        except (ValueError, ValueError) as e:
            raise DataCleanerError("ValueError: check column values")
        except KeyError as e:
            raise DataCleanerError(f"Columns not found: {e}")

    def handle_duplicates(self):
        try:
            self.df = self.df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
            self.df = self.df[~self.df.duplicated(keep='first')]
            self.df = self.df.groupby('product_id').agg({
                'product_name': 'first',
                'main_category': 'first',
                'sub_category': 'first',
                'actual_price': 'mean',
                'discounted_price': 'mean',
                'discount_percentage': 'mean',
                'rating': 'mean',
                'rating_count': 'mean',
            }).reset_index()
        except (ValueError, TypeError) as e:
            raise DataCleanerError(f"Error Occurred: {e}")
        except KeyError as e:
            raise DataCleanerError(f"Columns not found: {e}")

    def clean_text_cols(self, cols: list[str]):
        try:
            for col in cols:
                self.df[col] = self.df[col].str.strip().str.lower()

        except (ValueError, TypeError, AttributeError) as e:
            raise DataCleanerError(f"Error Occurred: {e}")
        except KeyError as e:
            raise DataCleanerError(f"Columns not found: {e}")

    def column_splitter(self,column_to_split, cols: list[str]):
        try:
            self.df[cols] = self.df[column_to_split].str.split('|', expand=True, n=2).iloc[:,:2]
            self.df.drop(columns=[column_to_split], inplace=True)

        except (ValueError, TypeError, AttributeError) as e:
            raise DataCleanerError(f"Error Occurred: {e}")
        except KeyError as e:
            raise DataCleanerError(f"Columns not found: {e}")

    def handle_missing_values(self):
        self.df = self.df.dropna()


    def run_cleaning(self):
        try:
            self.drop_unneeded_cols(['about_product','user_id','user_name','review_id','review_content','review_title','img_link','product_link'])
            self.numeric_cleaning(['actual_price','discount_percentage','discounted_price','rating','rating_count'])
            self.numeric_conv(['actual_price','discounted_price'])
            self.discount_fix()
            self.clean_text_cols(['product_name', 'category'])
            self.column_splitter('category', ['main_category', 'sub_category'])
            self.df['actual_price'] = self.df['actual_price'].round(2)
            self.handle_duplicates()
        except Exception as e:
            raise DataCleanerError(f"Error Occurred: {e}")

    def save_data(self):
        try:
            self.df.to_csv(r"{}".format(os.getenv('CLEAN_CSV')), index=False)
        except FileNotFoundError:
            return print("Invalid File path or file Does not exist")

    def __repr__(self):
        return f"<DataCleaner with {self.df.shape[0]} rows and {self.df.shape[1]} columns>"
