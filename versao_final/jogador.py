import pygame
from personagem import Personagem


class Jogador(Personagem):
    def __init__(self):
        super().__init__()
        self.__velocidade = 0 
        self.__voando = False 
        self.__game_over = False
        self.__tamanho = self.const.tamanho_personagem 
        self.__invencivel = False
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def voando(self):
        return self.__voando
    
    @property
    def game_over(self):
        return self.__game_over
    
    @property
    def tamanho(self):
        return self.__tamanho
    
    @property
    def invencivel(self):
        return self.__invencivel
    
    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade
    
    @voando.setter
    def voando(self, voando):
        self.__voando = voando
    
    @game_over.setter
    def game_over(self, game_over):
        self.__game_over = game_over
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho
    
    @invencivel.setter
    def invencivel(self, invencivel):
        self.__invencivel = invencivel

    def mover(self):
         # confere se o personagem está voando para aplicar a gravidade sobre ele
        if self.__voando:
            self.__velocidade += 0.5   # medida que o personagem desce a cada loop
            if self.__velocidade > 8:   # evita que o personagem caia muito rapidamente
                self.__velocidade = 8
            if self.y + self.__tamanho <= self.const.tela_jogo_altura:  # se o personagem não estiver no chão, atualiza sua posição
                self.y += int(self.__velocidade)

        # controle do pulo do personagem
        if not self.__game_over:
            teclas = pygame.key.get_pressed()  # verifica quais teclas foram pressionadas
            if teclas[pygame.K_UP] and not self.tecla_pressionada:
                self.tecla_pressionada = True
                self.__velocidade = -10
            
            if not teclas[pygame.K_UP]:
                self.tecla_pressionada = False

    def morreu(self, chao):
         # checa se o personagem atingiu o chão
        if self.gera_retangulo().colliderect(chao.sprites()[0].rect):
            self.__game_over = True
            self.__voando = False
        # checa se o personagem saiu da tela
        elif self.y <= 0:
            self.__game_over = True
