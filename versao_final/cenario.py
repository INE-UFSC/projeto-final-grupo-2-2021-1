import pygame
from tela import Tela
from singleton import Singleton


class Cenario(Tela, Singleton):
    def __init__(self, legenda='Flappy Bird Ultimate Edition'):
        super().__init__(legenda=legenda)
        self.fundo = pygame.image.load('versao_final/sprites/cenario/ceu.png')
        self.chao = pygame.image.load('versao_final/sprites/cenario/chao.png')
        self.ajusta_sprites()
        self.posicao_chao = 0

    def ajusta_sprites(self):
        self.fundo = pygame.transform.scale(self.fundo, (int(3072/2.4), (int(1536/2.4))))
        self.chao = pygame.transform.scale(self.chao, (int(3072/2.4), (int(1536/2.4))))

    def inicializa_tela(self):
        if self.posicao_chao <= -85.4:
            self.posicao_chao = 0
        self.tela.blit(self.fundo, (0, 0))
        self.tela.blit(self.chao, (self.posicao_chao, 0))
        self.posicao_chao -= 1.5
    
    def escreve_pontuacao(self, pontuacao):
        self.tela.blit(pontuacao, (self.const.tela_jogo_largura/2, 20))
