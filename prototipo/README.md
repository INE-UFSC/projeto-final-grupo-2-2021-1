Nesse diretório, o grupo irá trabalhar em cima do primeiro protótipo do jogo.

A ideia do protótipo não é que ele seja uma versão demo do jogo completo, mas sim que o principal mecanismo do jogo esteja implementado com certo grau de sucesso. Exemplo: em um jogo do tipo plataforma 2D, basta mostrar um retângulo colidindo com objetos e saltando/destruindo com alguma comando do usuário. A interface gráfica (com sprites) é opcional nessa etapa.

Como jogar:

- Executar o arquivo "app.py";
- Para iniciar o jogo, pressionar a seta para cima, que também será a responsável pela movimentação do personagem.

Funcionalidades do jogo:

- O objetivo principal é desviar o pássaro (quadrado vermelho) dos canos (retângulos verdes);
- É possível o personagem pegar itens que alteram seus atributos por um determinado tempo;
- O Item amarelo diminui o personagem;
- O Item cinza dá invencibilidade para o personagem;
- O personagem ainda não é capaz de pegar dois itens ao mesmo tempo;
- No final do jogo é printado no terminal os pontos contabilizados.

Melhorias de construção:

- Foi identificado pela equipe a necessidade de construir classes responsáveis apenas pelo gerenciamento dos itens, e dos canos. Pois quando são inseridos esses objetos no arquivo "app.py", acaba deixando o código com um alto acoplamento. Logo, é necessário realizar essa mudança até a entrega final.
