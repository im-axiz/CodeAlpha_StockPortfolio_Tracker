#Aziz Ahmad
#CodeAlpha Task 2
#Stock Portfolio Tracker

import requests
import time
import sys

class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = {}

    def add(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol} to your portfolio.")

    def remove(self, symbol, shares):
        if symbol in self.portfolio:
            if shares >= self.portfolio[symbol]:
                del self.portfolio[symbol]
                print(f"Removed all shares of {symbol} from your portfolio.")
            else:
                self.portfolio[symbol] -= shares
                print(f"Removed {shares} shares of {symbol} from your portfolio.")
        else:
            print(f"{symbol} is not in your portfolio.")

    def getPrice(self, symbol):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        try:
            last_refreshed = data['Meta Data']['3. Last Refreshed']
            price = data['Time Series (1min)'][last_refreshed]['4. close']
            return float(price)
        except KeyError:
            print(f"Error fetching data for {symbol}. Please check the symbol and try again.")
            return None

    def track(self):
        total_value = 0
        print("\n:::::::YOUR PORTFOLIO:\n")
        for symbol, shares in self.portfolio.items():
            price = self.getPrice(symbol)
            if price:
                stock_value = price * shares
                total_value += stock_value
                print(f"{symbol}: {shares} shares at ${price:.2f} each, Total: ${stock_value:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}")

if __name__ == "__main__":
    print("__________STOCK PORTFOLIO TRACKER__________\n")
    api_key = "your_actual_alpha_vantage_api_key"  # Replace with your actual API key
    p = StockPortfolio(api_key)
    print(":::::::MENU\n[A / a / 1 to Add Stock]\n[R / r / 2 to Remove Stock]\n[T / t / 3 to Track Portfolio]\n[Q / q / 4 to Quit]")
    while True:
        ask = input("Choose an action: ")

        if ask in ['A', 'a', '1']:
            symbol = input("Enter the stock symbol to add: ").upper()
            shares = int(input(f"Enter the number of shares to add for {symbol}: "))
            p.add(symbol, shares)
        elif ask in ['R', 'r', '2']:
            symbol = input("Enter the stock symbol to remove: ").upper()
            shares = int(input(f"Enter the number of shares to remove for {symbol}: "))
            p.remove(symbol, shares)
        elif ask in ['T', 't', '3']:
            p.track()
        elif ask in ['Q', 'q', '4']:
            print("Exiting", end="")
            for _ in range(3):
                sys.stdout.write('.')
                sys.stdout.flush()
                time.sleep(0.5)
            print("\nThank you for using my program!")
            time.sleep(1)
            break
        else:
            print("Invalid input, please try again.")
