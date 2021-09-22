import pygame
from cano import Cano
from animacao import CanoInferiorAnimacao, CanoSuperiorAnimacao

class CanoPadrao(Cano):
    def __init__(self):
        super().__init__()
        self.__cano_inferior = pygame.sprite.Group(CanoInferiorAnimacao())
        self.__cano_superior = pygame.sprite.Group(CanoSuperiorAnimacao())

    @property
    def cano_superior(self):
        return self.__cano_superior
    @property
    def cano_inferior(self):
        return self.__cano_inferior

    def efeito_colisao(self, personagem):
        if not personagem.invencivel:
            personagem.game_over = True
            self.colidiu = True

    def move(self):
        self.x += -5
