import pygame
from tela import Tela
from singleton import Singleton
from cenario import Cenario


class CenarioMenu(Cenario, Singleton):
    def __init__(self, legenda='Flappy Bird Ultimate Edition'):
        super().__init__(legenda=legenda)
        self.fundo = pygame.image.load('versao_final/sprites/menu/ceumenu.png')
        self.fundo = pygame.transform.scale(self.fundo, (int(3072/2.4), (int(1536/2.4))))
        self.chao = pygame.image.load('versao_final/sprites/menu/chaomenu.png')
        self.chao = pygame.transform.scale(self.chao, (int(3072/2.4), (int(1536/2.4))))
        self.posicao_chao = 0


    def inicializa_tela(self):
        if self.posicao_chao <= -85.4:
            self.posicao_chao = 0
        self.tela.blit(self.fundo, (0, 0))
        self.tela.blit(self.chao, (self.posicao_chao, 0))
        self.posicao_chao -= 1.5

