from bs4 import BeautifulSoup
from bs4 import NavigableString
import pandas as pd
import requests


url = 'https://iextrading.com/trading/eligible-symbols/'

def scrape():
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
    soup = BeautifulSoup(page.content, 'html5lib')

    names = soup.find('div', id='app')

    print(names)
    file = pd.read_html(names)
    print(file)

    # for name in names:
    #     symbol_dict[names.]

def main():
    scrape()


if __name__ == '__main__':
    main()


