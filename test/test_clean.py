import unittest
from clean_data import DataCleaner, DataCleanerError
import pandas as pd



class TestFunctions(unittest.TestCase):

# DataFrame that resets for each test
    def setUp(self):
        self.df = pd.DataFrame({
            'text_col_valid': ['bob', 'info', 'text', 'string'],
            'text_col_split': ['bob|terry', 'info|facts', 'text|words', 'string|sentence'],
            'text_col_na': ['bob', 'info', 'text', None],
            'text_col_dtype': ['bob', 'info', 'text', 25],
            'value_er_col': ['20', '10', '30', 'forty'],
            'num_col_valid': [10, 20, 30, 40],
            'num_col_na': [10, 20, None, 40],
            'num_col_dtype': [10, 20, '30', 40]
        })
        self.cleaner = DataCleaner(self.df)


    def test_DataCleaner_init_invalid(self):
        with self.assertRaises(TypeError):
            self.cleaner = DataCleaner(2)

    def test_unneeded_valid(self):
        self.cleaner.drop_unneeded_cols(['text_col_valid'])


    def test_unneeded_Key_Missing(self):
        with self.assertRaises(DataCleanerError):
            self.cleaner.drop_unneeded_cols(['DNE'])


    def test_numeric_cleaning_Invalid(self):
        with self.assertRaises(DataCleanerError):
            self.cleaner.numeric_cleaning(['DNE'])


    def test_numeric_conv_Invalid(self):
        with self.assertRaises(DataCleanerError):
            self.cleaner.numeric_conv(['DNE'])

    def test_numeric_conv_dtype(self):
        with self.assertRaises(DataCleanerError):
            self.cleaner.numeric_conv(['num_col_dtype'])

    def test_discount_fix(self):
        with self.assertRaises(DataCleanerError):
            self.cleaner.discount_fix()

    def test_handle_duplicates(self):
        with self.assertRaises(DataCleanerError):
            self.cleaner.handle_duplicates()

    def test_clean_text_cols_Invalid(self):
        with self.assertRaises(DataCleanerError):
            self.cleaner.clean_text_cols(['DNE'])

    def test_clean_text_cols_dtype(self):
        with self.assertRaises(DataCleanerError):
            self.cleaner.clean_text_cols(['num_col_valid'],)

    def test_col_splitter_valid(self):
        result = self.cleaner.column_splitter(['text_col_split'], ['NEW1', 'NEW2'])
        self.assertIn(['NEW1', 'NEW2'], result)

    def test_col_splitter_Dup(self):
        with self.assertRaises(DataCleanerError):
            self.cleaner.column_splitter(['text_col_valid'], ['text_col_split'])

    def test_col_splitter_dtype(self):
        with self.assertRaises(DataCleanerError):
            self.cleaner.column_splitter(['num_col_valid'], ['NEW1', 'NEW2'])

    def test_handle_missing_valid(self):
        result = self.cleaner.handle_missing_values()
        self.assertFalse(result, self.df.isnull().values.any())

    def test_run_cleaning(self):
        with self.assertRaises(DataCleanerError):
            self.cleaner.run_cleaning()

if __name__ == '__main__':
    unittest.main()
