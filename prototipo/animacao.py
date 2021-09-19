import pygame
from abc import ABC, abstractmethod
import os

class Animacao(pygame.sprite.Sprite, ABC):
    def __init__(self, diretorio) -> None:
        pygame.sprite.Sprites.__init__(self)
        self.sprite_atual = 0
        self.__sprites = []
        self.diretorio = diretorio
        self.__busca_arquivo()
        self.imagem = self.__sprites[self.sprite_atual]

    @property
    def sprites(self):
        return self.__sprites

    def __busca_arquivo(self):
        for arquivo in self.diretorio:
            self.busca_sprite(arquivo)
    
    def __busca_sprite(self, arquivo):
        for sprite in os.listdir(arquivo):
            self.__sprites.append(pygame.image.load(arquivo + sprite))

    @abstractmethod
    def atualiza(self):
        pass

class PersonagemAnimacao(Animacao):
    def __init__(self) -> None:
        super().__init__(['prototipo/sprites/personagem/'])

    def atualiza(self):
        self.sprite_atual = self.sprite_atual + 0.05
        if self.sprite_atual >= len(self.sprites):
            self.sprite_atual = 0
        self.imagem = self.sprites[int(self.sprite_atual)]


    

        


