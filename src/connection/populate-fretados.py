import json
from raspador_fretados import tables_on_page, clean_bus_df
from fretados_model import FretadoModel
from database import get_db

fretados_model = FretadoModel()

# # listando tudo
# print(fretados_model.listAll())

# # preparando as tabelas para inseri-las elemento a elemento no banco
# fretados_json = [ json.loads(table.to_json(orient='records')) for table in clean_bus_df(tables_on_page) ]

# # inserao multipla
# for table_json in fretados_json:
#     fretados_model.insertItems(table_json)

for item in fretados_model.listAll():
    print(item)