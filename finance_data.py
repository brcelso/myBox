"""
Use Alpha Vantage API to get stock data and plot it in graph.
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt


API_KEY = "TXQ8APATHEM6J9WF"
STOCK_SYMBOL = "TSLA"
def get_daily_stock_data(symbol: str):


    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


def main():
    data = get_daily_stock_data(STOCK_SYMBOL)

    # Turn the data into a pandas DataFrame
    df = pd.DataFrame(data["Time Series (Daily)"]).T
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)

    # Print the dataframe
    print(df)

    # Plot the data in a graph.
    plt.plot(df["4. close"])
    plt.show()

    pass

if __name__ == "__main__":
    main()






