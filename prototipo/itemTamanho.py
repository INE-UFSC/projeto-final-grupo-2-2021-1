# Item com efeito de diminuir o tamanho do personagem 
from item import Item
from constantes import Constante 


class ItemTamanho(Item):
    def __init__(self):
        super().__init__()
        self.cor = (255, 255, 0)
        self.tempo_efeito = self.const.tempo_pequeno
    
    def efeito(self, personagem):
        self.__personagem = personagem
        self.__personagem.tamanho = 18
        self.colidiu = True
        self.ativo = True

    def reverter(self):
        self.__personagem.tamanho = 35
        self.ativo = False

    def tempo_item(self):
        return self.tempo_efeito