from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from controlador import Controlador
from constantes import Constante
import pygame, sys


class Menu:
    def __init__(self, jogo:Controlador):
        self.const = Constante()
        self.jogo = jogo
        self.__fonte = pygame.font.get_default_font()
        self.click = False

    def desenha_texto(self, texto, tamanho, x, y):
        fonte = pygame.font.Font(self.__fonte, tamanho)
        superficie = fonte.render(texto, True, (255,255,255))
        texto_rect = superficie.get_rect()
        texto_rect.center = (x,y)
        self.jogo.cenario.tela.blit(superficie, texto_rect)
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

    def resetaclick(self):
        self.click = False
    
    def desenhabotao(self, x, y, tamanhox, tamanhoy, cor):
        botao = pygame.Rect(x, y, tamanhox, tamanhoy)
        pygame.draw.rect(self.jogo.cenario.tela, cor, botao)
        return botao

    def menu(self):          
        pygame.init()
        while True:

            self.jogo.cenario.inicializa_tela()
            self.desenha_texto('main menu', 20, 60, 20)

            botao1 = self.desenhabotao(240,250,300,75, (255,0,0))
            botao2 = self.desenhabotao(240,350,300,75, (0,255,0))
            botao3 = self.desenhabotao(240,450,300,75, (255,255,0))

            if botao1.collidepoint((pygame.mouse.get_pos())):
                if self.click:
                    self.jogo.iniciar()
            if botao2.collidepoint((pygame.mouse.get_pos())):
                if self.click:
                    self.highscore()
            if botao3.collidepoint((pygame.mouse.get_pos())):
                if self.click:
                    self.como_jogar()

            self.resetaclick()
            self.eventos_menu()
            self.atualizatela()

    def highscore(self):

        while True:
            self.jogo.cenario.inicializa_tela()
            self.desenha_texto('Highscore', 20, 60, 20)

            botao4 = self.desenhabotao(20,575,100,50, (255,255,0))

            if botao4.collidepoint((pygame.mouse.get_pos())):
                if self.click:
                    break
            
            self.resetaclick()
            self.eventos_menu()
            self.atualizatela()

    def como_jogar(self):

        while True:
            self.jogo.cenario.inicializa_tela()
            self.desenha_texto('Como jogar', 20, 60, 20)

            botao4 = self.desenhabotao(20,575,100,50, (255,255,0))

            if botao4.collidepoint((pygame.mouse.get_pos())):
                if self.click:
                    break
            
            self.resetaclick()
            self.eventos_menu()
            self.atualizatela()

    def gameover(self):

        while True:
            self.jogo.cenario.inicializa_tela()
            self.desenha_texto('Game over', 20, 60, 20)

            botao5 = pygame.Rect(20,575,100,50)
            pygame.draw.rect(self.jogo.cenario.tela, (255,0,0), botao5)

            if botao5.collidepoint((pygame.mouse.get_pos())):
                if self.click:
                    break
            
            self.resetaclick()
            self.eventos_menu()
            self.atualizatela()
