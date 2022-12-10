import src.turmasref.turmas_ingressantes_raspador as turmas_ingressantes_raspador
import src.turmasref.turmas_veteranos_raspador as turmas_veteranos_raspador
import src.turmasref.turmas_pos_reajuste as turmas_pos_ajuste
import src.turmasref.turmas_pos_ajuste_raspador as turmas_pos_reajuste_raspador
from ..database import get_db, DBCollections
from copy import deepcopy


def insert_items_AJUSTE(items):
    """
        Função que insere um documentos relacionados a turmas na coleção de turmas
    """
    try:
        response = _get_collection_AJUSTE().insert_many(items)
        if response:
            return response
        raise Exception("Erro ao inserir Fretados")
    except Exception as e:
        raise e

def insert_items_REAJUSTE(items):
    """
        Função que insere um documentos relacionados a turmas na coleção de turmas
    """
    try:
        response = _get_collection_REAJUSTE().insert_many(items)
        if response:
            return response
        raise Exception("Erro ao inserir Fretados")
    except Exception as e:
        raise e

def insert_items_INGRESSANTES(items):
    """
        Função que insere um documentos relacionados a turmas na coleção de turmas
    """
    try:
        response = _get_collection_INGRESSANTES().insert_many(items)
        if response:
            return response
        raise Exception("Erro ao inserir Fretados")
    except Exception as e:
        raise e

def insert_items_SALAS_HORARIOS(items):
    """
        Função que insere um documentos relacionados a turmas na coleção de turmas
    """
    try:
        response = _get_collection_SALAS_HORARIOS().insert_many(items)
        if response:
            return response
        raise Exception("Erro ao inserir Fretados")
    except Exception as e:
        raise e

def delete_all():
    """
        Função que remove todas os documentos relacionados com turmas
    """
    try:
        _get_collection_AJUSTE().delete_many({})
        _get_collection_REAJUSTE().delete_many({})
        _get_collection_INGRESSANTES().delete_many({})
        _get_collection_SALAS_HORARIOS().delete_many({})
    except Exception as e:
        raise e

def populate_database():
    # deleta o conteúdo atual do banco
    delete_all()

    # get dataframe
    parsed_dataframe = turmas_veteranos_raspador.clean_turmas_salas_horarios_df(turmas_veteranos_raspador.df)
    fretados_dicts = parsed_dataframe.to_dict('records')
    insert_items_SALAS_HORARIOS(fretados_dicts)

    # parsed_dataframe = turmas_ingressantes_raspador.clean_turmas_ingressantes_df(turmas_ingressantes_raspador.df)
    # fretados_dicts = parsed_dataframe.to_dict('records')
    # insert_items_INGRESSANTES(fretados_dicts)

    # parsed_dataframe = turmas_pos_ajuste.clean_turmas_pos_ajuste_df(turmas_pos_ajuste.df)
    # fretados_dicts = parsed_dataframe.to_dict('records')
    # insert_items_AJUSTE(fretados_dicts)

    # parsed_dataframe = turmas_pos_reajuste_raspador.clean_turmas_pos_ajuste_df(turmas_pos_reajuste_raspador.df)
    # fretados_dicts = parsed_dataframe.to_dict('records')
    # insert_items_REAJUSTE(fretados_dicts)

# função privada dentro desse módulo
def _get_collection_SALAS_HORARIOS():
    try:
        return get_db.get_collection(DBCollections.TURMAS_SALAS_HORARIOS)
    except Exception as e:
        raise e
# função privada dentro desse módulo
def _get_collection_AJUSTE():
    try:
        return get_db.get_collection(DBCollections.TURMAS_AJUSTE)
    except Exception as e:
        raise e
# função privada dentro desse módulo
def _get_collection_REAJUSTE():
    try:
        return get_db.get_collection(DBCollections.TURMAS_REAJUSTE)
    except Exception as e:
        raise e

def _get_collection_INGRESSANTES():
    try:
        return get_db.get_collection(DBCollections.TURMAS_INGRESSANTES)
    except Exception as e:
        raise e

# class Fretado:
#     """
#     Classe que Modela o Objeto de negócio Fretado
#     - linha:                      O número da linha de onibus, pode ter valores de 1 a 6
#     - dias:                       Pode ser de dois valores 'SEMANA' e 'SABADO'
#     - origem:                     Pode ser de dois valores 'SA' e 'SBC'
#     - hora_partida:               Pode ser do valor de um horário, tipo '8:25' ou 'N/A' caso não tenha valor
#     - destino:                    Pode ser de dois valores 'SA' e 'SBC'
#     - hora_chegada:               Pode ser do valor de um horário, tipo '8:25' ou 'N/A' caso não tenha valor
#     - desembarque_terminal_leste: Caso tenha desembarque no Terminal Leste é o valor de um horário, tipo '8:25', caso contrário, 'N/A'
#     """
#     def __init__(self, linha, dias, origem, hora_partida, destino, hora_chegada, desembarque_terminal_leste) -> None:
#         self.dias = dias
#         self.origem = origem
#         self.destino = destino
#         self.hora_partida = hora_partida
#         self.hora_chegada = hora_chegada
#         self.linha = linha
#         self.desembarque_terminal_leste = desembarque_terminal_leste

#     def __str__(self) -> str:
#         return "Fretado da Linha: {} que parte de {} as {} e chega em {} as {}, operando durante (o/a) {}".format(self.linha,self.origem,self.destino,self.hora_partida,self.hora_chegada,self.dias)

#     def to_dict(self) -> dict:
#         return self.__dict__

#     def from_dict(dictionary):
#         del dictionary['_id']

#         return Fretado(**dictionary)
