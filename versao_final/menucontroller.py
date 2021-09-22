import pygame, sys
from mainmenu import MainMenu
from cenario import Cenario
from menuhighscore import MenuHighscore
from menucomojogar import MenuComoJogar
from menugameover import MenuGameOver
from controlador import Controlador


class MenuController:
    def __init__(self):
       self.menuname = None

    def checamenu(self):
        if self.menuname == 'Main Menu':
            self.main_menu()
        elif self.menuname == 'Jogo':
            self.game()
        elif self.menuname == 'Highscore':
            self.highscore()
        elif self.menuname == 'Como Jogar':
            self.comojogar()
        elif self.menuname == 'Game over':
            self.gameover()

    def main_menu(self):
        menu = MainMenu()
        menu.menu()
        self.menuname = menu.estado
        self.checamenu()

    def game(self):
        jogo = Controlador()
        jogo.iniciar()
        self.menuname = jogo.estado
        self.checamenu()

    def highscore(self):
        menu = MenuHighscore()
        menu.menu()
        self.menuname = menu.estado
        self.checamenu()

    def comojogar(self):
        menu = MenuComoJogar()
        menu.menu()
        self.menuname = menu.estado
        self.checamenu()

    def gameover(self):
        menu = MenuGameOver()
        menu.menu()
        self.menuname = menu.estado
        self.checamenu()
