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
        self.click = False
        self.estado = ""

    @property
    def botoes(self):
        return self.__botoes
    
    @botoes.setter
    def botoes(self, botao):
        self.__botoes = botao

    def desenha_texto(self, texto, tamanho):
        fonte = pygame.font.Font(self.__fonte, tamanho)
        superficie = fonte.render(texto, True, (25,25,200))
        texto_rect = superficie.get_rect()
        texto_rect.center = (self.const.tela_jogo_largura/2, int(self.const.tela_jogo_altura/10))
        self.cenario.tela.blit(superficie, texto_rect)
        self.mainclock = pygame.time.Clock()

    def eventos_menu(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit
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

    @abstractmethod
    def desenha_botao(self):
        pass
    
    @abstractmethod
    def menu(self):          
        pass
