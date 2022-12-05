from requests import get
import pandas as pd
from tabula import read_pdf
TURMAS_INGRESSANTES_URL = "https://prograd.ufabc.edu.br/pdf/turmas_ingressantes_2022_3.pdf"
TURMAS_INGRESSANTES = get(TURMAS_INGRESSANTES_URL).content

with open("turmas_ingressantes.pdf","wb") as turmas:
    turmas.write(TURMAS_INGRESSANTES)

df = read_pdf("turmas_ingressantes.pdf",stream=True,guess=False,pages='all', pandas_options={'header': None})


def clean_turmas_ingressantes_df(df):
    # renomear as colunas
    # retirar as linhas extras
    pass