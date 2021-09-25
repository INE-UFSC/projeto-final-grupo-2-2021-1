from pagina import Pagina
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from botaogenerico import BotaoVoltar
from spritesestaticos import SpriteQuadroPontuacao
from atualizaplacar import Placar
import pygame, sys

class PaginaSair(Pagina):
    def __init__(self):
        super().__init__()

    def desenha_botao(self, y):
        pass

    def menu(self):
        
        pygame.quit()
        sys.exit()
            

