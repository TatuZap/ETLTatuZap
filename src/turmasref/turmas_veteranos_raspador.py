from requests import get
import pandas as pd
TURMAS_SALAS_HORARIOS_URL = "https://prograd.ufabc.edu.br/pdf/ajuste_2022_3_turmas.xlsx"
TURMAS_SALAS_HORARIOS = get(TURMAS_SALAS_HORARIOS_URL).content

with open("TURMAS_SALAS.xlsx","wb") as turmas:
    turmas.write(TURMAS_SALAS_HORARIOS)

df = pd.read_excel(TURMAS_SALAS_HORARIOS,sheet_name="AJUSTE_2022.3")

def clean_turmas_salas_horarios_df(df):
    # Realocando as colunas do Dataframe
    
    df.columns = df.iloc[0]
    df.drop(index=df.index[0], axis=0, inplace=True)
    
    # Limpeza dos elementos que são nulos
    
    for column in df.columns:
        df[column] = df[column].fillna(0)  
    return df