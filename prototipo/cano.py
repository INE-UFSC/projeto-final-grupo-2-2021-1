import pygame
import random

# Aqui vamos construir os canos que sarão os obstáculos do nosso personagem
# Temos que pensar como fazer os sistema de tamanho e posição aleatória



class Cano:
    def __init__(self):
        super().__init__() 

        bases = self.tamanhoCano(760)
        
        self.__largura = 35
        self.base_superior = bases[0]
        self.base_inferior = 120   
        self.__x = 760
        self.__y1 = 0
        self.__y2 = bases[1]  


    def geraCano(self, tela):

        bases = self.tamanhoCano(760)
        pygame.draw.rect(tela, (0, 255, 0), pygame.Rect(self.__x, self.__y1, self.__largura, self.base_superior))
        pygame.draw.rect(tela, (0, 255, 0), pygame.Rect(self.__x, self.__y2, self.__largura, self.base_inferior))

    def tamanhoCano(self, altura_tela):

        referenciaPadrao = altura_tela/6
        base_superior_cano = random.randint(int(referenciaPadrao), int(referenciaPadrao*4))
        base_inferior_cano = base_superior_cano + int(referenciaPadrao)
        
        bases = [base_superior_cano, base_inferior_cano]

        return bases

    def move(self):
        self.__x += -5
