## Jogo da Velha

#### Regras:

- É um jogo de regras extremamente simples, que não traz grandes dificuldades para seus jogadores e é facilmente aprendido.
- Participam duas pessoas, que jogam alternadamente, preenchendo cada um dos espaços vazios. Cada participante deve usar um símbolo (X ou O).
- Vence o jogador que conseguir formar primeiro uma linha com três símbolos iguais, seja ela na horizontal, vertical ou diagonal.


#### Formulação completa do problema de busca:

- Estado inicial > Tabuleiro Vazio
- Estado objetivo > Conseguir formar um linha, coluna ou diagonal com três símbolos iguais.
- Função sucessor (ações possíveis) > Preencher um dos espaços vazios do tabuleiro.
- Custo de caminho > Não é relevante nesse caso.


#### Algoritmo escolhido:

- É determinístico, pois, dado um conjunto de entradas conhecido, o jogo retorna um único conjunto de saídas.
- O algoritmo implementado para o jogo da velha foi o minimax, que é a melhor estratégia para os jogos determinísticos. Com base em todas as possibilidades de jogo, ele escolhe a jogada com o melhor retorno possível para chegar no objetivo, que é ganhar, mesmo com o oponente jogando da melhor forma possível.
- Outro algoritmo que poderia ser implementado é o Poda Alfa-Beta, que, pelo algoritmo minimax, busca diminuir o número de nós que são avaliados.