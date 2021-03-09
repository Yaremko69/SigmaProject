import os
import time
from io import StringIO
import pandas as pd
import requests
from dotenv import load_dotenv

monthly_stock_dfs = {}
ALPHAVANTAGE_API_URL = 'https://www.alphavantage.co/query'
STOCK_DATA_PATH = 'stocks'
API_CALL_SLEEP_SEC = 60
session = requests.Session()
load_dotenv()
API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')

COMPANY_STOCKS = {
    'Alibaba': 'BABA',
    'Alphabet': 'GOOGL',
    'Amazon': 'AMZN',
    'Apple': 'AAPL',
    'Facebook': 'FB',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Oracle': 'ORCL',
    'Tesla': 'TSLA',
    'Twitter': 'TWTR'
}

CRYPTOCURRENCIES = {
    'LTC': 'LTC',
    'EOS': 'EOS',
    'ETH': 'ETH',
    'NEO': 'NEO',
    'LINK': 'LINK'
}


def get_stock_data(session, name, symbol, api_key, function, datatype):
    params = {
        'function': function,
        'symbol': symbol,
        'apikey': api_key,
        'datatype': datatype
    }
    print(f'Getting monthly stock data for {name}')

    response = session.get(ALPHAVANTAGE_API_URL, params=params)

    if '5 calls per minute and 500 calls per day' in response.text:
        print('5 calls per minute were exceeded. Waiting for 1 minute...')
        time.sleep(API_CALL_SLEEP_SEC)
        response = session.get(ALPHAVANTAGE_API_URL, params=params)

    if response.status_code == requests.codes.ok:
        df = pd.read_csv(StringIO(response.text), comment='#')
        df.to_csv(os.path.join(
            os.path.dirname(__file__),
            f'{STOCK_DATA_PATH}/{name}_monthly.csv'
        ))
        print(f'Data for {name} was downloaded...')
        return df
    else:
        raise Exception(response.status_code, response.reaspon)


def get_sector_performance(session, name, api_key, function, datatype):
    params = {
        'function': function,
        'apikey': api_key,
        'datatype': datatype
    }
    print(f'Getting monthly stock data for {name}')

    response = session.get(ALPHAVANTAGE_API_URL, params=params)

    if '5 calls per minute and 500 calls per day' in response.text:
        print('5 calls per minute were exceeded. Waiting for 1 minute...')
        time.sleep(API_CALL_SLEEP_SEC)
        response = session.get(ALPHAVANTAGE_API_URL, params=params)

    if response.status_code == requests.codes.ok:
        df = pd.read_json(StringIO(response.text))
        print(df.to_string)
        df.to_json(os.path.join(
            os.path.dirname(__file__),
            f'{STOCK_DATA_PATH}/{name}_monthly.json'
        ))
        print(f'Data for {name} was downloaded...')
        return df
    else:
        raise Exception(response.status_code, response.reaspon)


def get_stoks(STOCKS):
    if not API_KEY:
        raise Exception(
            f'Missing config file |.env| and ALPHAVENTAGE_APY_KEY is not set.'
        )
    for name, symbol in STOCKS.items():
        monthly_stock_dfs[name] = get_stock_data(
            session, name, symbol, API_KEY, 'TIME_SERIES_MONTHLY', 'csv'
        )
    print('Finished')


def get_sp():
    if not API_KEY:
        raise Exception(
            f'Missing config file |.env| and ALPHAVENTAGE_APY_KEY is not set.'
        )
    get_sector_performance(session, 'Sector_Performance', API_KEY, 'SECTOR', 'json')
    print('Finished')
