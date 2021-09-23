from pagina import Pagina
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from controlador import Controlador
from constantes import Constante
from abc import ABC, abstractmethod
import pygame, sys

class PaginaComoJogar(Pagina):
    def __init__(self):
        super().__init__()
        self.estado = 'Como Jogar'

    def desenha_botao(self):
        if self.cria_botao(20,575).collidepoint(pygame.mouse.get_pos()):
            if self.click:
                self.estado = 'Main Menu'
                self.rodando = False

    def menu(self):
        
        pygame.init()
        self.rodando = True
        while self.rodando:
            self.cenario.inicializa_tela()
            self.desenha_texto(self.estado, 20, 60, 20)

            self.desenha_botao()
            
            self.resetaclick()
            self.eventos_menu()
            self.atualiza_tela()
