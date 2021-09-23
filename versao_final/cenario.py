import pygame
from tela import Tela
from singleton import Singleton
from animacao import ChaoAnimacao


class Cenario(Tela, Singleton):
    def __init__(self, legenda='Flappy Bird Ultimate Edition'):
        super().__init__(legenda=legenda)
        self.fundo = pygame.image.load('versao_final/sprites/cenario/ceu.png')
        self.fundo = pygame.transform.scale(self.fundo, (int(3072/2.4), (int(1536/2.4))))
        self.chao = pygame.sprite.Group(ChaoAnimacao())

    def inicializa_tela(self):
        self.tela.blit(self.fundo, (0, 0))
    
    def atualiza_chao(self, personagem):
        if personagem.voando and not personagem.game_over:
            self.chao.sprites()[0].move_chao()
        self.chao.update()
        self.chao.draw(self.tela)
    
    def escreve_pontuacao(self, pontuacao):
        self.tela.blit(pontuacao, (self.const.tela_jogo_largura/2, 20))
