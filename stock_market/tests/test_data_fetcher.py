import unittest
from stock_market.data_fetcher import fetch_stock_prices

class TestDataFetcher(unittest.TestCase):
    def test_fetch_stock_prices(self):
        # Example test case
        # You should mock fetch_stock_prices responses
        self.assertIsNotNone(fetch_stock_prices("AAPL", "2023-01-01", "2023-04-01"))

if __name__ == '__main__':
    unittest.main()