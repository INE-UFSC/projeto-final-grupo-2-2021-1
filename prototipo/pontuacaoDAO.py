from DAO import DAO
from pontuacao import Pontuacao

class PontuacaoDAO(DAO):
    def __init__(self, datasource) -> None:
        super().__init__('pontuacao.pkl')
    
    def add(self, pontuacao: Pontuacao):
        if ((pontuacao is not None) and isinstance(pontuacao, Pontuacao)):
            super().add(pontuacao.nome, pontuacao)

    def get(self, key):
        return super().get(key)
    
    def remove(self, key):
        return super().remove(key)
