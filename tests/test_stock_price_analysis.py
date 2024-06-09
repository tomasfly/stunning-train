import unittest
from unittest.mock import patch
import pandas as pd
from pandas.testing import assert_frame_equal
import stock_price_analysis

class TestStockPriceAnalysis(unittest.TestCase):
    @patch('stock_price_analysis.pd.read_csv')
    def test_stock_prices_loaded(self, mock_read_csv):
        # Mocking pd.read_csv to return a specific DataFrame
        mock_data = {
            "Open": [130.279999, 126.889999],  # Add all 62 rows with appropriate data
            "High": [130.899994, 128.660004],
            "Low": [124.169998, 125.080002],
            "Close": [125.070000, 126.360001],
            "Adj Close": [124.048042, 125.327515],
            "Volume": [112117500, 89113600]
        }
        expected_df = pd.DataFrame(mock_data)
        mock_read_csv.return_value = expected_df

        # Assuming stock_prices_loaded is a function that calls pd.read_csv
        actual_df = stock_price_analysis.stock_prices_loaded()

        pd.testing.assert_frame_equal(actual_df, expected_df)

if __name__ == '__main__':
    unittest.main()