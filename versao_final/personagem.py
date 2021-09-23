# Aqui a gente vai construir a classe do nosso personagem
# A ideia posteriormente é especializar essa classe, tendo vários personagens com características diferentes

import pygame
from constantes import Constante
from abc import ABC, abstractmethod
from animacao import PersonagemAnimacao

class Personagem(ABC):
    def __init__(self):
        self.__const = Constante()
        self.__animacao = pygame.sprite.Group(PersonagemAnimacao())
        self.__x = self.__const.posicao_personagem_x
        self.__y = self.__const.posicao_personagem_y
        self.__tecla_pressionada = False
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def tecla_pressionada(self):
        return self.__tecla_pressionada
    
    @property
    def animacao(self):
        return self.__animacao
    
    @property
    def const(self):
        return self.__const
    
    @x.setter
    def x(self, x):
        self.__x = x
    
    @y.setter
    def y(self, y):
        self.__y = y

    @tecla_pressionada.setter
    def tecla_pressionada(self, tecla_pressionada):
        self.__tecla_pressionada = tecla_pressionada
    
    @animacao.setter
    def animacao(self, animacao):
        self.__animacao = animacao

    @const.setter
    def const(self, const):
        self.__const = const

    def gera_retangulo(self):  # gera o retângulo referente à posição do personagem
        retangulo = self.__animacao.sprites()[0].rect
        return retangulo

    def desenha_personagem(self, tela):
        self.__animacao.update(self.__x, self.__y)
        self.__animacao.draw(tela)

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def morreu(self):
        pass
    