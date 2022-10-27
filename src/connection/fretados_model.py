from dataclasses import dataclass
from urllib import response
from database import get_db, DBconfig

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

    def __get_collection(self):
        return get_db.get_collection("fretados")

