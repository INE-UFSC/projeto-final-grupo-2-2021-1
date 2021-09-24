from abc import ABC, abstractmethod
from pontuacaoDAO import PontuacaoDAO
from spritebotoes import SpriteBotaoJogar, SpriteBotaoComoJogar, \
        SpriteBotaoPontuacao, SpriteBotaoSalvar, SpriteBotaoVoltar, SpriteCaixaTexto
import pygame

class BotaoGenerico(ABC):
    def __init__(self, sprite) -> None:
        self.__sprite = pygame.sprite.Group(sprite)
    
    def atualizar(self, x, y):
        self.__sprite.update(x, y)
    
    def desenhar(self, tela):
        self.__sprite.draw(tela)
    
    def gera_retangulo(self):
        rect_superior = self.__sprite.sprites()[0].rect

        return rect_superior
    
    @abstractmethod
    def efeito_colisao(self):
        pass

class BotaoJogar(BotaoGenerico):
    def __init__(self) -> None:
        sprite = pygame.sprite.Group(SpriteBotaoJogar())
        super().__init__(sprite)

    def efeito_colisao(self):
        return "Jogo"

class BotaoComoJogar(BotaoGenerico):
    def __init__(self) -> None:
        sprite = pygame.sprite.Group(SpriteBotaoComoJogar())
        super().__init__(sprite)

    def efeito_colisao(self):
        return "ComoJogar"

class BotaoPontuacao(BotaoGenerico):
    def __init__(self) -> None:
        sprite = pygame.sprite.Group(SpriteBotaoPontuacao())
        super().__init__(sprite)

    def efeito_colisao(self):
        return "Pontuacao"

class BotaoVoltar(BotaoGenerico):
    def __init__(self) -> None:
        sprite = pygame.sprite.Group(SpriteBotaoVoltar())
        super().__init__(sprite)

    def efeito_colisao(self):
        return "MenuPrincipal"

class BotaoSalvar(BotaoGenerico):
    def __init__(self) -> None:
        sprite = pygame.sprite.Group(SpriteBotaoSalvar())
        super().__init__(sprite)
        self.__pontuacao_dao = PontuacaoDAO() 
        self.__salvo = False

    @property
    def salvo(self):
        return self.__salvo

    def efeito_colisao(self, pontuacao, nome):
        nome = str(nome).upper()

        try:
            self.__pontuacao_dao.get(nome)
            return "Esse User ja existe!"

        except:
            if len(nome) < 3:
                return "O User deve conter 3 caracteres!"
            else:
                self.__pontuacao_dao.add(nome, pontuacao)
                self.__salvo = True
                return "MenuPrincipal"

        
class CaixaTexto(BotaoGenerico):
    def __init__(self) -> None:
        sprite = pygame.sprite.Group(SpriteCaixaTexto())
        super().__init__(sprite)

    def efeito_colisao(self):
        return True