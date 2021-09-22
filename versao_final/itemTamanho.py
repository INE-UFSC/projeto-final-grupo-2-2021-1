# Item com efeito de diminuir o tamanho do personagem 
from item import Item
from constantes import Constante 
from animacao import ItemPequenoAnimacao
import pygame

class ItemTamanho(Item):
    def __init__(self):
        super().__init__()
        self.__animacao_item = pygame.sprite.Group(ItemPequenoAnimacao())
        self.cor = (255, 255, 0)
        self.tempo_efeito = self.const.tempo_pequeno
    
    @property
    def animacao_item(self):
        return self.__animacao_item

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