from pygame import event
from menu import Menu
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from controlador import Controlador
from constantes import Constante
from melhorpontuacao import MelhorPontuacao
from abc import ABC, abstractmethod
import pygame, sys

class MenuGameOver(Menu):
    def __init__(self, pontuacao: int):
        super().__init__()
        self.__fonte = pygame.font.SysFont('Comic Sans MS', 20)
        self.pontuacao = pontuacao
        self.estado = 'Game over'
        self.userinput = ''
        self.checaponto = MelhorPontuacao()
        self.salvo = False
        self.rank = None

    def eventos_menu(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit
                if event.type == pygame.KEYDOWN:
                    if len(self.userinput) < 3:
                        if event.key == pygame.K_BACKSPACE:
                            self.userinput = self.userinput[0:-1]
                        else:
                            self.userinput += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    def desenha_botao(self):
        if self.cria_botao(20,575,100,50).collidepoint(pygame.mouse.get_pos()):
            if self.click:
                self.estado = 'Main Menu'
                self.rodando = False

    def inserinome(self):
        textbox = pygame.Rect(200, 200, 140, 32)
        cor = pygame.Color('lightskyblue3')
        pygame.draw.rect(self.cenario.tela, cor, textbox, 2)
        textrender = self.__fonte.render(self.userinput, True, (0, 0, 255))
        self.cenario.tela.blit(textrender, (203, 200))

    def checapontos(self):
        if not self.salvo:
            if self.checaponto.checapontuacao(self.pontuacao):
                self.inserinome()
                if len(self.userinput) >= 3:
                    self.checaponto.novapontuacao(self.pontuacao, self.userinput)
                    self.salvo = True
            else:
                self.desenha_botao()
        else:
            self.desenha_botao()

    def atualizarank(self):
        self.rank = self.checaponto.score

    def menu(self):
        
        pygame.init()
        self.rodando = True
        while self.rodando:
            self.cenario.inicializa_tela()
            self.desenha_texto('game over', 20, 60, 20)
            self.checapontos()
            self.atualizarank()
            self.resetaclick()
            self.eventos_menu()
            self.atualizatela()
