from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from controlador import Controlador
from constantes import Constante
from cenario import Cenario
import pygame, sys


class Menu:
    def __init__(self):
        self.const = Constante()
        self.cenario = Cenario()
        self.__fonte = pygame.font.get_default_font()
        self.click = False

    def desenha_texto(self, texto, tamanho, x, y):
        fonte = pygame.font.Font(self.__fonte, tamanho)
        superficie = fonte.render(texto, True, (255,255,255))
        texto_rect = superficie.get_rect()
        texto_rect.center = (x,y)
        self.cenario.tela.blit(superficie, texto_rect)
        self.mainclock = pygame.time.Clock()

    def eventos_menu(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

    def atualizatela(self):
            pygame.display.update()
            self.mainclock.tick(self.const.fps)

    def checa_gameover(self, jogo: Controlador):
        if jogo.personagem.game_over == True:
            if jogo.personagem.voando == False:
                self.gameover()

    def resetaclick(self):
        self.click = False
    
    def botao(self, x, y, tamanhox, tamanhoy):
        acao = False
        botao = pygame.Rect(x, y, tamanhox, tamanhoy)
        pygame.draw.rect(self.cenario.tela, (255,0,0), botao)
        
        if botao.collidepoint(pygame.mouse.get_pos()):
            if self.click:
                acao = True
        return acao

    def iniciar(self):
        self.jogo = Controlador()

        pygame.init()
        clock = pygame.time.Clock()

        self.rodando = True
        while self.rodando:

            clock.tick(self.const.fps)
            self.jogo.cenario.inicializa_tela()
            self.jogo.contador.contador_tempo()
            self.jogo.gera_objetos()
            self.jogo.detecta_colisao()
            self.jogo.itens_ativos()
            self.jogo.atualiza_personagem()
            self.jogo.pontuacao()
            self.checa_gameover(self.jogo)

            self.jogo.le_eventos()
            pygame.display.update()
    
    def menu(self):          
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

    def highscore(self):

        while True:
            self.cenario.inicializa_tela()
            self.desenha_texto('Highscore', 20, 60, 20)

            if self.botao(20,575,100,50):
                break
            
            self.resetaclick()
            self.eventos_menu()
            self.atualizatela()

    def como_jogar(self):

        while True:
            self.cenario.inicializa_tela()
            self.desenha_texto('Como jogar', 20, 60, 20)

            if self.botao(20,575,100,50):
                break
            
            self.resetaclick()
            self.eventos_menu()
            self.atualizatela()

    def gameover(self):

        while True:
            self.cenario.inicializa_tela()
            self.desenha_texto('Game over', 20, 60, 20)

            if self.botao(20,575,100,50):
                self.menu()
            
            self.resetaclick()
            self.eventos_menu()
            self.atualizatela()
