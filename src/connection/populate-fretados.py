from fretados_model import FretadoModel

# instanciando o model do Fretado
fretados_model = FretadoModel()

# resetando o banco (deletando tudo e depois raspando e inserindo os dados)
fretados_model.populate_database()

# listando tudo que foi recuperado do banco
for item in fretados_model.list_all():
    print(item)

# listando os que saem de SA e vão para SBC
# for item in fretados_model.next_bus_sa_sbc(""):
#     print(item)
