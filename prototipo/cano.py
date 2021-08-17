# Aqui vamos construir os canos que sarão os obstáculos do nosso personagem
# Temos que pensar como fazer os sistema de tamanho e posição aleatória
import pygame


class Cano:
    def __init__(self, x):
        self.cano = pygame.transform.scale2x(x)
        self.lista_canos = []

    def criar_cano(self):
        cano = pygame.image.load('projeto-final-grupo-2-2021-1-main/prototipo/teste.png')
        cano = pygame.transform.scale2x(cano)
        novo = cano.get_rect(midtop = (382,308))
        return novo
