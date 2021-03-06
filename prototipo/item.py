from abc import ABC, abstractmethod
import pygame
import random
from personagem import Personagem
from contador import Contador
from constantes import Constante

# Aqui vamos construir os canos que sarão os obstáculos do nosso personagem
# Temos que pensar como fazer os sistema de tamanho e posição aleatória

class Item(ABC):
    def __init__(self):
        self.const = Constante()
        self.itens = []  
        self.criado = False
        self.colidiu = False
        self.ativo = False
        self.final_efeito = 0
        self.__x = 0
        self.__y = 0
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

    def atualiza(self, tela_jogo): #Faz todo o processo de gerar o item, aplicar o movimento e destruir
        if not self.criado:
            self.define_posicao_tela()
        self.desenha_objeto(tela_jogo)

    def define_posicao_tela(self): #Sorteia uma posicão que o item vai ficar na tela

        range_inicio_y = self.const.distancia_item_cano
        range_final_y = self.const.tela_jogo_altura - self.const.distancia_item_cano

        self.__y = random.randint(range_inicio_y, range_final_y)

        range_inicio_x = self.const.tela_jogo_largura + self.const.distancia_item_cano + self.const.largura_cano
        range_final_x = self.const.tela_jogo_largura + \
                    (self.const.tela_jogo_largura - (self.const.posicao_gera_cano + self.const.distancia_item_cano))

        self.__x = random.randint(range_inicio_x, range_final_x)
        self.criado = True

    def gera_retangulo(self):    # gera o retângulo que representa a posição do item
        retangulo = pygame.Rect(self.__x, self.__y, self.const.largura_item, self.const.largura_item)

        return [retangulo]

    def desenha_objeto(self, tela_jogo): #Desenha o item na tela do jogo
        lista_retangulo = self.gera_retangulo()

        pygame.draw.rect(tela_jogo, self.cor, lista_retangulo[0])

    def move(self):
        self.__x += -5
    
    def efeito_colisao(self, personagem):
        self.efeito(personagem)

    def tempo(self, tempo_atual):
        self.final_efeito = tempo_atual + self.tempo_item()

    def duracao_item(self, contador):
        
        if self.colidiu == True:
            self.tempo(int(contador.tempo_contado))
            self.colidiu = False

        if self.final_efeito == contador.tempo_contado:
            self.reverter()

    @abstractmethod
    def tempo_item(self): #Retornar o tempo de duração do efeito do item
        pass 

    @abstractmethod
    def efeito(self, personagem):  # aplica o efeito do item, método a ser especializado nas subclasses
        pass
    
    @abstractmethod
    def reverter(self):  # reverte o efeito do item
        pass


