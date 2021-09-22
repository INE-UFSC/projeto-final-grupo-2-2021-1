from menu import Menu
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from controlador import Controlador
from constantes import Constante
from abc import ABC, abstractmethod
import pygame, sys

class MenuHighscore(Menu):
    def __init__(self):
        super().__init__()
        self.estado = 'Highscore'

    def desenha_botao(self):
        acao = False
        if self.cria_botao(20,575,100,50).collidepoint(pygame.mouse.get_pos()):
            if self.click:
                acao = True
        return acao

    def menu(self):
        
        pygame.init()
        while True:
            self.cenario.inicializa_tela()
            self.desenha_texto(self.estado, 20, 60, 20)

            if self.desenha_botao():
                self.estado = 'Main Menu'
                break
            
            self.resetaclick()
            self.eventos_menu()
            self.atualizatela()
