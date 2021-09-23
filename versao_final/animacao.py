import pygame
from abc import ABC, abstractmethod
import os
from constantes import Constante

class Animacao(pygame.sprite.Sprite, ABC):
    def __init__(self, diretorio) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.const = Constante()
        self.sprite_atual = 0
        self.__sprites = []
        self.diretorio = diretorio
        self.__busca_arquivo()
        self.image = self.__sprites[self.sprite_atual]

    @property
    def sprites(self):
        return self.__sprites

    def __busca_arquivo(self):
        for arquivo in self.diretorio:
            self.__busca_sprite(arquivo)

    def __busca_sprite(self, arquivo):
        for sprite in os.listdir(arquivo):
            self.__sprites.append(pygame.image.load(arquivo + sprite))

    @abstractmethod
    def update(self):
        pass

class PersonagemAnimacao(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/personagem/'])
        self.__rect = self.image.get_rect(center=(self.const.posicao_personagem_x, self.const.posicao_personagem_y))
        self.inicio_posicao = True

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    def update(self, x, y):
        self.sprite_atual = self.sprite_atual + 0.05
        if self.sprite_atual >= len(self.sprites):
            self.sprite_atual = 0
        self.image = self.sprites[int(self.sprite_atual)]
        self.image = pygame.transform.scale(self.image, (int(716/11), int(632/11)))
        self.__rect = self.image.get_rect(center=(x, y))
    
class CanoSuperiorAnimacao(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/cano/canosuperior/'])
        self.__rect = self.image.get_rect(center=(self.const.posicao_gera_cano, 0))
        self.inicio_posicao = True

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    def update(self, x, y):
        self.sprite_atual = self.sprite_atual + 0.05
        if self.sprite_atual >= len(self.sprites):
            self.sprite_atual = 0
        self.image = self.sprites[int(self.sprite_atual)]
        self.image = pygame.transform.scale(self.image, (int(388/8), int(5048/8)))
        self.__rect = self.image.get_rect(center=(x, y))

class CanoInferiorAnimacao(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/cano/canoinferior/'])
        self.__rect = self.image.get_rect(center=(self.const.posicao_gera_cano, 0))
        self.inicio_posicao = True

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    def update(self, x, y):
        self.sprite_atual = self.sprite_atual + 0.10
        if self.sprite_atual >= len(self.sprites):
            self.sprite_atual = 0
        self.image = self.sprites[int(self.sprite_atual)]
        self.image = pygame.transform.scale(self.image, (int(388/8), int(5048/8)))
        self.__rect = self.image.get_rect(center=(x, y))

class ItemInvencivelAnimacao(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/item/iteminvencibilidade/'])
        self.__rect = self.image.get_rect(center=(self.const.tela_jogo_largura, 0))
        self.inicio_posicao = True

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    def update(self, x, y):
        self.sprite_atual = self.sprite_atual + 0.10
        if self.sprite_atual >= len(self.sprites):
            self.sprite_atual = 0
        self.image = self.sprites[int(self.sprite_atual)]
        self.image = pygame.transform.scale(self.image, (int(50*1.3), int(50*1.3)))
        self.__rect = self.image.get_rect(center=(x, y))

class ItemPequenoAnimacao(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/item/itempequeno/'])
        self.__rect = self.image.get_rect(center=(self.const.tela_jogo_largura, 0))
        self.inicio_posicao = True

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect

    def update(self, x, y):
        self.sprite_atual = self.sprite_atual + 0.10
        if self.sprite_atual >= len(self.sprites):
            self.sprite_atual = 0
        self.image = self.sprites[int(self.sprite_atual)]
        self.image = pygame.transform.scale(self.image, (int(50*1.3), int(50*1.3)))
        self.__rect = self.image.get_rect(center=(x, y))

class ChaoAnimacao(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/cenario/chao/'])
        self.posicao_chao = 438.5
        self.__rect = self.image.get_rect(center=(self.posicao_chao, self.const.tela_jogo_altura-30))
        self.velocidade_chao = 2
    
    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, rect):
        self.__rect = rect
    
    def update(self):
        self.sprite_atual = self.sprite_atual + 0.05
        if self.sprite_atual >= len(self.sprites):
            self.sprite_atual = 0
        self.image = self.sprites[int(self.sprite_atual)]
        self.image = pygame.transform.scale(self.image, ((int(3072/3.5)), (int(208/3.5))))
        self.__rect = self.image.get_rect(center=(self.posicao_chao, self.const.tela_jogo_altura-30))
        self.move_chao()

    def move_chao(self):
        if self.posicao_chao <= 347:
            self.posicao_chao = 438.5
        self.posicao_chao -= self.velocidade_chao
