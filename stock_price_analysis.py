import numpy as np
import pandas as pd
from keras_model import prepare_data, build_and_train_model, evaluate_model

# Function to fetch stock prices (placeholder)
def fetch_stock_prices(ticker, start_date, end_date):
    # Placeholder: Implement the actual logic to fetch stock prices
    # For demonstration, return a DataFrame with random data
    dates = pd.date_range(start_date, end_date)
    prices = np.random.rand(len(dates), 4) * 100
    df = pd.DataFrame(prices, columns=['Open', 'High', 'Low', 'Close'], index=dates)
    return df

# Main execution starts here
ticker = 'AAPL'
start_date = '2023-01-01'
end_date = '2023-04-01'
stock_prices = fetch_stock_prices(ticker, start_date, end_date)

# Display the fetched stock prices DataFrame
print("Stock Prices DataFrame:")
print(stock_prices)

# Calculate the mean price using NumPy
mean_price = np.mean(stock_prices['Close'])  # Assuming 'Close' column exists
print(f"Mean Closing Price: {mean_price}")

# Save the DataFrame to a CSV file
stock_prices.to_csv('stock_prices.csv', index=True)

# Read the data back from the CSV file
stock_prices_loaded = pd.read_csv('stock_prices.csv', index_col=0)

# Display the loaded DataFrame
print("Loaded Stock Prices DataFrame:")
print(stock_prices_loaded)

# Prepare the data for the model
X_train, X_test, y_train, y_test = prepare_data(stock_prices)

# Build and train the model
model = build_and_train_model(X_train, y_train)

# Evaluate the model
evaluate_model(model, X_test, y_test)