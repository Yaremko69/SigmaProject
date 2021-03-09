import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import alpha_vantage.data.get_alphavantage_data as get_ad
import data_frames
from my_tables import generate_table, generate_sf

DATA_FRAMES_COMPANIES = pd.DataFrame()
DATA_FRAMES_CRIPTO = pd.DataFrame()
DATA_FRAME_SP = pd.DataFrame()

if (data_frames.get_stoks_companies() == False):
    get_ad.get_stoks(get_ad.COMPANY_STOCKS)
else:
    DATA_FRAMES_COMPANIES = data_frames.get_stoks_companies()

if (data_frames.get_stoks_cripto() == False):
    get_ad.get_stoks(get_ad.CRYPTOCURRENCIES)
else:
    DATA_FRAMES_CRIPTO = data_frames.get_stoks_cripto()

if (data_frames.get_stoks_cripto() == False):
    get_ad.get_ad.get_sp()
else:
    DATA_FRAME_SP = data_frames.get_sp().get('SF')


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1(
        children='Dash Project',
        style={
            'textAlign': 'center'
        }
    ),
    dcc.Tabs([
        dcc.Tab(label="Stocks", children=[
            dcc.Graph(
                figure={
                    "data": [
                        {
                            "x": df["timestamp"].head(15),
                            "y": df["volume"].head(15),
                            "type": "lines",
                            'name': name
                        } for name, df in DATA_FRAMES_COMPANIES.items()

                    ],
                },
            ),
            generate_table(DATA_FRAMES_COMPANIES, 'Companies')

        ]),
        dcc.Tab(label="Cryptocurrency", children=[
            dcc.Graph(
                figure={
                    "data": [
                        {
                            "x": df["timestamp"].head(15),
                            "y": df["volume"].head(15),
                            "type": "lines",
                            'name': name
                        } for name, df in DATA_FRAMES_CRIPTO.items()

                    ],
                },
            ),
            generate_table(DATA_FRAMES_CRIPTO, 'Cripto')
        ]),
        dcc.Tab(label="Sector Performance", children=[
            dcc.Graph(
                figure={
                    "data": [{
                        "x": DATA_FRAME_SP.columns[1:],
                        "y": DATA_FRAME_SP.loc[x][1:],
                        'name': x,
                        "type": "bar",
                    } for x in DATA_FRAME_SP.index[2:]
                    ],
                },
            ),
            generate_sf(DATA_FRAME_SP)
        ])]),

])

if __name__ == '__main__':
    app.run_server(debug=True)
