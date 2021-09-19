# Item com efeito de tornar o personagem imune a colisões com os canos
# Ainda pode haver "game over", caso o personagem atinja o chão ou o topo da tela 

from item import Item
from constantes import Constante


class ItemInvencibilidade(Item):
    def __init__(self):
        super().__init__()
        self.tempo_efeito = self.const.tempo_invencibilidade

    def efeito(self, personagem):
        self.__personagem = personagem
        self.__personagem.invencivel = True
        self.__personagem.cor = (0, 0, 0)
        self.colidiu = True
        self.ativo = True

    def reverter(self):
        self.__personagem.invencivel = False
        self.__personagem.cor = (255, 0, 0)
        self.ativo = False

    def tempo_item(self):
        return self.tempo_efeito