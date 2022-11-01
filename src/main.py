from transform.tratamento import tratamento_json,tratamento_df, to_json_file
from extract.extrator import get_all_dataframes
from extract.get_files import files

#Retorna todos os dados em json
#tratamento_json(get_all_dataframes)

#retorna todos os dados em dataframes
dfs = tratamento_df(get_all_dataframes)
for i in dfs:
    print(i["file_name"])
#Cria arquivos json na pasta output
#to_json_file(dfs)

