import pandas as pd
import matplotlib.pyplot as plt

# Load the stock prices data
stock_prices = pd.read_csv('stock_prices.csv')

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(stock_prices['Close'], label='Close Price')
plt.title('Stock Close Prices Over Time')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()