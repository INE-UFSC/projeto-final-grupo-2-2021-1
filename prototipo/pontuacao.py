#Essa classe irá realizar o calculo dos pontos, e posteriormente enviar para o banco de dados

class Pontuacao:
    def __init__(self) -> None:
        self.__pontos = 0
        self.status_game_over = False
        self.printou = False

    def marca_ponto(self, valor_ponto):
        self.__pontos += valor_ponto
    
    def mostra_ponto(self, status_game_over):
        self.status_game_over = status_game_over
        if self.status_game_over and self.printou == False:
            print(self.__pontos)
            self.printou = True
