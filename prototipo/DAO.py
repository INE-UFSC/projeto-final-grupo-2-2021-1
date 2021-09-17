from abc import ABC
import pickle


class DAO(ABC):
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.load()
        except FileNotFoundError:
            self.dump()
    
    def dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))
    
    def load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))
    
    def add(self, key, obj):
        self.__cache[key] = obj
        self.dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            raise KeyError

    def remove(self, key):
        try:
            del self.__cache[key]
            self.dump()
        except KeyError:
            raise KeyError

    def get_all(self):
        return self.__cache.values()
