
import json
import requests
import pandas as pd
import unidecode
BUS_URL = "https://pu.ufabc.edu.br/horarios-dos-onibus"
BUS_PAGE = requests.get(BUS_URL).content
tables_on_page = pd.read_html(BUS_PAGE)
BUS_NAMES = ["SA-SBC-SS","SBC-TSBC","SA-SBC-FDS"]

def clean_bus_df(df):
    normalise_df_columns_names = lambda df : (df.set_axis([ unidecode.unidecode(column.lower()) for column in list(df.columns)], axis=1))
    clean_df = []
    for table in df:
        current_table = normalise_df_columns_names(table)
        clean_df.append(current_table)
        for column in current_table.columns:
            current_table.loc[(current_table[column] == "---"),column] = "N"
    return clean_df