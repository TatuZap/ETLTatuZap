from fretados_model import FretadoModel

# instanciando o model do Fretado
fretados_model = FretadoModel()

# resetando o banco (deletando tudo e depois raspando e inserindo os dados)
fretados_model.populate_database()

# #### listando tudo que foi recuperado do banco ####
# for item in fretados_model.list_all():
#     print(item)

# #### listando os que saem de SA e vão para SBC ####
# for item in fretados_model.next_bus("SA", "SBC", ""):
#     print(item)

# #### listando os que saem de SBC e vão para SA ####
# for item in fretados_model.next_bus("SA", "SBC", ""):
#     print(item)

#### listando os que saem de SBC e vão para SBC ####
# for item in fretados_model.next_bus("SBC", "SBC", ""):
#     print(item)

# #### listando o primeiro fretado que achar que é da linha 2 ####
# print(fretados_model.find_by_linha(2))
