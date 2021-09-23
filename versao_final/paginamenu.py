from pagina import Pagina
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from controlador import Controlador
from constantes import Constante
from abc import ABC, abstractmethod
import pygame, sys

class PaginaMenu(Pagina):
    def __init__(self):
        super().__init__()
        self.estado = 'Main Menu'

    def desenha_botao(self, y, estado):
        if self.cria_botao(240,y).collidepoint(pygame.mouse.get_pos()):
            if self.click:
                self.estado = estado
                self.rodando = False

    def menu(self):

        pygame.init()
        self.rodando = True
        while self.rodando:

            self.cenario.inicializa_tela()
            self.desenha_texto('main menu', 20, 60, 20)

            self.desenha_botao(250, 'Jogo')
            self.desenha_botao(350, 'Highscore')
            self.desenha_botao(450, 'Como Jogar')

            self.resetaclick()
            self.eventos_menu()
            self.atualiza_tela()
