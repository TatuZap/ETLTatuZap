import requests # requisições http
import pandas as pd 
RESTAURANT_URL = "https://proap.ufabc.edu.br/nutricao-e-restaurantes-universitarios/cardapio-semanal"
RESTAURANT_PAGE = requests.get(RESTAURANT_URL).content
tables_on_page = pd.read_html(RESTAURANT_PAGE)

def clean_restaurant_df(df):
    pass 
