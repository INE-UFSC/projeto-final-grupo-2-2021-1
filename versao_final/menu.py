from abc import ABC, abstractmethod
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from controlador import Controlador
from constantes import Constante
from cenario import Cenario
import pygame, sys


class Menu(ABC):
    def __init__(self):
        self.const = Constante()
        self.cenario = Cenario()
        self.__fonte = pygame.font.get_default_font()
        self.click = False

    def desenha_texto(self, texto, tamanho, x, y):
        fonte = pygame.font.Font(self.__fonte, tamanho)
        superficie = fonte.render(texto, True, (255,255,255))
        texto_rect = superficie.get_rect()
        texto_rect.center = (x,y)
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

    def atualizatela(self):
            pygame.display.update()
            self.mainclock.tick(self.const.fps)

    def checa_gameover(self, jogo: Controlador):
        if jogo.personagem.game_over == True:
            if jogo.personagem.voando == False:
                self.gameover()

    def resetaclick(self):
        self.click = False
    
    def cria_botao(self, x, y, tamanhox, tamanhoy):
        botao = pygame.Rect(x, y, tamanhox, tamanhoy)
        pygame.draw.rect(self.cenario.tela, (255,0,0), botao)
        return botao

    @abstractmethod
    def desenha_botao(self, x, y, tamanhox, tamanhoy, estado):
        pass
    
    @abstractmethod
    def menu(self):          
        pass
