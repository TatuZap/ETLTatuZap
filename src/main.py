from transform.tratamento import tratamento_json,tratamento_df, to_json_file
from extract.extrator import get_all_dataframes

#Retorna todos os dados em json
#tratamento_json(get_all_dataframes)

#retorna todos os dados em dataframes
dfs = tratamento_df(get_all_dataframes)

#Cria arquivos json na pasta output
to_json_file(dfs)