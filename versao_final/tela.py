import pygame
from constantes import Constante
from abc import ABC, abstractmethod


class Tela(ABC):
    def __init__(self, legenda='Flappy Bird Ultimate Edition'):
        self.__const = Constante()
        self.__tela = pygame.display.set_mode((self.const.tela_jogo_largura,
            self.const.tela_jogo_altura))
        pygame.display.set_caption(legenda)

    @property
    def const(self):
        return self.__const
    
    @const.setter
    def const(self, const):
        self.__const = const
    
    @property
    def tela(self):
        return self.__tela
    
    @tela.setter
    def tela(self, tela):
        self.__tela = tela

    @abstractmethod
    def inicializa_tela(self):
        pass
