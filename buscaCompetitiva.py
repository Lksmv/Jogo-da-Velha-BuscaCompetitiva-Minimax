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
    num = rd.choice([0,1])
    if num == 0:
        jogador = humano
        print("Humano Sorteado ('O')")
    else:
        jogador = pc
        print("Computador Sorteado ('X')")
    exibeTabuleiro(tabuleiro)
    resultado = jogo(tabuleiro,jogador)
    print(resultado)
    
    



def exibeTabuleiro(tabuleiro):
    print("\n   "+tabuleiro[0][0] + "  \ " + tabuleiro[0][1] + " \ " + tabuleiro[0][2])
    print("   ~~~\~~~\~~~")
    print("   "+tabuleiro[1][0] + "  \ " + tabuleiro[1][1] + " \ " + tabuleiro[1][2])
    print("   ~~~\~~~\~~~")
    print("   "+tabuleiro[2][0] + "  \ " + tabuleiro[2][1] + " \ " + tabuleiro[2][2]+"\n")
    
def jogo(tabuleiro,jogador):

    profundidade = 9 ## Profundidade máxima da árvore que será gerada

    while (verificarEstado(tabuleiro) == 0):
        if jogador == 1:
            print("Máquina")
            l,c,pontos = minimax(tabuleiro,profundidade,True)
            tabuleiro[l][c] = pc
            exibeTabuleiro(tabuleiro)
            jogador = 0
            profundidade -= 1
        else:
            print("Humano")
            l,c = vezHumano(tabuleiro)
            tabuleiro[l][c] = humano
            jogador = 1
            profundidade -= 1
            print('- Tabuleiro')
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
        

def verificarEstado(tabuleiro): #retorna o estado : -1 = PC ganhador
                       #                   1 = Humano ganhador 
                       #                   0 = sem ganhador com espaços vagos no tabuleiro 
                       #                   2 = sem ganhador e sem espaços vagos ( EMPATE )
                       
    for linha in range(3):
        if ((tabuleiro[linha][0] == tabuleiro[linha][1]) and (tabuleiro[linha][1] == tabuleiro[linha][2])):
            if tabuleiro[linha][0] == pc:
                return -1
            elif tabuleiro[linha][0] == humano:
                return 1
    
    for coluna in range(3):
        if ((tabuleiro[0][coluna] == tabuleiro[1][coluna]) and (tabuleiro[1][coluna] == tabuleiro[2][coluna])):
            if tabuleiro[0][coluna] == pc:
                return -1
            elif tabuleiro[0][coluna] == humano:
                return 1

    if ((tabuleiro[0][0] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[2][2])):
            if tabuleiro[0][0] == pc:
                return -1
            elif tabuleiro[0][0] == humano:
                return 1
    
    if ((tabuleiro[2][0] == tabuleiro[1][1]) and (tabuleiro[1][1] == tabuleiro[0][2])):
            if tabuleiro[2][0] == pc:
                return -1
            elif tabuleiro[2][0] == humano:
                return 1
            
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == vazio:
                return 0
    return 2

def minimax(tabuleiro,profundidade,isMax):
    # pontuacao [0] = linha
    # pontuacao [1] = coluna
    # pontuacao [2] = pontos
    
    if ((profundidade < 1) or (verificarEstado(tabuleiro) == 2)):
        return [-1,-1,verificarEstado(tabuleiro)]
    
    if isMax:
        melhor_pontuacao = [-1,-1,math.inf]

        for espacos in jogadas(tabuleiro):
            l = espacos[0]
            c = espacos[1]
            tabuleiro[l][c] = pc
            pontuacao_atual = minimax(tabuleiro,profundidade-1,False)
            tabuleiro[l][c] = vazio
            if melhor_pontuacao[2] > pontuacao_atual[2]:
                melhor_pontuacao[0] = l
                melhor_pontuacao[1] = c
                melhor_pontuacao[2] = pontuacao_atual[2]
    else:
        melhor_pontuacao = [-1,-1,-math.inf]

        for espacos in jogadas(tabuleiro):
            l = espacos[0]
            c = espacos[1]
            tabuleiro[l][c] = humano
            pontuacao_atual = minimax(tabuleiro,profundidade-1,True)
            tabuleiro[l][c] = vazio
            if melhor_pontuacao[2] < pontuacao_atual[2]:
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
