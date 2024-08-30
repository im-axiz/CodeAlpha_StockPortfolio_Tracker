# CodeAlpha_StockPortfolio_Tracker
Project Description The Stock Portfolio Tracker is a Python application that allows users to manage and track their stock investments. This tool provides functionality to add and remove stocks and to track the current value of the portfolio.
# Stock Portfolio Tracker

## Description
The Stock Portfolio Tracker is a Python-based application designed to help users manage their stock investments. With this tool, users can:

- **Add Stocks**: Include new stocks to their portfolio with a specified number of shares.
- **Remove Stocks**: Remove stocks or reduce the number of shares for existing stocks.
- **Track Portfolio**: View the current value of the portfolio based on real-time stock prices.

The application retrieves stock prices from the Alpha Vantage API, which provides intraday time series data for various stocks.

## Features
- **Add Shares**: Easily add shares of any stock to your portfolio.
- **Remove Shares**: Remove or reduce shares of a stock from your portfolio.
- **Track Portfolio Value**: Calculate and display the total value of your portfolio based on real-time prices.
- **Interactive Menu**: Simple command-line interface for user interactions.

## Installation
Open CMD and install requests as pip install requests and then run the .py file. 
## Update API Key: 
Replace the placeholder API key in the StockPortfolio class with your actual Alpha Vantage API key. You can obtain a free API key by signing up on the Alpha Vantage website.
## Interactive Menu:
Add Stock: [A / a / 1] – Enter the stock symbol and the number of shares.
Remove Stock: [R / r / 2] – Enter the stock symbol and the number of shares to remove.
Track Portfolio: [T / t / 3] – View the current value of your portfolio.
Quit: [Q / q / 4] – Exit the application.
## Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!
