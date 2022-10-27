from dataclasses import dataclass
from database import get_db, DBconfig

@dataclass
class FretadoModel:
    """
        Classe que se connecta e performa requisições na coleção: Fretados.
    """

    def listAll(self):
        """
            retorna todos os fretados
        """
        return self.__get_collection().find()

    def findByLinha(self, linha):
        return self.__get_collection().findOne({ "linha": linha })
        
    def insertItem(self, item):
        return self.__get_collection().insert_one(item)

    def insertItems(self, items):
        return self.__get_collection().insert_many(items)

    def deleteAll(self):
        return self.__get_collection().remove()

    def __get_collection(self):
        return get_db["fretados"]  
