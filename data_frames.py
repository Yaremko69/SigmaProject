import pandas as pd


def get_stoks_companies():
    try:
        DATA_FRAMES = {
            'Alibaba': pd.read_csv('alpha_vantage/data/stocks/Alibaba_monthly.csv'),
            'Alphabet': pd.read_csv('alpha_vantage/data/stocks/Alphabet_monthly.csv'),
            'Amazon': pd.read_csv('alpha_vantage/data/stocks/Amazon_monthly.csv'),
            'Apple': pd.read_csv('alpha_vantage/data/stocks/Apple_monthly.csv'),
            'Facebook': pd.read_csv('alpha_vantage/data/stocks/Facebook_monthly.csv'),
            'Microsoft': pd.read_csv('alpha_vantage/data/stocks/Microsoft_monthly.csv'),
            'Netflix': pd.read_csv('alpha_vantage/data/stocks/Netflix_monthly.csv'),
            'Oracle': pd.read_csv('alpha_vantage/data/stocks/Oracle_monthly.csv'),
            'Tesla': pd.read_csv('alpha_vantage/data/stocks/Tesla_monthly.csv'),
            'Twitter': pd.read_csv('alpha_vantage/data/stocks/Twitter_monthly.csv')
        }
    except FileNotFoundError:
        return False
    return DATA_FRAMES


def get_stoks_cripto():
    try:
        DATA_FRAMES = {
            'LTC': pd.read_csv('alpha_vantage/data/stocks/LTC_monthly.csv'),
            'EOS': pd.read_csv('alpha_vantage/data/stocks/EOS_monthly.csv'),
            'ETH': pd.read_csv('alpha_vantage/data/stocks/ETH_monthly.csv'),
            'NEO': pd.read_csv('alpha_vantage/data/stocks/NEO_monthly.csv'),
            'LINK': pd.read_csv('alpha_vantage/data/stocks/LINK_monthly.csv')
        }
    except FileNotFoundError:
        return False
    return DATA_FRAMES

def get_sp():
    try:
        df = pd.DataFrame(pd.read_json('alpha_vantage/data/stocks/Sector_Performance_monthly.json'))
        df = df.rename(columns={
            'Rank A: Real-Time Performance': 'Real-Time',
            'Rank B: 1 Day Performance': '1 Day',
            'Rank C: 5 Day Performance': '5 Day',
            'Rank D: 1 Month Performance': '1 Month',
            'Rank E: 3 Month Performance': '3 Month',
            'Rank F: Year-to-Date (YTD) Performance': 'Year-to-Date',
            'Rank G: 1 Year Performance': '1 Year',
            'Rank H: 3 Year Performance': '3 Year',
            'Rank I: 5 Year Performance': '5 Year',
            'Rank J: 10 Year Performance': '10 Year'
        })
        df = df.fillna(0)

    except FileNotFoundError:
        return False
    DATA_FRAMES = {'SF': df}
    return DATA_FRAMES
