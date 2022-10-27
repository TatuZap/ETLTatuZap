import json
from raspador_fretados import tables_on_page, clean_bus_df
from fretados_model import FretadoModel
from database import get_db

fretados_model = FretadoModel()

# listando tudo
# for item in fretados_model.list_all():
#     print(item)

# preparando as tabelas para inseri-las elemento a elemento no banco
# fretados_json = [ json.loads(table.to_json(orient='records')) for table in clean_bus_df(tables_on_page) ]

# # inserao multipla
# for table_json in fretados_json:
#     fretados_model.insert_items(table_json)



# listando os que saem de SA e vão para SBC
for item in fretados_model.next_bus_sa_sbc(""):
    print(item)


#print(a==b)