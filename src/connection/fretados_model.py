from dataclasses import dataclass
from urllib import response
from database import get_db, DBconfig
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

        # preparando as tabelas para inseri-las elemento a elemento no banco
        fretados_json = [ json.loads(table.to_json(orient='records')) for table in clean_bus_df(tables_on_page) ]

        # inserção multipla
        for table_json in fretados_json:
            self.insert_items(table_json)

    def __get_collection(self):
        return get_db.get_collection("fretados")
