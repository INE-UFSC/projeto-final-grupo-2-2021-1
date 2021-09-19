import pygame
from constantes import Constante

class Cenario:
    def __init__(self):
        self.const = Constante()
        self.tela = pygame.display.set_mode((self.const.tela_jogo_largura,
            self.const.tela_jogo_altura))
        pygame.display.set_caption("Flappy Bird Ultimate Edition")
        self.velocidade_jogo = 0.5
    
    def inicializa_tela(self):
        self.tela.fill((0, 0, 150))
    
    def escreve_pontuacao(self, pontuacao):
        self.tela.blit(pontuacao, (self.const.tela_jogo_largura/2,20))
