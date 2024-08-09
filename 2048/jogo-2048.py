from funcoes import *

def main():
    print('-'*70)
    print('Bem vindo ao 2048!')
    print('O seu objetivo é chegar em 2048(ou qualquer potência de 2 que você decidir)\nmovendo os valores pra direita, esquerda, cima ou baixo')

    #Confere se a dificuldade escolhida é uma potência de 2, se não for reinicia o jogo
    dificuldade=int(input('\nEscolha sua dificuldade(Potência de 2): '))
    if dificuldade not in potenciaDeDois():
        print('Dificuldade inválida!')
        print('Fim de jogo!')
        main()
    
    tabuleiro=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    dois_ou_quatro(tabuleiro)

    mostra_tabuleiro(tabuleiro)

    print('Comandos possíveis: ')
    print('Mover para direita = D')
    print('Mover para esquerda = A')
    print('Mover para cima = W')
    print('Mover para baixo = S')
    print('Para finalizar o jogo = F')
    print('Para reiniciar o jogo = R')

    
    #Confere se houve vitória, game over, ou se o jogo continua
    while True:
        
        if vitoria(tabuleiro,dificuldade)==True:
            print('Parabéns, você ganhou!')
            print('\nDigite F para finalizar o jogo.')
            print('Ou digite qualquer letra para reiniciar o jogo.')

            comando_2 = input('Digite seu comando: ').upper()
            
            if comando_2 == 'F':
                comand_2 = False
                break
            
            else:
                main()
        
        chave= False

        #Verifica se ainda existe possibilidade de jogar, ou seja, se há zeros ou se há nos arredores números iguais
        #Caso nenhuma dessas condições sejam satisfeitas - e não tiver ocorrido vitória- , o jogador perde

        for numero_linha in range(len(tabuleiro)):
            for numero_coluna in range(len(tabuleiro)):
                if numero_coluna != (len(tabuleiro) - 1):
                    if tabuleiro[numero_linha][numero_coluna + 1] == 0 or tabuleiro[numero_linha][numero_coluna] == tabuleiro[numero_linha][numero_coluna + 1]:
                        chave = True
                if numero_linha != (len(tabuleiro) - 1):
                    if tabuleiro[numero_linha + 1][numero_coluna] == 0 or tabuleiro[numero_linha][numero_coluna] == tabuleiro[numero_linha + 1][numero_coluna]:
                        chave = True

        if chave == False:
            print('Game Over!')
            print('\nDigite F para finalizar o jogo.')
            print('Ou digite qualquer letra para reiniciar o jogo.')

            comando_3 = input('Digite seu comando: ').upper()
            
            if comando_3 == 'F':
                comand_3 = False
                break
            
            else:
                main()     
                    
        comando=(input('Digite seu comando: ')).upper()

        if comando == 'D':
            direita(tabuleiro)
            dois_ou_quatro(tabuleiro)
            mostra_tabuleiro(tabuleiro)
            
        elif comando == 'A':
            esquerda(tabuleiro)
            dois_ou_quatro(tabuleiro)
            mostra_tabuleiro(tabuleiro)
            
        elif comando == 'W':
            cima(tabuleiro)
            dois_ou_quatro(tabuleiro)
            mostra_tabuleiro(tabuleiro)
            
        elif comando == 'S':
           baixo(tabuleiro)
           dois_ou_quatro(tabuleiro)
           mostra_tabuleiro(tabuleiro)

        elif comando == 'F':
            print('Saindo do jogo...')
            break

        elif comando == 'R':
            main()

        else:
            print('Comando inválido')
 

    return None

if __name__ == "__main__":
    main()
