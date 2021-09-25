from abc import ABC, abstractmethod
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from controlador import Controlador
from constantes import Constante
from cenariomenu import CenarioMenu
import pygame, sys

class Pagina(ABC):
    def __init__(self):
        self.const = Constante()
        self.cenario = CenarioMenu()
        self.__fonte = pygame.font.get_default_font()
        self.__botoes = []
        self.__rodando = True
        self.click = False
        self.estado = ""

    @property
    def botoes(self):
        return self.__botoes
    
    @botoes.setter
    def botoes(self, botao):
        self.__botoes = botao

    @property
    def rodando(self):
        return self.__rodando
    
    @rodando.setter
    def rodando(self, rodando):
        self.__rodando = rodando

    def desenha_texto(self, texto, tamanho):
        fonte = pygame.font.Font(self.__fonte, tamanho)
        superficie = fonte.render(texto, True, (0,128,128))
        texto_rect = superficie.get_rect()
        texto_rect.center = (self.const.tela_jogo_largura/2, int(self.const.tela_jogo_altura/10))
        self.cenario.tela.blit(superficie, texto_rect)
        self.mainclock = pygame.time.Clock()

    def eventos_menu(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.estado = "PaginaFechar"
                self.rodando = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:                    
                    self.estado = "PaginaFechar"
                    self.rodando = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    def atualiza_tela(self):
            pygame.display.update()
            self.mainclock.tick(self.const.fps)

    def checa_gameover(self, jogo: Controlador):
        if jogo.personagem.game_over == True:
            if jogo.personagem.voando == False:
                self.gameover()

    def resetaclick(self):
        self.click = False
    
    def cria_botao(self, x, y):
        botao = pygame.Rect(x, y, self.const.botao_maior_x, self.const.botao_maior_y)
        pygame.draw.rect(self.cenario.tela, (255,0,0), botao)
        return botao

    def detecta_colisao(self):
        for botao in self.botoes:
            if botao.gera_retangulo().collidepoint(pygame.mouse.get_pos()) and self.click:
                self.estado = botao.efeito_colisao()
                self.rodando = False

    def toca_som(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('versao_final/sons/menu/som_menu.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.03)

    @abstractmethod
    def desenha_botao(self):
        pass
    
    @abstractmethod
    def menu(self):          
        pass
