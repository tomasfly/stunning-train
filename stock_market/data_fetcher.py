import yfinance as yf

def fetch_stock_prices(ticker, start_date, end_date):
    """
    Fetches historical stock prices for a given ticker between start_date and end_date.
    """
    data = yf.download(ticker, start=start_date, end=end_date)
    return data