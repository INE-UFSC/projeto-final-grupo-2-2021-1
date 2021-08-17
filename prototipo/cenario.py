import pygame


class Cenario:
    def __init__(self):
        self.largura_tela = 764
        self.altura_tela = 636
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        pygame.display.set_caption("Flappy Bird Ultimate Edition")
        self.velocidade_jogo = 0.5

    def tela(self):
        return self.tela
