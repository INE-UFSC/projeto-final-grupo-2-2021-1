import pygame
from constantes import Constante
from animacao import PersonagemAnimacao
from personagem import Personagem


class Jogador(Personagem):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.velocidade = 0 
        self.voando = False 
        self.game_over = False
        self.tamanho = self.const.tamanho_personagem 
        self.invencivel = False 
        self.cor = (255, 0, 0) 

    def mover(self):
         # confere se o personagem está voando para aplicar a gravidade sobre ele
        if self.voando:
            self.velocidade += 0.5   # medida que o personagem desce a cada loop
            if self.velocidade > 8:   # evita que o personagem caia muito rapidamente
                self.velocidade = 8
            if self.y + self.tamanho <= self.const.tela_jogo_altura:  # se o personagem não estiver no chão, atualiza sua posição
                self.y += int(self.velocidade)

        # controle do pulo do personagem
        if not self.game_over:
            teclas = pygame.key.get_pressed()  # verifica quais teclas foram pressionadas
            if teclas[pygame.K_UP] and self.tecla_pressionada == False:
                self.tecla_pressionada = True
                self.velocidade = -10
            
            if not teclas[pygame.K_UP]:
                self.tecla_pressionada = False

    def morreu(self, chao):
         # checa se o personagem atingiu o chão
        if self.gera_retangulo().colliderect(chao.sprites()[0].rect):
            self.game_over = True
            self.voando = False
        # checa se o personagem saiu da tela
        elif self.y <= 0:
            self.game_over = True