from paginamenu import PaginaMenu
from paginapontuacao import PaginaPontuacao
from paginacomojogar import PaginaComoJogar
from paginafimdejogo import PaginaFimDeJogo
from paginafechar import PaginaSair
from controlador import Controlador


class ControladorPagina:
    def __init__(self):
        self.__pontuacao_jogo = 0
        self.__pagina_atual = 'MenuPrincipal'

    def iniciar(self):
        while True:
            try:
                self.paginas = {
                    'MenuPrincipal' : PaginaMenu(),
                    'Jogo'          : Controlador(),
                    'Pontuacao'     : PaginaPontuacao(),
                    'ComoJogar'     : PaginaComoJogar(),
                    'FimDeJogo'     : PaginaFimDeJogo(self.__pontuacao_jogo),
                    'PaginaFechar'  : PaginaSair()
                    }
                
                self.paginas[self.__pagina_atual].menu()
                self.__pagina_atual = self.paginas[self.__pagina_atual].estado

                if self.__pagina_atual == 'FimDeJogo':
                    self.__pontuacao_jogo = self.paginas['Jogo'].pontuacao.pontos
                
            except KeyError:
                print(("O botão clicado não foi instanciado corretamente!"))
