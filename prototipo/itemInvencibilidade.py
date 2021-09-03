# Item com efeito de tornar o personagem imune a colisões com os canos
# Ainda pode haver "game over", caso o personagem atinja o chão ou o topo da tela 

from item import Item


class ItemInvencibilidade(Item):
    def __init__(self, tela_jogo, personagem):
        super().__init__(tela_jogo, personagem)
        self.personagem = personagem

    def efeito(self):
        self.personagem.invencivel = True
        self.personagem.cor = (0, 0, 0)

    def reverter(self):
        self.personagem.invencivel = False
        self.personagem.cor = (255, 0, 0)
