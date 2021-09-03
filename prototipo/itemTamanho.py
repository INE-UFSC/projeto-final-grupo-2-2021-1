# Item com efeito de diminuir o tamanho do personagem 

from item import Item


class ItemTamanho(Item):
    def __init__(self, tela_jogo, persongem):
        super().__init__(tela_jogo, persongem)
        self.cor = (255, 255, 0)
        self.personagem = persongem
    
    def efeito(self):
        self.personagem.tamanho = 18

    def reverter(self):
        self.personagem.tamanho = 35
