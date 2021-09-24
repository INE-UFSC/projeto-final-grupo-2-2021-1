from item import Item
import random
import pygame
from pygame.locals import *
from jogador import Jogador
from canoPadrao import CanoPadrao
from cano import Cano
from cenario import Cenario
from geradorItem import GeradorItem
from contador import Contador
from constantes import Constante
from pontuacao import Pontuacao
from colisao import Colisao


class Controlador:
    def __init__(self) -> None:
        self.const = Constante()
        self.estado = 'Jogo'
        self.__personagem = Jogador()
        self.__cenario = Cenario()
        self.__contador = Contador()
        self.__lista_objetos = []
        self.__itens_ativos = []
        self.__pontuacao = Pontuacao()
        self.__colisao = Colisao()
        self.__fim_de_jogo = None

    @property
    def cenario(self):
        return self.__cenario

    @property
    def personagem(self):
        return self.__personagem
    
    @property
    def contador(self):
        return self.__contador
    
    @property
    def pontuacao(self):
        return self.__pontuacao

    @property
    def fim_de_jogo(self):
        return self.__fim_de_jogo

    def menu(self):

        pygame.init()
        clock = pygame.time.Clock()

        self.tocar_musica_jogo()

        self.rodando = True
        while self.rodando:

            clock.tick(self.const.fps)
            self.__cenario.inicializa_tela()
            self.__contador.contador_tempo()
            self.gera_objetos()
            self.__cenario.atualiza_chao(self.__personagem)
            self.detecta_colisao()
            self.itens_ativos()
            self.atualiza_personagem()
            self.atualiza_pontuacao()
            self.le_eventos()
            self.confere_fim_de_jogo()
            pygame.display.update()

    def tocar_musica_jogo(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('versao_final/sons/menu/som_jogo.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.4)

    def atualiza_personagem(self):
        self.__personagem.desenha_personagem(self.__cenario.tela)
        self.__personagem.mover()
        self.__personagem.morreu(self.__cenario.chao)
        self.__fim_de_jogo = self.__personagem.game_over

    def gera_objetos(self):

        self.controla_objetos()

        for objeto in self.__lista_objetos:
            objeto.atualiza(self.__cenario.tela)
            if self.__personagem.voando and not self.__personagem.game_over:
                objeto.move()

    def controla_objetos(self): #Controla os canos da lista de objetos que são gerados
        if not self.__lista_objetos:
            self.__lista_objetos.append(CanoPadrao())

        for objeto in self.__lista_objetos:
            if objeto.x == self.const.posicao_gera_cano:
                if isinstance(objeto, Cano):
                    self.__lista_objetos.append(CanoPadrao())
                    self.instancia_itens()

            if objeto.x <= self.const.posicao_destruir:
                self.__lista_objetos.remove(objeto)
                del objeto

    def instancia_itens(self): #FACTORY
        geradores_de_itens = GeradorItem.__subclasses__()
        gerador_selecionado = random.choice(geradores_de_itens)
        item = gerador_selecionado().criador_item()

        if random.randint(1,5) == 1:
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
            self.__colisao.detectar_colisao(self.__personagem, objeto)

    def atualiza_pontuacao(self):
        for cano in self.__lista_objetos:
            if cano.x == self.const.posicao_pontuar and isinstance(cano, Cano) \
                and not self.personagem.game_over and self.personagem.voando:
                self.__pontuacao.marca_ponto(1)

        self.__cenario.escreve_pontuacao(self.__pontuacao.mostra_ponto())

    def le_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            if (evento.type == pygame.KEYDOWN 
                    and evento.key == pygame.K_UP
                    and not self.__personagem.voando 
                    and not self.__personagem.game_over):
                self.__personagem.voando = True
    
    def confere_fim_de_jogo(self):
        if self.__personagem.game_over and not self.__personagem.voando:
            self.estado = 'FimDeJogo'
            self.rodando = False
