from .get_files import files
from .xlsx_to_df import xlsx_to_df

def get_all_dataframes():
    dfs = []
    for file in files():
        dfs.append(xlsx_to_df(file,'AJUSTE_2022.3'))
    return dfs

