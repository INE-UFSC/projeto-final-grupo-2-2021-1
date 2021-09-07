import pygame
import random
from constantes import Constante as const

# Aqui vamos construir os canos que sarão os obstáculos do nosso personagem
# Temos que pensar como fazer os sistema de tamanho e posição aleatória

class Cano:
    def __init__(self, tela_jogo):

        self.tela_jogo = tela_jogo
        self.largura_tela = const.tela_jogo_largura
        self.altura_tela = const.tela_jogo_altura
        self.__largura_cano = const.largura_cano
        self.__x = const.tela_jogo_largura
        self.__y1 = 0
        self.__y2 = 0
        self.base_superior = 0 
        self.base_inferior = 0
        self.tamanho_cano_definido = False

    @property
    def x(self):
        return self.__x

    def atualiza(self):
        if not self.tamanho_cano_definido:
            self.tamanho_cano()
        if self.__x < const.posicao_destruir:
            self.destruir()
        self.desenha_objeto()
        self.move()

    def tamanho_cano(self): #Altera o tamnho do cano

        referenciaPadrao = self.altura_tela/8
        base_superior_cano = random.randint(int(referenciaPadrao), int(referenciaPadrao*5))
        base_inferior_cano = base_superior_cano + 2*int(referenciaPadrao)
        
        self.bases = [base_superior_cano, base_inferior_cano]
        self.tamanho_cano_definido = True 
    
    def gera_retangulo(self):  # gera os retângulos que representarão os canos
        retangulo1 = pygame.Rect(self.__x, self.__y1, self.__largura_cano, self.base_superior)
        retangulo2 = pygame.Rect(self.__x, self.__y2, self.__largura_cano, self.base_inferior)
        return [retangulo1, retangulo2]
   
    def desenha_objeto(self): #Desenha o cano na tela do jogo
        retangulos = self.gera_retangulo()

        self.__y2 = self.bases[1]  
        self.base_superior = self.bases[0]
        self.base_inferior = self.altura_tela - self.bases[1] 
        pygame.draw.rect(self.tela_jogo, (0, 255, 0), retangulos[0])
        pygame.draw.rect(self.tela_jogo, (0, 255, 0), retangulos[1])

    def move(self):
        self.__x += -5

    def destruir(self):
        self.__x = self.largura_tela
        self.tamanho_cano_definido = False
