from pygame import event
from pagina import Pagina
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from botaogenerico import BotaoVoltar, CaixaTexto
from melhorpontuacao import MelhorPontuacao
import pygame, sys

class PaginaFimDeJogo(Pagina):
    def __init__(self, pontuacao: int):
        super().__init__()
        self.__fonte_entrada_texto = pygame.font.SysFont('Comic Sans MS', 30)
        self.__caixa_texto = CaixaTexto()
        self.botoes.append(BotaoVoltar())
        self.botoes.append(self.__caixa_texto)
        self.pontuacao = pontuacao
        self.estado = 'MenuPrincipal'
        self.__texto_ativo = False
        self.texto_usuario = ''
        self.checar_ponto = MelhorPontuacao()
        self.salvo = False
        self.rank = None

    def desenha_botao(self, y):
        for botao in self.botoes:
            if isinstance(botao, BotaoVoltar):
                botao.atualizar(100, 610)
                botao.desenhar(self.cenario.tela)
            else:
                botao.atualizar(self.const.tela_jogo_largura/2, y)
                botao.desenhar(self.cenario.tela)
                y += 100

    def detecta_colisao(self):
        for botao in self.botoes:
            if botao.gera_retangulo().collidepoint(pygame.mouse.get_pos()) and self.click:
                if isinstance(botao, CaixaTexto):
                    self.__texto_ativo = botao.efeito_colisao()
                else:
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
                if event.type == pygame.KEYDOWN and self.__texto_ativo:
                    if event.key == pygame.K_BACKSPACE:
                        self.texto_usuario = self.texto_usuario[0:-1]
                    elif len(self.texto_usuario) < 3:
                        self.texto_usuario += event.unicode
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    def inserir_nome(self):
        texto_usuario = self.__fonte_entrada_texto.render(self.texto_usuario.upper(), True, (255, 255, 255))
        self.cenario.tela.blit(texto_usuario, ((self.const.tela_jogo_largura/2)-20,240))

    def checapontos(self):
        if not self.salvo:
            if self.checar_ponto.checapontuacao(self.pontuacao):
                self.inserir_nome()
                if len(self.texto_usuario) >= 3:
                    self.checar_ponto.novapontuacao(self.pontuacao, self.texto_usuario)
                    self.salvo = True
            else:
                self.desenha_botao(250)
        else:
            self.desenha_botao(250)

    def atualizarank(self):
        self.rank = self.checar_ponto.score

    def menu(self):
        
        pygame.init()
        self.rodando = True
        while self.rodando:
            self.cenario.inicializa_tela()
            self.desenha_texto("Fim de Jogo", 40)

            self.desenha_botao(250)
            self.detecta_colisao()
            self.inserir_nome()

            self.resetaclick()
            self.eventos_menu()
            self.atualiza_tela()
           
            #self.checapontos()
            #self.atualizarank()

