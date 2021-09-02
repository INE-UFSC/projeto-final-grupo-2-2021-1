# Item com efeito de tornar o personagem imune a colisões com os canos
# Ainda pode haver "game over", caso o personagem atinja o chão ou o topo da tela 

from item import Item


class ItemInvencibilidade(Item):
    def __init__(self, largura_tela, altura_tela, tela_jogo, posicao_gera_cano):
        super().__init__(largura_tela, altura_tela, tela_jogo, posicao_gera_cano)
    
    def efeito(self, personagem):
        personagem.invencivel = True
        personagem.cor = (0, 0, 0)
    
    def reverter(self, personagem):
        personagem.invencivel = False
        personagem.cor = (255, 0, 0)
