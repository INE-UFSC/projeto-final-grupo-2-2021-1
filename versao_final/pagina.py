from abc import ABC, abstractclassmethod
import pygame, sys
from constantes import Constante
from cenario import Cenario

class Pagina(ABC):
    def __init__(self):
        self.const = Constante()
        self.__fonte = pygame.font.get_default_font()
        self.botoes = []
        self.click = False
        self.cenario = Cenario()

    def desenha_texto(self, texto, tamanho, x, y):
        fonte = pygame.font.Font(self.__fonte, tamanho)
        superficie = fonte.render(texto, True, (255,255,255))
        texto_rect = superficie.get_rect()
        texto_rect.center = (x,y)
        self.cenario.tela.blit(superficie, texto_rect)
        self.mainclock = pygame.time.Clock()

    def atualizatela(self):
        pygame.display.update()
        self.mainclock.tick(self.const.fps)

    def resetaclick(self):
        self.click = False

    @abstractclassmethod
    def decta_colisão(self):       
        acao = False
        if botao.collidepoint(pygame.mouse.get_pos()):
            if self.click:
                acao = True
        return acao

    @abstractclassmethod
    def desenha_botao(self, x, y, tamanhox, tamanhoy):
        botao = pygame.Rect(x, y, tamanhox, tamanhoy)
        pygame.draw.rect(self.cenario.tela, (255,0,0), botao)
    
    @abstractclassmethod
    def mostra_pagina(self):          
        pass