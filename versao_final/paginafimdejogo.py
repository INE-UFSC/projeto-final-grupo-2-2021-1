from pygame import event
from pagina import Pagina
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from botaogenerico import BotaoVoltar
from melhorpontuacao import MelhorPontuacao
import pygame, sys

class PaginaFimDeJogo(Pagina):
    def __init__(self, pontuacao: int):
        super().__init__()
        self.__fonte = pygame.font.SysFont('Comic Sans MS', 20)
        self.botoes.append(BotaoVoltar())
        self.pontuacao = pontuacao
        self.estado = 'MenuPrincipal'
        self.userinput = ''
        self.checar_ponto = MelhorPontuacao()
        self.salvo = False
        self.rank = None

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

    def inserir_nome(self):
        caixa_de_texto = pygame.Rect(200, 200, 140, 32)
        cor = pygame.Color('lightskyblue3')
        pygame.draw.rect(self.cenario.tela, cor, caixa_de_texto, 2)
        textrender = self.__fonte.render(self.userinput, True, (0, 0, 255))
        self.cenario.tela.blit(textrender, (203, 200))

    def checapontos(self):
        if not self.salvo:
            if self.checar_ponto.checapontuacao(self.pontuacao):
                self.inserir_nome()
                if len(self.userinput) >= 3:
                    self.checar_ponto.novapontuacao(self.pontuacao, self.userinput)
                    self.salvo = True
            else:
                self.desenha_botao(610)
        else:
            self.desenha_botao(610)

    def atualizarank(self):
        self.rank = self.checar_ponto.score

    def menu(self):
        
        pygame.init()
        self.rodando = True
        while self.rodando:
            self.cenario.inicializa_tela()
            self.desenha_texto("Fim de Jogo",40)
            self.checapontos()
            self.atualizarank()

            self.resetaclick()
            self.eventos_menu()
            self.atualiza_tela()

            self.desenha_botao(610)
            self.detecta_colisao()
