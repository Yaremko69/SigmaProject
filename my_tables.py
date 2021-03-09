import dash_table
import pandas as pd


def generate_table(DATA_FRAMES, name):
    table_df = pd.DataFrame(columns=['date', 'name', 'open', 'low', 'high', 'close', 'valume'])
    index = 0
    for name, df in DATA_FRAMES.items():
        for df_column in df.head(15).values.tolist():
            table_df.loc[index] = [df_column[1], name, df_column[2], df_column[3], df_column[4], df_column[5],
                                   df_column[6]]
            index += 1

    return dash_table.DataTable(
        id=name,
        sort_action='native',
        filter_action="native",
        columns=[{"name": i, "id": i} for i in table_df.columns],
        data=table_df.to_dict('records'),
        style_table={'height': '500px', 'overflowY': 'auto'}
    )


def generate_sf(DATA_FRAMES):
    table_df = pd.DataFrame(
        columns=['Period', 'Information Technology', 'Consumer Discretionary', 'Communication Services', 'Health Care',
                 'Industrials', 'Materials', 'Consumer Staples', 'Real Estate', 'Utilities', 'Financials', 'Energy'])
    index = 0
    for x in DATA_FRAMES.columns[1:]:
        table_df.loc[index] = [x, *list(DATA_FRAMES[x])[2:]]
        index += 1

    return dash_table.DataTable(
        id='SF',
        sort_action='native',
        filter_action="native",
        columns=[{"name": i, "id": i} for i in table_df.columns],
        data=table_df.to_dict('records'),
    )
