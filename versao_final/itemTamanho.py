# Item com efeito de diminuir o tamanho do personagem 

import pygame
from item import Item
from animacao import ItemPequenoAnimacao


class ItemTamanho(Item):
    def __init__(self):
        super().__init__()
        self.__animacao_item = pygame.sprite.Group(ItemPequenoAnimacao())
        self.__tempo_efeito = self.const.tempo_pequeno
    
    @property
    def animacao_item(self):
        return self.__animacao_item
    
    @property
    def tempo_efeito(self):
        return self.__tempo_efeito
    
    @animacao_item.setter
    def animacao_item(self, animacao_item):
        self.__animacao_item = animacao_item
    
    @tempo_efeito.setter
    def tempo_efeito(self, tempo_efeito):
        self.__tempo_efeito = tempo_efeito

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
