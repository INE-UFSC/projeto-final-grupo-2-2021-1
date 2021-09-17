#Essa classe irá realizar o calculo dos pontos, e posteriormente enviar para o banco de dados
from singleton import Singleton
import pygame, sys
from pygame.locals import *

class Pontuacao(Singleton):
    def __init__(self) -> None:
        self.__pontos = 0
        pygame.font.init()
        self.__fonte = pygame.font.SysFont('Comic Sans MS', 30)

    def marca_ponto(self, valor_ponto):
        self.__pontos += valor_ponto
    
    def mostra_ponto(self):
        texto_ponto = self.__fonte.render(str(self.__pontos), False, (255,255,255))
        return texto_ponto
        