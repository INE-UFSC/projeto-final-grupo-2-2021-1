from pagina import Pagina
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from botaogenerico import BotaoVoltar
import pygame, sys

class PaginaPontuacao(Pagina):
    def __init__(self):
        super().__init__()
        self.botoes.append(BotaoVoltar())
        self.estado = "Pontuacao"

    def desenha_botao(self, y):
        for botao in self.botoes:
            botao.atualizar(100,y)
            botao.desenhar(self.cenario.tela)
            y += 100
    
    def detecta_colisao(self):
        for botao in self.botoes:
            if botao.gera_retangulo().collidepoint(pygame.mouse.get_pos()) and self.click:
                self.estado = botao.efeito_colisao()
                self.rodando = False

    def menu(self):
        
        pygame.init()
        self.rodando = True
        while self.rodando:
            self.cenario.inicializa_tela()
            self.desenha_texto("Tabela de Líderes",40)

            self.desenha_botao(610)
            self.detecta_colisao()
            
            self.resetaclick()
            self.eventos_menu()
            self.atualiza_tela()
