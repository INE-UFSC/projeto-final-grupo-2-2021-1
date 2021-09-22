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
       self.lastscore = None
       self.main = MainMenu()
       self.jogo = Controlador()
       self.menuhighscore = MenuHighscore()
       self.menucomojogar = MenuComoJogar()
       self.menugameover = MenuGameOver(self.lastscore)

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
        self.main.menu()
        self.menuname = self.main.estado
        self.checamenu()

    def game(self):
        self.jogo = Controlador()
        self.jogo.iniciar()
        self.lastscore = int(self.jogo.pontos.pontos)
        self.menuname = self.jogo.estado
        self.checamenu()

    def highscore(self):
        self.menuhighscore = MenuHighscore()
        self.menuhighscore.menu()
        self.menuname = self.menuhighscore.estado
        self.checamenu()

    def comojogar(self):
        self.menucomojogar.menu()
        self.menuname = self.menucomojogar.estado
        self.checamenu()

    def gameover(self):
        self.menugameover = MenuGameOver(self.lastscore)
        self.menugameover.menu()
        self.menuname = self.menugameover.estado
        self.rank = self.menugameover.checaponto.score
        self.checamenu()
