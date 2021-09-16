# Item com efeito de diminuir o tamanho do personagem 
from contador import Contador
from item import Item
from constantes import Constante as const

class ItemTamanho(Item):
    def __init__(self, tela_jogo):
        super().__init__(tela_jogo)
        self.cor = (255, 255, 0)
        self.tempo_efeito = const.tempo_pequeno
    
    def efeito(self, personagem):
        self.__personagem = personagem
        self.__personagem.tamanho = 18
        self.colidiu = True
        self.ativo = True

    def reverter(self):
        self.__personagem.tamanho = 35
        self.ativo = False
