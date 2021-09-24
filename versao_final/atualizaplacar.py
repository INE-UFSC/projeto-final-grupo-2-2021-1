from pontuacaoDAO import PontuacaoDAO

class Placar:
    def __init__(self) -> None:
        self.__pontuacaoDAO = PontuacaoDAO()
        self.__nome_usuarios = self.__pontuacaoDAO.get_all()
        self.__rank_pontuacao = []
        self.__organizar_rank()
        self.__retirar_pontuacao_menor()

    @property
    def rank_pontuacao(self):
        return self.__rank_pontuacao

    def __organizar_rank(self):
        rank = []
        for usuario in self.__nome_usuarios:
            pontos = self.__pontuacaoDAO.get(usuario)
            rank.append([usuario, pontos])
        
        rank = sorted(rank, key=lambda x: x[1])
        
        self.__rank_pontuacao = rank.copy()

    def __retirar_pontuacao_menor(self):
        for pontos in self.__rank_pontuacao: 
            if len(self.__rank_pontuacao) > 8:
                nome = self.__rank_pontuacao.pop(0)[0]
                self.__pontuacaoDAO.remove(nome)
            else:
                break

        
    
