from pagina import Pagina
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from botaogenerico import BotaoJogar, BotaoComoJogar, BotaoPontuacao
import pygame, sys

class PaginaMenu(Pagina):
    def __init__(self):
        super().__init__()
        self.botoes = []
        self.botoes.append(BotaoJogar())
        self.botoes.append(BotaoComoJogar())
        self.botoes.append(BotaoPontuacao())
        self.estado = 'MenuPrincipal'

    def desenha_botao(self, y):
        for botao in self.botoes:
            botao.atualizar(self.const.tela_jogo_largura/2,y)
            botao.desenhar(self.cenario.tela)
            y += 100

    def menu(self):

        pygame.init()
        self.rodando = True
        while self.rodando:

            self.cenario.inicializa_tela()
            self.desenha_texto("Menu Principal",40)

            self.desenha_botao(250)
            self.detecta_colisao()

            self.resetaclick()
            self.eventos_menu()
            self.atualiza_tela()
