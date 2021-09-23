from DAO import DAO
from pontuacao import Pontuacao

class PontuacaoDAO(DAO):
    def __init__(self) -> None:
        super().__init__('pontuacao.pkl')
    
    def add(self, nome: str, pontuacao: int):
        if ((nome is not None) and isinstance(nome, str)):
            super().add(nome, pontuacao)

    def get(self, key):
        return super().get(key)
    
    def remove(self, key):
        return super().remove(key)
