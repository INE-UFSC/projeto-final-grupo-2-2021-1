from pygame import event
from pagina import Pagina
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from botaogenerico import BotaoVoltar, BotaoSalvar, CaixaTexto
import pygame, sys

class PaginaFimDeJogo(Pagina):
    def __init__(self, pontuacao):
        super().__init__()
        self.__pontuacao_personagem = pontuacao
        self.__caixa_texto = CaixaTexto()
        self.__instancia_botoes()
        self.estado = 'FimDeJogo'
        self.mensagem_interface = ''
        self.__texto_ativo = False
        self.nome_usuario = ''
    
    @property
    def pontuacao_personagem(self):
        return self.__pontuacao_personagem
    
    @pontuacao_personagem.setter
    def pontuacao_personagem(self, pontuacao_personagem):
        self.__pontuacao_personagem = pontuacao_personagem

    def __instancia_botoes(self):
        self.botoes.append(BotaoVoltar())
        self.botoes.append(self.__caixa_texto)
        self.botoes.append(BotaoSalvar())

    def desenha_botao(self, y):
        for botao in self.botoes:
            if isinstance(botao, BotaoVoltar):
                botao.atualizar(100, 610)
                botao.desenhar(self.cenario.tela)
            else:
                botao.atualizar(self.const.tela_jogo_largura/2, y)
                botao.desenhar(self.cenario.tela)
                y += 70

    def detecta_colisao(self):
        for botao in self.botoes:
            if botao.gera_retangulo().collidepoint(pygame.mouse.get_pos()) and self.click:
                if isinstance(botao, CaixaTexto):
                    self.__texto_ativo = botao.efeito_colisao()
                elif isinstance(botao, BotaoSalvar):
                    self.__texto_ativo = True
                    self.mensagem_interface = botao.efeito_colisao(self.__pontuacao_personagem, self.nome_usuario)
                    if botao.salvo:
                        self.estado = self.mensagem_interface
                        self.rodando = False
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
                        self.nome_usuario = self.nome_usuario[0:-1]
                    elif len(self.nome_usuario) < 3:
                        self.nome_usuario += event.unicode
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    def inserir_nome(self):

        fonte = pygame.font.SysFont('Comic Sans MS', 30)
        texto_fonte = fonte.render(str(self.nome_usuario).upper(), True, (255, 255, 255))
        self.cenario.tela.blit(texto_fonte, ((self.const.tela_jogo_largura/2)-20,240))

    def inserir_pontuacao(self):

        fonte = pygame.font.SysFont('Comic Sans MS', 50)
        texto_fonte = fonte.render(str(self.__pontuacao_personagem).upper(), True, (70, 60, 255))
        self.cenario.tela.blit(texto_fonte,((self.const.tela_jogo_largura/2)-20,150))

    def inserir_mensagem(self):

        fonte = pygame.font.SysFont('Comic Sans MS', 30)
        texto_fonte = fonte.render(str(self.mensagem_interface).upper(), True, (70, 60, 255))
        self.cenario.tela.blit(texto_fonte, ((self.const.tela_jogo_largura/5)-20,400))

    def menu(self):
        
        pygame.init()
        self.rodando = True
        while self.rodando:
            self.cenario.inicializa_tela()
            self.desenha_texto("Fim de Jogo", 40)
            self.desenha_botao(250)
            self.inserir_nome()
            self.inserir_pontuacao()
            self.inserir_mensagem()

            self.detecta_colisao()

            self.resetaclick()
            self.eventos_menu()
            self.atualiza_tela()
