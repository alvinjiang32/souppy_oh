from iexfinance.refdata import get_symbols
import json

token = 'pk_222272c1554c4b7083c64705db326a65'
static_tickers = '' # csv or json

class requester:
    stocks = []

    # pass in a stock object to retrieve data
    def get_stock_data(self, stock):
        data = stock.get_quote()
        ticker = data['symbol']
        name = data['companyName']
        open_price = float(data['open'])
        closing_price = float(data['close'])
        day_high = float(data['high'])
        day_low = float(data['low'])
        date_updated = data['latestTime']
        day_change = float(data['change'])
        percent_change = float(data['change']) * 100

@staticmethod
def get_default_stock_data(self):
    for stock in static_tickers:
        print(requester.get_stock_data(stock))

