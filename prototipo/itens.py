import pygame
import random

# Aqui vamos construir os canos que sarão os obstáculos do nosso personagem
# Temos que pensar como fazer os sistema de tamanho e posição aleatória

class Itens:
    def __init__(self, largura_tela, altura_tela, tela_jogo, posicao_gera_cano):

        self.largura_cano = 40
        self. posicao_gera_cano = posicao_gera_cano
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.tela_jogo = tela_jogo
        self.largura_item = 15
        self.__x = 0
        self.__y = 300
        self.distancia_do_cano = 70

    @property
    def x(self):
        return self.__x

    def posicao_tela(self): #Sorteia uma posicão que o item vai ficar na tela

        range_inicio = self.largura_tela + self.distancia_do_cano + self.largura_cano
        range_final = self.largura_tela + \
                    (self.largura_tela - (self.posicao_gera_cano + self.distancia_do_cano))

        self.__x = random.randint(range_inicio, range_final)

    def desenha_objeto(self): #Desenha o item na tela do jogo
            
        pygame.draw.rect(self.tela_jogo, (30, 0, 180), pygame.Rect(self.__x, 300, self.largura_item, self.largura_item,))
   
    def move(self):
        self.__x += -5

    def destruir(self):
        self.__x = 780
