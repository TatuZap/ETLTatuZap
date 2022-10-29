import json
from raspador_fretados import tables_on_page, clean_bus_df
from fretados_model import FretadoModel
from database import get_db

fretados_model = FretadoModel()

# listando tudo
# for item in fretados_model.list_all():
#     print(item)

# resetando o banco (deletando tudo e depois raspando e inserindo os dados)
fretados_model.populate_database()

# listando os que saem de SA e vão para SBC
for item in fretados_model.next_bus_sa_sbc(""):
    print(item)
