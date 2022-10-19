import pandas as pd

def extrator(file,sheetname):
    df = pd.read_excel(file,sheet_name=sheetname)
    return df