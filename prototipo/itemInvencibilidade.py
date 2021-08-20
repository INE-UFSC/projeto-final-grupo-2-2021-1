# Item com efeito de tornar o personagem imune a colisões com os canos
# Ainda pode haver "game over", caso o personagem atinja o chão ou o topo da tela 

from itens import Itens


class ItemInvencibilidade(Itens):
    def __init__(self, largura_tela, altura_tela, tela_jogo, posicao_gera_cano):
        super().__init__(largura_tela, altura_tela, tela_jogo, posicao_gera_cano)
    
    def efeito(self, personagem):
        personagem.invencivel = True
    
    def reverter(self, personagem):
        personagem.invencivel = False
