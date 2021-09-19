from item import Item
import random
import pygame
from pygame.locals import *
from personagem import Personagem
from cano import Cano
from cenario import Cenario
from geradorItem import GeradorItem, GeradorItemInvencibilidade, GeradorItemTamanho
from contador import Contador
from constantes import Constante
from pontuacao import Pontuacao
from colisão import Colisao


class Controlador:
    def __init__(self) -> None:
        self.const = Constante()
        self.__personagem = Personagem(self.const.posicao_personagem_x, self.const.posicao_personagem_y)
        self.__cenario = Cenario()
        self.__contador = Contador()
        self.__lista_objetos = []
        self.__itens_ativos = []
        self.__pontuacao = Pontuacao()
        self.__colisao = Colisao()

    @property
    def cenario(self):
        return self.__cenario

    @property
    def personagem(self):
        return self.__personagem

    def iniciar(self):

        pygame.init()
        clock = pygame.time.Clock()

        self.rodando = True
        while self.rodando:

            clock.tick(self.const.fps)
            self.__cenario.inicializa_tela()
            self.__contador.contador_tempo()
            self.gera_objetos()
            self.detecta_colisao()
            self.itens_ativos()
            self.atualiza_personagem()
            self.pontuacao()

            self.le_eventos()
            pygame.display.update()
        
        pygame.quit()


    def atualiza_personagem(self):
        self.__personagem.desenha_personagem(self.__cenario.tela)
        self.__personagem.mover()
        self.__personagem.morreu()

    def gera_objetos(self):

        self.controla_objetos()

        for objeto in self.__lista_objetos:
            objeto.atualiza(self.__cenario.tela)
            if self.__personagem.voando and not self.__personagem.game_over:
                objeto.move()

    def controla_objetos(self): #Controla os canos da lista de objetos que são gerados
        if not self.__lista_objetos:
            self.__lista_objetos.append(Cano())

        for objeto in self.__lista_objetos:
            if objeto.x == self.const.posicao_gera_cano:
                if isinstance(objeto, Cano):
                    self.__lista_objetos.append(Cano())
                    self.instancia_itens()

            if objeto.x <= self.const.posicao_destruir:
                self.__lista_objetos.remove(objeto)
                del objeto

    def instancia_itens(self): #FACTORY
        geradores_de_itens = GeradorItem.__subclasses__()
        gerador_selecionado = random.choice(geradores_de_itens)
        item = gerador_selecionado().criador_item()

        if random.randint(1,2) == 1:
            self.__lista_objetos.append(item)


    def itens_ativos(self):

        for item in self.__lista_objetos:
            if item.colidiu and isinstance(item, Item):
                for item_ativo in self.__itens_ativos:
                    if type(item_ativo) is type(item):
                        self.__itens_ativos.remove(item_ativo)
                        del item_ativo
                self.__itens_ativos.append(item)
                self.__lista_objetos.remove(item)
        
        if len(self.__itens_ativos) != 0:
            for item in self.__itens_ativos:
                item.duracao_item(self.__contador)
                if item.ativo == False:
                    self.__itens_ativos.remove(item)
                    del item

    def detecta_colisao(self):
        for objeto in self.__lista_objetos:
            self.__colisao.detectar_colisão(self.__personagem, objeto)

    def pontuacao(self):

        for cano in self.__lista_objetos:
            if cano.x == self.const.posicao_pontuar:
                if isinstance(cano, Cano):
                    self.__pontuacao.marca_ponto(1)

        self.__cenario.escreve_pontuacao(self.__pontuacao.mostra_ponto())

    def le_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
            if evento.type == pygame.KEYDOWN and not self.__personagem.voando and not self.__personagem.game_over:
                if evento.key == pygame.K_UP:
                    self.__personagem.voando = True
    
