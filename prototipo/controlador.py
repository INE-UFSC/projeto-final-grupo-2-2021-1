import pygame
from pygame.locals import *
from personagem import Personagem
from cano import Cano
from cenario import Cenario
from itemInvencibilidade import ItemInvencibilidade
from itemTamanho import ItemTamanho
from contador import Contador
from constantes import Constante as const


class Controlador:
    def __init__(self) -> None:
        self.__personagem = Personagem(const.posicao_personagem_x, const.posicao_personagem_y)
        self.__cenario = Cenario()
        self.__contador = Contador()
        self.instancia_canos()
        self.instancia_itens()
        self.__lista_objetos = []

    def inciar(self):

        pygame.init()
        clock = pygame.time.Clock()
        self.__cenario.tela.fill((0, 0, 150))

        rodando = True
        while rodando:

            clock.tick(const.fps)
            self.__contador.contador_tempo()


    def gera_objetos(self):
        for objeto in self.__lista_objetos:
            objeto.atualizar()

        self.controla_canos()

    def controla_canos(self): #Controla os canos da lista de objetos que são gerados
        if not self.__lista_objetos:
            self.__lista_objetos.append(self.__cano_1)

        for objeto in self.__lista_objetos:
            if isinstance(objeto, Cano):
                if objeto.x == const.posicao_gera_cano:
                    if self.__cano_1.tamanho_cano_definido == False:
                        self.__lista_objetos.append(self.__cano_1)
                    elif self.__cano_2.tamanho_cano_definido == False:
                        self.__lista_objetos.append(self.__cano_2)    
                    elif self.__cano_3.tamanho_cano_definido == False:
                        self.__lista_objetos.append(self.__cano_3)

                if objeto.x < const.posicao_destruir:
                    self.__lista_objetos.remove(objeto)
            

    def instancia_canos(self):
        self.__cano_1 = Cano(self.__cenario.tela)
        self.__cano_2 = Cano(self.__cenario.tela)
        self.__cano_3 = Cano(self.__cenario.tela)

    def instancia_itens(self):
        self.__item_1 = ItemTamanho(self.__cenario, self.__personagem)
        self.__item_2 = ItemInvencibilidade(self.__cenario, self.__personagem)
        


    