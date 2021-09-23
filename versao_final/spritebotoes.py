from animacao import Animacao
import pygame

class SpriteBotaoJogar(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/jogar/'])
        self.__rect = self.image.get_rect(center=(0, 0))
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
        self.image = pygame.transform.scale(self.image, (int(192), int(48)))
        self.__rect = self.image.get_rect(center=(x, y))

class SpriteBotaoComoJogar(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/comojogar/'])
        self.__rect = self.image.get_rect(center=(0, 0))
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
        self.image = pygame.transform.scale(self.image, (int(192), int(48)))
        self.__rect = self.image.get_rect(center=(x, y))

class SpriteBotaoVoltar(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/voltar/'])
        self.__rect = self.image.get_rect(center=(0, 0))
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
        self.image = pygame.transform.scale(self.image, (int(192), int(48)))
        self.__rect = self.image.get_rect(center=(x, y))

class SpriteBotaoPontuacao(Animacao):
    def __init__(self) -> None:
        super().__init__(['versao_final/sprites/botoes/pontuacao/'])
        self.__rect = self.image.get_rect(center=(0, 0))
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
        self.image = pygame.transform.scale(self.image, (int(192), int(48)))
        self.__rect = self.image.get_rect(center=(x, y))