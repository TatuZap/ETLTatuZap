import json
import raspador_restaurante
import pandas as pd 
from database import get_db, DBCollections
from raspador_restaurante import tables_on_page, clean_restaurant_df

def list_all():
    """
        Função que retorna todos os Restaurante da coleção de Restaurante
    """
    try:
        response = _get_collection().find()
        if response.explain()["executionStats"]["executionSuccess"]: # Procura nos Status se a operação deu Certo
            return response
    except Exception as e:
        raise e 

def insert_item(item):
    """
        Função que insere um Fretado na Coleção de Restaurante
    """
    try:
        response = _get_collection().insert_one(item)
        if response:
            return response
    except Exception as e:
        raise e

def insert_items(items):
    """
        Função que insere uma lista de Restaurante na Coleção de Restaurante
    """
    try:
        response = _get_collection().insert_many(items)
        if response:
            return response
        raise Exception("Erro ao inserir Restaurante")
    except Exception as e:
        raise e

def delete_all():
    """
        Função que remove todas as entradas da coleção de Restaurante
    """
    try:
        response = _get_collection().delete_many({})
        if response:
            return response
    except Exception as e:
        raise e

def populate_database():
    # deleta o conteúdo atual do banco
    delete_all()

    # get dataframe
    parsed_dataframe = raspador_restaurante.clean_restaurant_df(raspador_restaurante.tables_on_page)

    # preparando as tabelas para inseri-las elemento a elemento no banco
    Restaurante_json = json.loads(parsed_dataframe.to_json(orient='records'))

    # inserção
    insert_items(Restaurante_json)

# função privada dentro desse módulo
def _get_collection():
    """
        Função que retorna a coleção de Restaurante
    """
    try:
        return get_db.get_collection(DBCollections.RESTAURANTE)
    except Exception as e:
        raise e





