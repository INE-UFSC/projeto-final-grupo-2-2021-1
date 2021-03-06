# Item com efeito de tornar o personagem imune a colisões com os canos
# Ainda pode haver "game over", caso o personagem atinja o chão ou o topo da tela 

import pygame
from item import Item
from animacao import ItemInvencivelAnimacao


class ItemInvencibilidade(Item):
    def __init__(self):
        super().__init__()
        self.__animacao_item = pygame.sprite.Group(ItemInvencivelAnimacao())
        self.__tempo_efeito = self.const.tempo_invencibilidade

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
        self.__personagem.invencivel = True
        self.colidiu = True
        self.ativo = True
        personagem.animacao = personagem.animacao_item_efeito

    def reverter(self):
        self.__personagem.invencivel = False
        self.ativo = False
        self.__personagem.animacao = self.__personagem.animacao_personagem

    def tempo_item(self):
        return self.tempo_efeito
