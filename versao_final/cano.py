import pygame
import random
from constantes import Constante
from abc import ABC, abstractmethod

# Aqui vamos construir os canos que sarão os obstáculos do nosso personagem
# Temos que pensar como fazer os sistema de tamanho e posição aleatória


class Cano(ABC):
    def __init__(self):
        self.__const = Constante()
        self.__x = self.__const.tela_jogo_largura
        self.__y1 = 0
        self.__y2 = 0
        self.__base_superior = 0 
        self.__base_inferior = 0
        self.__tamanho_cano_definido = False
        self.__colidiu = False

    @property
    def const(self):
        return self.__const

    @property
    def x(self):
        return self.__x
    
    @property
    def y1(self):
        return self.__y1
    
    @property
    def y2(self):
        return self.__y2
    
    @property
    def base_superior(self):
        return self.__base_superior
    
    @property
    def base_inferior(self):
        return self.__base_inferior
    
    @property
    def tamanho_cano_definido(self):
        return self.__tamanho_cano_definido
    
    @property
    def colidiu(self):
        return self.__colidiu

    @const.setter
    def const(self, const):
        self.__const = const
    
    @x.setter
    def x(self, x):
        self.__x = x

    @y1.setter
    def y1(self, y1):
        self.__y1 = y1
    
    @y2.setter
    def y2(self, y2):
        self.__y2 = y2
    
    @base_superior.setter
    def base_superior(self, base_superior):
        self.__base_superior = base_superior
    
    @base_inferior.setter
    def base_inferior(self, base_inferior):
        self.__base_inferior = base_inferior

    @tamanho_cano_definido.setter
    def tamanho_cano_definido(self, tamanho_cano_definido):
        self.__tamanho_cano_definido = tamanho_cano_definido
    
    @colidiu.setter
    def colidiu(self, colidiu):
        self.__colidiu = colidiu

    def atualiza(self, tela_jogo):
        if not self.__tamanho_cano_definido:
            self.tamanho_cano()
        self.desenha_objeto(tela_jogo)

    def tamanho_cano(self): #Altera o tamanho do cano
        referencia_padrao = self.__const.tela_jogo_altura/8
        base_superior_cano = random.randint(int(referencia_padrao), int(referencia_padrao*5))
        base_inferior_cano = base_superior_cano + 2*int(referencia_padrao)
        
        self.bases = [base_superior_cano, base_inferior_cano]
        self.__tamanho_cano_definido = True 
    
    def gera_retangulo(self):  # gera os retângulos que representarão os canos
        retangulo1 = pygame.Rect(self.__x, self.__y1, self.__const.largura_cano, self.__base_superior)
        retangulo2 = pygame.Rect(self.__x, self.__y2, self.__const.largura_cano, self.__base_inferior)
        return [retangulo1, retangulo2]

    def desenha_objeto(self, tela_jogo): #Desenha o cano na tela do jogo
        retangulos = self.gera_retangulo()

        self.__y2 = self.bases[1]  
        self.__base_superior = self.bases[0]
        self.__base_inferior = self.__const.tela_jogo_altura - self.bases[1] 
        pygame.draw.rect(tela_jogo, (0, 255, 0), retangulos[0])
        pygame.draw.rect(tela_jogo, (0, 255, 0), retangulos[1])

    @abstractmethod
    def efeito_colisao(self):
        pass

    @abstractmethod
    def move(self):
        pass
