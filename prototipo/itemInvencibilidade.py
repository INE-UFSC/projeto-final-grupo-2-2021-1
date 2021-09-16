# Item com efeito de tornar o personagem imune a colisões com os canos
# Ainda pode haver "game over", caso o personagem atinja o chão ou o topo da tela 

from contador import Contador
from item import Item
from constantes import Constante as const

class ItemInvencibilidade(Item):
    def __init__(self, tela_jogo):
        super().__init__(tela_jogo)
        self.__contador = Contador()

    def efeito(self, personagem):
        self.__personagem = personagem
        self.__personagem.invencivel = True
        self.__personagem.cor = (0, 0, 0)
        self.colidiu = True

    def reverter(self):
        self.__personagem.invencivel = False
        self.__personagem.cor = (255, 0, 0)
        self.colidiu = False

    def tempo_efeito(self):
        if self.__contador.duracao_item(const.tempo_invencibilidade) == True:
            self.reverter()
            return True
        return False

    
        
