import pygame


class Cenario:
    def __init__(self):
        self.largura_tela = 780
        self.altura_tela = 640
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        pygame.display.set_caption("Flappy Bird Ultimate Edition")
        self.velocidade_jogo = 0.5

    def tela(self):
        return self.tela
