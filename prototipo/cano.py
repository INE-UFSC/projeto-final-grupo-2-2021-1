import pygame
import random

# Aqui vamos construir os canos que sarão os obstáculos do nosso personagem
# Temos que pensar como fazer os sistema de tamanho e posição aleatória

class Cano:
    def __init__(self, tamanho_tela):

        self.tamanho_tela = tamanho_tela

        bases = self.tamanhoCano(self.tamanho_tela)

        self.__x = 760
        self.__y1 = 0
        self.__y2 = bases[1]  
        self.base_superior = bases[0]
        self.base_inferior = self.tamanho_tela - bases[1] 
        self.__largura = 35

    @property
    def x(self):
        return self.__x

    def geraCano(self, tela):
        
        pygame.draw.rect(tela, (0, 255, 0), pygame.Rect(self.__x, self.__y1, self.__largura, self.base_superior))
        pygame.draw.rect(tela, (0, 255, 0), pygame.Rect(self.__x, self.__y2, self.__largura, self.base_inferior))

    def tamanhoCano(self, altura_tela):

        referenciaPadrao = altura_tela/8
        base_superior_cano = random.randint(int(referenciaPadrao), int(referenciaPadrao*6))
        base_inferior_cano = base_superior_cano + 2*int(referenciaPadrao)
        
        bases = [base_superior_cano, base_inferior_cano]

        return bases

    def move(self):
        self.__x += -5

    def destruir(self):
        self.__x = 760
