# Aqui a gente vai coonstruir a classe do nosso personagem
# A ideia posteriormente é especializar essa classe, tendo varios personagens com caracterśticas diferentes

import pygame


class Personagem:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.velocidade = 0
        self.__tecla_pressionada = False
        self.voando = False
        self.game_over = False
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def tecla_pressionada(self):
        return self.__tecla_pressionada

    def desenha_personagem(self, tela):
        pygame.draw.rect(tela, (255, 0, 0), pygame.Rect(self.__x, self.__y, 35, 35))

    def mover(self):
        # gravidade
        if self.voando:
            self.velocidade += 0.5
            if self.velocidade > 8:
                self.velocidade = 8
            if self.__y < 600:
                self.__y += int(self.velocidade)

        # pulo
        teclas = pygame.key.get_pressed()  # verifica quais teclas foram pressionadas
        if teclas[pygame.K_UP] and self.__tecla_pressionada == False:
            self.__tecla_pressionada = True
            self.velocidade = -10
        
        if not teclas[pygame.K_UP]:
            self.__tecla_pressionada = False
        
        self.morreu()
    
    def morreu(self):
        # checar se passaro caiu
        if self.__y > 600:
            self.game_over = True
            self.voando = False
