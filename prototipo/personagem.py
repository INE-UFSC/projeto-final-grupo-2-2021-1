# Aqui a gente vai construir a classe do nosso personagem
# A ideia posteriormente é especializar essa classe, tendo vários personagens com características diferentes

from typing import List
from cano import Cano
import pygame


class Personagem:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.velocidade = 0
        self.__tecla_pressionada = False
        self.voando = False
        self.game_over = False
        self.tamanho = 35
        self.invencivel = False
        self.cor = (255, 0, 0)
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def tecla_pressionada(self):
        return self.__tecla_pressionada

    def gera_retangulo(self):  # gera o retângulo referente à posição do personagem
        retangulo = pygame.Rect(self.__x, self.__y, self.tamanho, self.tamanho)
        return retangulo

    def desenha_personagem(self, tela):
        pygame.draw.rect(tela, self.cor, self.gera_retangulo())

    def mover(self):
        # confere se o personagem está voando para aplicar a gravidade sobre ele
        if self.voando:
            self.velocidade += 0.5   # medida que o personagem desce a cada loop
            if self.velocidade > 8:   # evita que o personagem caia muito rapidamente
                self.velocidade = 8
            if self.__y < 600:  # se o personagem não estiver no chão, atualiza sua posição
                self.__y += int(self.velocidade)

        # controle do pulo do personagem
        if not self.game_over:
            teclas = pygame.key.get_pressed()  # verifica quais teclas foram pressionadas
            if teclas[pygame.K_UP] and self.__tecla_pressionada == False:
                self.__tecla_pressionada = True
                self.velocidade = -10
            
            if not teclas[pygame.K_UP]:
                self.__tecla_pressionada = False

    
    def morreu(self):
        # checa se o personagem atingiu o chão
        if self.__y > 600:
            self.game_over = True
            self.voando = False
        # checa se o personagem saiu da tela
        elif self.__y <= 0:
            self.game_over = True
    