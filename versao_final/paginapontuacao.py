from pagina import Pagina
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from botaogenerico import BotaoVoltar
from spritesestaticos import SpriteQuadroPontuacao
from atualizaplacar import Placar
import pygame, sys

class PaginaPontuacao(Pagina):
    def __init__(self):
        super().__init__()
        self.botoes.append(BotaoVoltar())
        self.estado = "Pontuacao"
        self.__fundo_tabela = pygame.sprite.Group(SpriteQuadroPontuacao())
        self.placar = Placar()
        self.rank_jogadores = self.placar.rank_pontuacao

    def desenha_botao(self, y):
        for botao in self.botoes:
            botao.atualizar(100,y)
            botao.desenhar(self.cenario.tela)
            y += 100

    def desenha_rank(self):
        self.__fundo_tabela.update(self.const.tela_jogo_largura/2, self.const.tela_jogo_altura/2)
        self.__fundo_tabela.draw(self.cenario.tela)
        fonte = pygame.font.SysFont('Comic Sans MS', 30)
        indice = 1
        y = 200

        for jogador, pontos in self.rank_jogadores[::-1]:
            linha = str(indice) + " - " + jogador + ": " + str(pontos)
            texto_fonte = fonte.render(linha, True, (45, 255, 155))
            self.cenario.tela.blit(texto_fonte, ((self.const.tela_jogo_largura/2)-50,y))
            indice += 1
            y += 30

    def menu(self):
        
        pygame.init()
        self.rodando = True
        while self.rodando:
            self.cenario.inicializa_tela()
            self.desenha_texto("Tabela de Líderes",40)

            self.desenha_botao(610)
            self.desenha_rank()
            self.detecta_colisao()
            
            self.resetaclick()
            self.eventos_menu()
            self.atualiza_tela()

