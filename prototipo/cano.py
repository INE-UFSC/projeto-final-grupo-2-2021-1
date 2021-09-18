import pygame
import random
from constantes import Constante

# Aqui vamos construir os canos que sarão os obstáculos do nosso personagem
# Temos que pensar como fazer os sistema de tamanho e posição aleatória

class Cano:
    def __init__(self, tela_jogo):

        self.const = Constante()
        self.tela_jogo = tela_jogo
        self.__x = self.const.tela_jogo_largura
        self.__y1 = 0
        self.__y2 = 0
        self.base_superior = 0 
        self.base_inferior = 0
        self.tamanho_cano_definido = False
        self.colidiu = False

    @property
    def x(self):
        return self.__x

    def atualiza(self):
        if not self.tamanho_cano_definido:
            self.tamanho_cano()
        self.desenha_objeto()

    def tamanho_cano(self): #Altera o tamnho do cano

        referenciaPadrao = self.const.tela_jogo_altura/8
        base_superior_cano = random.randint(int(referenciaPadrao), int(referenciaPadrao*5))
        base_inferior_cano = base_superior_cano + 2*int(referenciaPadrao)
        
        self.bases = [base_superior_cano, base_inferior_cano]
        self.tamanho_cano_definido = True 
    
    def gera_retangulo(self):  # gera os retângulos que representarão os canos
        retangulo1 = pygame.Rect(self.__x, self.__y1, self.const.largura_cano, self.base_superior)
        retangulo2 = pygame.Rect(self.__x, self.__y2, self.const.largura_cano, self.base_inferior)
        return [retangulo1, retangulo2]

    def desenha_objeto(self): #Desenha o cano na tela do jogo
        retangulos = self.gera_retangulo()

        self.__y2 = self.bases[1]  
        self.base_superior = self.bases[0]
        self.base_inferior = self.const.tela_jogo_altura - self.bases[1] 
        pygame.draw.rect(self.tela_jogo, (0, 255, 0), retangulos[0])
        pygame.draw.rect(self.tela_jogo, (0, 255, 0), retangulos[1])

    def efeito_colisao(self, personagem):
        if not personagem.invencivel:
            personagem.game_over = True
            self.colidiu = True

    def move(self):
        self.__x += -5