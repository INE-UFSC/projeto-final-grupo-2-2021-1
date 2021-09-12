from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from controlador import Controlador
from constantes import Constante as const
import pygame, sys

class Menu:
    def __init__(self, jogo:Controlador):
        self.jogo = jogo
        self.__fonte = pygame.font.get_default_font()
        self.click = False

    def desenha_texto(self, texto, tamanho, x, y):
        fonte = pygame.font.Font(self.__fonte, tamanho)
        superficie = fonte.render(texto, True, (255,255,255))
        texto_rect = superficie.get_rect()
        texto_rect.center = (x,y)
        self.jogo.cenario.tela.blit(superficie, texto_rect)

    def menu(self):

        pygame.init()
        while True:
            
            self.jogo.cenario.inicializa_tela
            self.desenha_texto('main menu', 20, 60, 20)
            mainclock = pygame.time.Clock()

            mx, my = pygame.mouse.get_pos()
            botao1 = pygame.Rect(50,100,300,75)
            botao2 = pygame.Rect(50,250,300,75)
            botao3 = pygame.Rect(50,400,300,75)
            pygame.draw.rect(self.jogo.cenario.tela, (255,0,0), botao1)
            pygame.draw.rect(self.jogo.cenario.tela, (0,255,0), botao2)
            pygame.draw.rect(self.jogo.cenario.tela, (0,0,255), botao3)

            if botao1.collidepoint((mx,my)):
                if self.click:
                    self.jogo.iniciar()
            if botao2.collidepoint((mx,my)):
                if self.click:
                    pass
            if botao3.collidepoint((mx,my)):
                if self.click:
                    pass

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

            pygame.display.update()
            mainclock.tick(const.fps)
