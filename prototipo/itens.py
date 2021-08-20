import pygame
import random
from contador import Contador

# Aqui vamos construir os canos que sarão os obstáculos do nosso personagem
# Temos que pensar como fazer os sistema de tamanho e posição aleatória

class Itens:
    def __init__(self, largura_tela, altura_tela, tela_jogo, posicao_gera_cano):

        self.criado = False
        self.coletado = False
        self.largura_cano = 40
        self.posicao_gera_cano = posicao_gera_cano
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.tela_jogo = tela_jogo
        self.largura_item = 20
        self.__x = 0
        self.__y = 0
        self.distancia_do_cano = 70
        self.__timer = None
        self.cor = (160, 160, 160)

    @property
    def x(self):
        return self.__x
    
    @property
    def timer(self):
        return self.__timer
    
    @timer.setter
    def timer(self, tempo):
        self.__timer = tempo

    def posicao_tela(self): #Sorteia uma posicão que o item vai ficar na tela

        range_inicio_y = self.distancia_do_cano
        range_final_y = self.altura_tela - self.distancia_do_cano

        self.__y = random.randint(range_inicio_y, range_final_y)

        range_inicio_x = self.largura_tela + self.distancia_do_cano + self.largura_cano
        range_final_x = self.largura_tela + \
                    (self.largura_tela - (self.posicao_gera_cano + self.distancia_do_cano))

        self.__x = random.randint(range_inicio_x, range_final_x)
        self.criado = True

    def gera_retangulo(self):    # gera o retângulo que representa a posição do item
        retangulo = pygame.Rect(self.__x, self.__y, self.largura_item, self.largura_item)
        return retangulo

    def desenha_objeto(self): #Desenha o item na tela do jogo
        pygame.draw.rect(self.tela_jogo, self.cor, self.gera_retangulo())

    def move(self):
        self.__x += -5

    def destruir(self):
        self.__x = 780
        self.criado = False
    
    def efeito(self, personagem):  # aplica o efeito do item, método a ser especializado nas subclasses
        pass

    def reverter(self, personagem):  # reverte o efeito do item
        pass
