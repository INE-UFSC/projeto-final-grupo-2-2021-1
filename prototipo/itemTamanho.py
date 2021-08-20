# Item com efeito de diminuir o tamanho do personagem 

from itens import Itens


class ItemTamanho(Itens):
    def __init__(self, largura_tela, altura_tela, tela_jogo, posicao_gera_cano):
        super().__init__(largura_tela, altura_tela, tela_jogo, posicao_gera_cano)
        self.cor = (255, 255, 0)
    
    def efeito(self, personagem):
        personagem.tamanho = 18

    def reverter(self, personagem):
        personagem.tamanho = 35
