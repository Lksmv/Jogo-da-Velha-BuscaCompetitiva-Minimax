import random as rd
import math

humano = 'O' 
pc = 'X'     
vazio = ' '  


def main():
    tabuleiro = [
            [vazio,vazio,vazio],
            [vazio,vazio,vazio],
            [vazio,vazio,vazio]
            ]
    print("Jogo da Velha!")
    print("Sorteio de quem ira iniciar!")
    num = rd.choice([0,1])# sorteia 0 ou 1, 0 para jogador e 1 para computador
    print(num)
    if num == 0:
        jogador = 0
        print("Humano Sorteado ('O')")
    else:
        jogador = 1
        print("Computador Sorteado ('X')")
    exibeTabuleiro(tabuleiro)
    resultado = jogo(tabuleiro,jogador)
    if resultado == 1:
        print("Vitoria do Computador!!!")
    elif resultado == -1:
        print("Vitoria do Jogador!!!")
    else:
        print("EMPATE!!!")
        
    print("Jogar Novamente? Y/N")
    x = input()
    if(x == 'Y' or x == 'y'):
        main()
        
    



def exibeTabuleiro(tabuleiro):# exibe o tabuleiro
    print("\n   "+tabuleiro[0][0] + "  \ " + tabuleiro[0][1] + " \ " + tabuleiro[0][2])
    print("   ~~~\~~~\~~~")
    print("   "+tabuleiro[1][0] + "  \ " + tabuleiro[1][1] + " \ " + tabuleiro[1][2])
    print("   ~~~\~~~\~~~")
    print("   "+tabuleiro[2][0] + "  \ " + tabuleiro[2][1] + " \ " + tabuleiro[2][2]+"\n")
    
def jogo(tabuleiro,jogador): 

    profundidade = 9 ## Profundidade máxima da árvore que será gerada

    while (verificarEstado(tabuleiro) == 0):
        if jogador == 1:# caso seja a vez do computador
            print("Máquina")
            if(profundidade == 9):
                l = rd.choice([0,1,2])
                c = rd.choice([0,1,2])
            else:
                l,c,pontos = minimax(tabuleiro,profundidade,True) #executa o algoritmo minimax, que vai retornar a jogada otima
            tabuleiro[l][c] = pc # faz a 'jogada'
            exibeTabuleiro(tabuleiro) # exibe tabuleiro com a jogada da maquina
            jogador = 0
            profundidade -= 1
        else: # vez do humano
            print("Humano")
            l,c = vezHumano(tabuleiro) # executa o metodo responsavel por validar e perguntar a jogada ao jogador
            tabuleiro[l][c] = humano # fez a 'jogada'
            jogador = 1
            profundidade -= 1
            print('** Tabuleiro **')
            exibeTabuleiro(tabuleiro)

    return verificarEstado(tabuleiro)


def vezHumano(tabuleiro):
    l = -1
    c = -1
    print("Informe sua jogada !! Linha e Coluna [0,1,2] e separados por virgula! ex: ' 0,2 ' ")
    jogada = input()
    posicoes = jogada.split(",")
    l = int(posicoes[0])
    c = int(posicoes[1])
    if(l >= 3 or l <= -1):
        print("Jogada invalida!")
    elif(c >= 3 or c <= -1):
        print("Jogada invalida!")
    elif(tabuleiro[l][c]!= ' '):
        print("Jogada invalida!")
    else:
        print("Jogada Valida!")
        print("Linha: " + str(l) + " - Coluna: " + str(c))
        return l, c
    return vezHumano(tabuleiro)
        

def verificarEstado(tabuleiro): #retorna o estado : 1 = PC ganhador
                       #                   -1 = Humano ganhador 
                       #                   0 = sem ganhador com espaços vagos no tabuleiro 
                       #                   2 = sem ganhador e sem espaços vagos ( EMPATE )
                       
    for linha in range(3): #verifica as 3 linhas
        if ((tabuleiro[linha][0] == tabuleiro[linha][1]) and (tabuleiro[linha][1] == tabuleiro[linha][2])):
            if tabuleiro[linha][0] == pc:
                return 1
            elif tabuleiro[linha][0] == humano:
                return -1
    
    for coluna in range(3): # verifica as 3 colunas
        if ((tabuleiro[0][coluna] == tabuleiro[1][coluna]) and (tabuleiro[1][coluna] == tabuleiro[2][coluna])):
            if tabuleiro[0][coluna] == pc:
                return 1
            elif tabuleiro[0][coluna] == humano:
                return -1

    if ((tabuleiro[0][0] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[2][2])): # verifica  a diagonal \
            if tabuleiro[0][0] == pc:
                return 1
            elif tabuleiro[0][0] == humano:
                return -1
    
    if ((tabuleiro[2][0] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[0][2])): # verifica a diagonal /
            if tabuleiro[2][0] == pc:
                return 1
            elif tabuleiro[2][0] == humano:
                return -1
            
    for i in range(3): # procura por espaço vazio
        for j in range(3):
            if tabuleiro[i][j] == vazio:
                return 0
    return 2 # caso não tenha vencedor e não tenha espaço vazio retorna 2 ( EMPATE )

def pontos(tabuleiro): # pontuacao >  1 = pc ganhador
                       # pontuacao > -1 = humano ganhador
                       # pontuacao >  0 = sem ganhador

    for linha in range(3):
        if ((tabuleiro[linha][0] == tabuleiro[linha][1]) and (tabuleiro[linha][1] == tabuleiro[linha][2])):
            if tabuleiro[linha][0] == pc:
                return 1
            elif tabuleiro[linha][0] == humano:
                return -1
    
    for coluna in range(3):
        if ((tabuleiro[0][coluna] == tabuleiro[1][coluna]) and (tabuleiro[1][coluna] == tabuleiro[2][coluna])):
            if tabuleiro[0][coluna] == pc:
                return 1
            elif tabuleiro[0][coluna] == humano:
                return -1

    if ((tabuleiro[0][0] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[2][2])):
            if tabuleiro[0][0] == pc:
                return 1
            elif tabuleiro[0][0] == humano:
                return -1
    
    if ((tabuleiro[2][0] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[0][2])):
            if tabuleiro[2][0] == pc:
                return 1
            elif tabuleiro[2][0] == humano:
                return -1

    return 0

def minimax(tabuleiro,profundidade,isMax): # algoritmo minmax : gera uma arvore(Game Tree), onde cada nó representa uma jogada
                                           # e cada linha da arvore um turno, até chegar no final da ramificação. Guardando
                                           # o resultado ( -1 perder, 0 empatar e 1 ganhar)
    # pontuacao [0] = linha
    # pontuacao [1] = coluna
    # pontuacao [2] = pontos
    
    if isMax: # turno computador
        melhor_pontuacao = [-1,-1,-math.inf]
        jogador = pc
    else: #turno jogador
        jogador = humano
        melhor_pontuacao = [-1,-1,math.inf]
    
    if ((profundidade < 1) or pontos(tabuleiro) == 1 or pontos(tabuleiro) == -1): #ultimo nó
        return [-1,-1,pontos(tabuleiro)]
    

    for espacos in jogadas(tabuleiro):
        l = espacos[0]
        c = espacos[1]
        tabuleiro[l][c] = jogador
        pontuacao_atual = minimax(tabuleiro,profundidade-1,isMax == False)
        tabuleiro[l][c] = vazio            
    
        if isMax:
            if pontuacao_atual[2] > melhor_pontuacao[2]:
                melhor_pontuacao[0] = l
                melhor_pontuacao[1] = c
                melhor_pontuacao[2] = pontuacao_atual[2]
        else:
            if pontuacao_atual[2] < melhor_pontuacao[2]:
                melhor_pontuacao[0] = l
                melhor_pontuacao[1] = c
                melhor_pontuacao[2] = pontuacao_atual[2]
                
    return melhor_pontuacao

def jogadas(tabuleiro):

    jogadas = []

    for l in range(3):
        for c in range(3):
            if tabuleiro[l][c] == vazio:
                jogadas.append([l,c])
    return jogadas


if __name__ == "__main__":
    main()

# Amanda Miranda Zanella, Bárbara Alessandra Maas, Bruno Henrique Wiedemann Reis e Lucas Miguel Vieira
#  Jogo da Velha
#  Regras:
# É um jogo de regras extremamente simples, que não traz grandes dificuldades para seus jogadores e é facilmente aprendido.

# Participam duas pessoas, que jogam alternadamente, preenchendo cada um dos espaços vazios. Cada participante deve usar um símbolo (X ou O).

# Vence o jogador que conseguir formar primeiro uma linha com três símbolos iguais, seja ela na horizontal, vertical ou diagonal.

#  Formulação completa do problema de busca:
# Estado inicial > Tabuleiro Vazio

# Estado objetivo > Conseguir formar um linha, coluna ou diagonal com três símbolos iguais.

# Função sucessor (ações possíveis) > Preencher um dos espaços vazios do tabuleiro.

# Custo de caminho > Não é relevante nesse caso.

#  Algoritmo escolhido:
# É determinístico, pois, dado um conjunto de entradas conhecido, o jogo retorna um único conjunto de saídas.

# O algoritmo implementado para o jogo da velha foi o minimax, que é a melhor estratégia para os jogos determinísticos. Com base em todas as possibilidades de jogo, ele escolhe a jogada com o melhor retorno possível para chegar no objetivo, que é ganhar, mesmo com o oponente jogando da melhor forma possível.

# Outro algoritmo que poderia ser implementado é o Poda Alfa-Beta, que, pelo algoritmo minimax, busca diminuir o número de nós que são avaliados.
