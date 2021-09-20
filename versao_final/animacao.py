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
        self.image = pygame.transform.scale(self.image, (int(716/10), int(632/10)))
        self.__rect = self.image.get_rect(center=(x, y))


