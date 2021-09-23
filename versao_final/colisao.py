class Colisao:
    def __init__(self) -> None:
        pass

    def detectar_colisao(self, personagem, objeto):
        
        lista_retangulos = objeto.gera_retangulo()

        if personagem.voando and not personagem.game_over:
            for retangulo in lista_retangulos:
                if personagem.gera_retangulo().colliderect(retangulo):
                    objeto.efeito_colisao(personagem)
