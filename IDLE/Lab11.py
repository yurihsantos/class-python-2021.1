# Nome: Yurih Santos de Oliveira
# DRE: 121056855

#1 - Não delete nem modifique esta linha

import random

def cartas():
    lista = list(range(1,8+1))*2
    lista = random.sample(lista, 16)
    matriz = [lista[:4], lista[4:8], lista[8:12], lista[12:16]]
    return matriz

def mascarado():
    matriz = [ ]
    for i in range(4):
        list.append(matriz , 4*['*'] )
    return matriz

def exibeMatriz(matriz):
    print(matriz[0][0],matriz[0][1],matriz[0][2],matriz[0][3])
    print(matriz[1][0],matriz[1][1],matriz[1][2],matriz[1][3])
    print(matriz[2][0],matriz[2][1],matriz[2][2],matriz[2][3])
    print(matriz[3][0],matriz[3][1],matriz[3][2],matriz[3][3])

def verificaEntrada(x ,y , mascara):
    if x > 3 or x < 0:
        return True
    elif y > 3 or y < 0:
        return True
    elif mascara[x][y] != '*':
        return True
    else:
        return False
    
def pede_entrada1(mascara):
    exibeMatriz(mascara)
    c = input("Escolha a Primeira posição [x,y]: ")
    x = int(c[1])
    y = int(c[3])    
    while verificaEntrada(x,y,mascara):
        exibeMatriz(mascara)
        c = input("Posição invalida ou já escolhida. Escolha a Primeira posição [x,y]: ")
        x = int(c[1])
        y = int(c[3])
    return (x, y)

def pede_entrada2(mascara):
    exibeMatriz(mascara)
    c = input("Escolha a Segunda posição [x,y]: ")
    x = int(c[1])
    y = int(c[3])    
    while verificaEntrada(x,y,mascara):
        exibeMatriz(mascara)
        c = input("Posição invalida ou já escolhida. Escolha a Segunda posição [x,y]: ")
        x = int(c[1])
        y = int(c[3])
    return (x, y)

def verificaJogada(carta1 , carta2, mascara):
    if carta1 == carta2:
        exibeMatriz(mascara)
        print("Parabéns você acertou")
        return True
    else:
        exibeMatriz(mascara)        
        print("Você errou... Tente novamente")
        return False
    
def jogada(mascara, matriz, lista):
    c1 = pede_entrada1(mascara)
    carta1 = matriz[c1[0]][c1[1]]
    mascara[c1[0]][c1[1]] = carta1    
    c2 = pede_entrada2(mascara)
    carta2 = matriz[c2[0]][c2[1]]
    mascara[c2[0]][c2[1]] = carta2        
    if verificaJogada(carta1, carta2, mascara):
        list.append(lista,carta1)
    else:
        mascara[c1[0]][c1[1]] = '*'
        mascara[c2[0]][c2[1]] = '*'
          
def main():
    mascara = mascarado()
    matriz = cartas()
    tentativas = 0
    lista = []
    while len(lista) < 8 :
        jogada(mascara, matriz, lista)
        tentativas = tentativas + 1
    print("Parabéns você conseguiu concluir o jogo em ", tentativas, "tentativas")

if __name__ == "__main__":
    main()
    
#Casos de teste da questão 1 - Não delete nem modifique esta linha
