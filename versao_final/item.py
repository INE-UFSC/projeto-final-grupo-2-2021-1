import random
from constantes import Constante
from abc import ABC, abstractmethod
import pygame


class Item(ABC):
    def __init__(self):
        self.__const = Constante()
        self.__x = 0
        self.__y = 0
        self.__criado = False
        self.__colidiu = False
        self.__ativo = False
        self.__final_efeito = 0
        self.__colisao_som = pygame.mixer.Sound("versao_final/sons/efeitos/item_colisao.wav")
    
    @property
    def const(self):
        return self.__const

    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def criado(self):
        return self.__criado
    
    @property
    def colidiu(self):
        return self.__colidiu
    
    @property
    def ativo(self):
        return self.__ativo
    
    @property
    def final_efeito(self):
        return self.__final_efeito
    
    @const.setter
    def const(self, const):
        self.__const = const
    
    @x.setter
    def x(self, x):
        self.__x = x
    
    @y.setter
    def y(self, y):
        self.__y = y
    
    @criado.setter
    def criado(self, criado):
        self.__criado = criado
    
    @colidiu.setter
    def colidiu(self, colidiu):
        self.__colidiu = colidiu
    
    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo
    
    @final_efeito.setter
    def final_efeito(self, final_efeito):
        self.__final_efeito = final_efeito

    @property
    def colisao_som(self):
        return self.__colisao_som

    @colisao_som.setter
    def colisao_som(self, colisao_som):
        self.__colisao_som = colisao_som

    def atualiza(self, tela_jogo): #Faz todo o processo de gerar o item, aplicar o movimento e destruir
        if not self.__criado:
            self.define_posicao_tela()
        self.desenha_objeto(tela_jogo)

    def define_posicao_tela(self): #Sorteia uma posicão que o item vai ficar na tela

        range_inicio_y = self.__const.distancia_item_cano
        range_final_y = self.__const.tela_jogo_altura - self.__const.distancia_item_cano

        self.__y = random.randint(range_inicio_y, range_final_y)

        range_inicio_x = self.__const.tela_jogo_largura + self.__const.distancia_item_cano + self.__const.largura_cano
        range_final_x = self.__const.tela_jogo_largura + \
                    (self.__const.tela_jogo_largura - (self.__const.posicao_gera_cano + self.__const.distancia_item_cano))

        self.__x = random.randint(range_inicio_x, range_final_x)
        self.__criado = True

    def gera_retangulo(self):    # gera o retângulo que representa a posição do item
        rect = self.animacao_item.sprites()[0].rect
        return [rect]

    def desenha_objeto(self, tela_jogo): #Desenha o item na tela do jogo
        self.animacao_item.update(self.__x, self.__y)
        self.animacao_item.draw(tela_jogo)

    def move(self):
        self.__x += -5
    
    def efeito_colisao(self, personagem):
        self.colisao_som.set_volume(0.3)
        self.colisao_som.play()
        self.efeito(personagem)

    def tempo(self, tempo_atual):
        self.__final_efeito = tempo_atual + self.tempo_item()

    def duracao_item(self, contador):
        if self.__colidiu:
            self.tempo(int(contador.tempo_contado))
            self.__colidiu = False

        if self.__final_efeito == contador.tempo_contado:
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
