# Controlador ainda não está operando corretamente
# Necessário arrumar ainda: 
# 1. Colisão do personagem com os canos
# 2. Geração dos itens (ainda não foi implementada a lógica para desenhá-los na tela)
# 3. Geração dos canos (no momento gera somente o conjunto dos 3 primeiros canos)
# 4. Lógica para contabilizar a pontuação


import random
import pygame
from pygame.locals import *
from personagem import Personagem
from cano import Cano
from cenario import Cenario
from itemInvencibilidade import ItemInvencibilidade
from itemTamanho import ItemTamanho
from contador import Contador
from constantes import Constante as const
from pontuacao import Pontuacao

class Controlador:
    def __init__(self) -> None:
        self.__personagem = Personagem(const.posicao_personagem_x, const.posicao_personagem_y)
        self.__cenario = Cenario()
        self.__contador = Contador()
        self.__lista_objetos = []
        self.__pontuacao = Pontuacao()

    @property
    def cenario(self):
        return self.__cenario

    def iniciar(self):

        pygame.init()
        clock = pygame.time.Clock()

        self.rodando = True
        while self.rodando:

            clock.tick(const.fps)
            self.__cenario.inicializa_tela()
            self.__contador.contador_tempo()
            self.gera_objetos()
            self.__personagem.desenha_personagem(self.__cenario.tela)
            self.__personagem.mover()

            self.le_eventos()
            pygame.display.update()
        
        pygame.quit()


    def gera_objetos(self):

        self.controla_canos()

        for objeto in self.__lista_objetos:
            objeto.atualiza()
            if self.__personagem.voando and not self.__personagem.game_over:
                objeto.move()

    def controla_canos(self): #Controla os canos da lista de objetos que são gerados
        if not self.__lista_objetos:
            self.__lista_objetos.append(Cano(self.__cenario.tela))

        for objeto in self.__lista_objetos:
            if objeto.x == const.posicao_gera_cano:
                if isinstance(objeto, Cano):
                    self.__lista_objetos.append(Cano(self.__cenario.tela))
                    self.instancia_itens()

            if objeto.x <= const.posicao_destruir:
                self.__lista_objetos.remove(objeto)
                del objeto
             
    def instancia_itens(self):
        self.__item_1 = ItemTamanho(self.__cenario.tela, self.__personagem)
        self.__item_2 = ItemInvencibilidade(self.__cenario.tela, self.__personagem)

        lista_itens = [self.__item_1, self.__item_2]
        item = random.choice(lista_itens)

        if random.randint(1,2) == 1:
            self.__lista_objetos.append(item)

    def le_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
            if evento.type == pygame.KEYDOWN and not self.__personagem.voando and not self.__personagem.game_over:
                if evento.key == pygame.K_UP:
                    self.__personagem.voando = True
    
