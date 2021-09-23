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

        self.__pagina_atual = None

    def verifica_menu(self):
        if self.__pagina_atual == 'MenuPrincipal':
            self.menu_principal()
        elif self.__pagina_atual == 'Jogo':
            self.jogar()
        elif self.__pagina_atual == 'Pontuacao':
            self.ranque_pontuacao()
        elif self.__pagina_atual == 'ComoJogar':
            self.como_jogar()
        elif self.__pagina_atual == 'FimDeJogo':
            self.fim_jogo()
        else:
            raise KeyError("O botão clicado não foi instanciado Corretamente!")

    def menu_principal(self):
        self.__pagina_menu = PaginaMenu()
        self.__pagina_menu.menu()
        self.__pagina_atual = self.__pagina_menu.estado
        self.verifica_menu()

    def jogar(self):
        self.__controlador_jogo = Controlador()
        self.__controlador_jogo.iniciar()
        self.__pagina_atual = self.__controlador_jogo.estado
        self.verifica_menu()

    def ranque_pontuacao(self):
        self.__pagina_pontuacao = PaginaPontuacao()
        self.__pagina_pontuacao.menu()
        self.__pagina_atual = self.__pagina_pontuacao.estado
        self.verifica_menu()

    def como_jogar(self):
        self.__pagina_como_jogar = PaginaComoJogar()
        self.__pagina_como_jogar.menu()
        self.__pagina_atual = self.__pagina_como_jogar.estado
        self.verifica_menu()

    def fim_jogo(self):
        self.__pagina_fim_de_jogo = PaginaFimDeJogo(1)
        self.__pagina_fim_de_jogo.menu()
        self.__pagina_atual = self.__pagina_fim_de_jogo.estado
        self.verifica_menu()
