from iexfinance.refdata import get_symbols
from iexfinance.stocks import Stock
import json

token = 'pk_222272c1554c4b7083c64705db326a65'
static_tickers = '' # csv or json

class requester:

    stocks = []

    # pass in a ticker symbol to retrieve data
    @staticmethod
    def get_stock_data(ticker):
        stock = Stock(ticker, token=token)
        data = stock.get_quote()
        ticker = data['symbol']
        name = data['companyName']
        open_price = data['open']
        closing_price = data['close']
        day_high = data['high']
        day_low = data['low']
        date_updated = data['latestTime']
        day_change = data['change']
        percent_change = str(data['changePercent'] * 100) + '%'
        return {'ticker': ticker, 'name': name, 'open_price': open_price,
                'closing_price': closing_price, 'day_high': day_high,
                'day_low': day_low, 'date_updated': date_updated,
                'day_change': day_change, 'percent_change': percent_change}

    @staticmethod
    def get_stock_data_str(ticker):
        data = requester.get_stock_data(ticker)
        str_data = ''
        for key in data:
            str_data = str_data + key + ': ' + str(data[key]) + '\n'
        return str_data

    @staticmethod
    def get_default_stock_data(self):
        for stock in static_tickers:
            print(self.get_stock_data(Stock(stock)))

def main():
    done = False
    while not done:
        ticker = input('\nWhat stock would you like to look at?\nEnter x to '
                       'quit.\n')
        if ticker.lower() == 'x':
            break;
        values = requester.get_stock_data(ticker)
        print('Info for', ticker)
        for key in values:
            if values[key] is not None:
                print(key + ': ' + str(values[key]))
            else:
                print(key + ' does not have value')


if __name__ == '__main__':
    main()
