from pagina import Pagina
import pygame

class paginaMenu(Pagina):
    def __init__(self):
        super().__init__()

    def botao(self, x, y):

        botao = pygame.Rect(x, y, 300, 75)  
        return  botao

    def instancia_botao(self):
        
        self.botoes.append(self.botao(240, 250))
        self.botoes.append(self.botao(240, 350))
        self.botoes.append(self.botao(240, 450))
   
    def desenha_botao(self, fundo_tela):
        
        for botao in self.botoes:
            pygame.draw.rect(fundo_tela, (255,0,0), botao)

    def mostra_pagina(self):          
        pygame.init()
        while True:

            self.cenario.inicializa_tela()
            self.desenha_texto('main menu', 20, 60, 20)

            if self.botao(240,250,300,75):
                self.iniciar()
            if self.botao(240,350,300,75):
                self.highscore()
            if self.botao(240,450,300,75):
                self.como_jogar()

            self.resetaclick()
            self.eventos_menu()
            self.atualizatela()
