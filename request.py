from iexfinance.stocks import Stock
import json
import csv

token = open('secrets').read()

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


def main():
    # with open('tickers.json', 'r') as file:
    #     tickers = json.load(file)
    # symbols = []
    # for values in tickers:
    #     symbols.append(values['symbol'])
    #
    # with open('symbols.csv', 'w', newline='') as csvfile:
    #     writer = csv.writer(csvfile, delimiter=' ')
    #     writer.writerow(symbols)

    # print(requester.tickers)
    pass


if __name__ == '__main__':
    main()
