from pagina import Pagina
from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, QUIT
from botaogenerico import BotaoVoltar
from spritesestaticos import SpriteTeclaUp
from animacao import PersonagemAnimacao, ItemPequenoAnimacao, ItemInvencivelAnimacao
import pygame, sys

class PaginaComoJogar(Pagina):
    def __init__(self):
        super().__init__()
        self.botoes.append(BotaoVoltar())
        self.estado = "ComoJogar"
        self.__texto_base = []
        self.__texto_objetos = []
        self.__texto_como_jogar()
        self.__sprites_jogo = []
        self.__sprites_jogo.append(pygame.sprite.Group(PersonagemAnimacao()))
        self.__sprites_jogo.append(pygame.sprite.Group(SpriteTeclaUp()))
        self.__sprites_jogo.append(pygame.sprite.Group(ItemPequenoAnimacao()))
        self.__sprites_jogo.append(pygame.sprite.Group(ItemInvencivelAnimacao()))
        

    def desenha_botao(self, y):
        for botao in self.botoes:
            botao.atualizar(100,y)
            botao.desenhar(self.cenario.tela)
            y += 100

    def desenha_sprites(self):
        y = 260
        for sprite in self.__sprites_jogo:
            sprite.update(100, y)
            sprite.draw(self.cenario.tela)
            y += 80

    def desenha_lista_texto(self):
        fonte = pygame.font.SysFont('Comic Sans MS', 30)
        y = 100
        for texto in self.__texto_base:
            texto_fonte = fonte.render(texto, True, (0, 100, 0))
            self.cenario.tela.blit(texto_fonte,(80, y))
            y += 40
        
        fonte = pygame.font.SysFont('Comic Sans MS', 25)
        y=260
        for texto in self.__texto_objetos:
            
            texto_fonte = fonte.render(texto, True, (0, 100, 0))
            self.cenario.tela.blit(texto_fonte,(160, y))
            y += 80

    def __texto_como_jogar(self):
        texto_1 = "Neste jogo seu objetivo é fazer o maior número de pontos possíveis."
        texto_2 = "Desviando dos canos e pegando os itens pelo cenario."
        texto_3 = "Esse é seu personagem!"
        texto_4 = "Você controle ele pela tecla Key_Up."
        texto_5 = "Esse é o item que diminui o tamanho do seu personagem."
        texto_6 = "Esse é o item que deixa seu personagem invencível."

        self.__texto_base = [texto_1, texto_2]
        self.__texto_objetos = [texto_3, texto_4, texto_5, texto_6]

    def menu(self):
        
        pygame.init()
        self.rodando = True
        while self.rodando:
            self.cenario.inicializa_tela()
            self.desenha_texto("Como Jogar",40)

            self.desenha_botao(610)
            self.desenha_sprites()
            self.desenha_lista_texto()
            self.detecta_colisao()
            
            self.resetaclick()
            self.atualiza_tela()
            self.eventos_menu()
            
