from transform.tratamento import tratamento_json,tratamento_df
from extract.extrator import get_all_dataframes

#Retorna todos os dados em json
tratamento_json(get_all_dataframes)

#retorna todos os dados em dataframes
tratamento_df(get_all_dataframes)
