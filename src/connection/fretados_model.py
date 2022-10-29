from dataclasses import dataclass
from database import get_db
import json
from raspador_fretados import tables_on_page, clean_bus_df

@dataclass
class FretadoModel:
    """
        Classe que se connecta e performa requisições na coleção: Fretados.
    """

    def list_all(self):
        """
            retorna todos os fretados
        """

        return self.__get_collection().find()

    def next_bus_sa_sbc(self, horario):
        return self.__get_collection().find( { "santo andre partida" : { "$exists" : True } , "sao bernardo chegada" : { "$exists" : True } })

    def find_by_linha(self, linha):
        return self.__get_collection().findOne({ "linha": linha })

    def insert_item(self, item):
        return self.__get_collection().insert_one(item)

    def insert_items(self, items):
        return self.__get_collection().insert_many(items)

    def delete_all(self):
        return self.__get_collection().drop()

    def populate_database(self):
        # deleta o conteúdo atual do banco
        self.delete_all()

        # get dataframe
        parsed_dataframe = clean_bus_df(tables_on_page)

        # preparando as tabelas para inseri-las elemento a elemento no banco
        fretados_json = json.loads(parsed_dataframe.to_json(orient='records'))

        # inserção
        self.insert_items(fretados_json)

    def __get_collection(self):
        return get_db.get_collection("fretados")
