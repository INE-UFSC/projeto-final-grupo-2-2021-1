import pygame, sys
from paginamenu import PaginaMenu
from paginapontuacao import PaginaPontuacao
from paginacomojogar import PaginaComoJogar
from paginafimdejogo import PaginaFimDeJogo
from cenario import Cenario
from controlador import Controlador


class ContraladorPagina:
    def __init__(self):
        self.__controlador_jogo = Controlador()
        self.__pagina_menu = PaginaMenu()
        self.__pagina_pontuacao = PaginaPontuacao()
        self.__pagina_como_jogar = PaginaComoJogar()
        self.__pagina_fim_de_jogo = PaginaFimDeJogo(1)

        self.menuname = None

    def verifica_menu(self):
        if self.menuname == 'Main Menu':
            self.menu_principal()
        elif self.menuname == 'Jogo':
            self.jogar()
        elif self.menuname == 'Highscore':
            self.ranque_pontuacao()
        elif self.menuname == 'Como Jogar':
            self.como_jogar()
        elif self.menuname == 'Game over':
            self.fim_jogo()

    def menu_principal(self):
        self.__pagina_menu = PaginaMenu()
        self.__pagina_menu.menu()
        self.menuname = self.__pagina_menu.estado
        self.verifica_menu()

    def jogar(self):
        self.__controlador_jogo = Controlador()
        self.__controlador_jogo.iniciar()
        self.menuname = self.__controlador_jogo.estado
        self.verifica_menu()

    def ranque_pontuacao(self):
        self.__pagina_pontuacao = PaginaPontuacao()
        self.__pagina_pontuacao.menu()
        self.menuname = self.__pagina_pontuacao.estado
        self.verifica_menu()

    def como_jogar(self):
        self.__pagina_como_jogar = PaginaComoJogar()
        self.__pagina_como_jogar.menu()
        self.menuname = self.__pagina_como_jogar.estado
        self.verifica_menu()

    def fim_jogo(self):
        self.__pagina_fim_de_jogo = PaginaFimDeJogo(1)
        self.__pagina_fim_de_jogo.menu()
        self.menuname = self.__pagina_fim_de_jogo.estado
        self.verifica_menu()
