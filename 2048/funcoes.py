import random as rand 

def vitoria(tabuleiro, dificuldade):
    '''
        Verifica se o jogador possui pontuação o suficiente para ser declarado vencedor

        Args:

            tabuleiro (list): Tabuleiro do jogo
            dificuldade (int): Pontuação mínima para ser declarado vencedor 
            
        Retorna:

            bool: True caso o jogador tenha vencido e False caso não
    '''
    for linha in tabuleiro:
        if dificuldade in linha:
            return True
    return False


def dois_ou_quatro(tabuleiro):
    '''
        Insere 2 ou 4 em uma casa vazia pseudoaleatória do tabuleiro. O número 2 possui 75% de chances de ser inserido

        Args:

            tabuleiro (list): Tabuleiro do jogo
            
        Retorna:

            None
    '''

    numero = 2
    if round(rand.random(), 2) >= 0.75:
        numero = 4
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    if 0 in [valor for linha in tabuleiro for valor in linha]:
        while True:
            linha_rand = rand.randrange(linhas)
            coluna_rand = rand.randrange(colunas)
            if tabuleiro[linha_rand][coluna_rand] == 0:
                tabuleiro[linha_rand][coluna_rand] = numero
                break
    return None


def mostra_tabuleiro(tabuleiro):
    '''
        Mostra o tabuleiro formatado para o jogador

        ASSUME QUE o argumento é um tabuleiro válido

        Args:

            tabuleiro (list): Tabuleiro do jogo 
            
        Retorna:

            None
    '''

    dim_tabuleiro = len(tabuleiro)
    print(' ____' * dim_tabuleiro)
    for lin_contador in range(dim_tabuleiro):
        for col_contador in range(dim_tabuleiro):
            valor_str = str(tabuleiro[lin_contador][col_contador])
            espaco = ' ' * (4 - len(valor_str))
            if col_contador == (dim_tabuleiro - 1):
                print('|' + valor_str + espaco + '|')
            else:
                print('|' + valor_str + espaco, end = '')
                
    print(' ‾‾‾‾' * dim_tabuleiro)
    return None


def esquerda(tabuleiro):
    '''
        Move os valores de tabuleiro para a esquerda

        ASSUME QUE o argumento é um tabuleiro válido

        Args:

            tabuleiro (list): Tabuleiro do jogo 
            
        Retorna:

            None
    '''
    
    dim_tabuleiro = len(tabuleiro)
    for lin_contador in range(dim_tabuleiro):
        cols_congeladas = list() 
        for col_contador in range(dim_tabuleiro):
            col_atual = col_contador
            for indice in range(col_contador - 1, -1, -1):
                if tabuleiro[lin_contador][col_atual] == 0:
                    break
                if tabuleiro[lin_contador][indice] == 0:
                    tabuleiro[lin_contador][indice] = tabuleiro[lin_contador][col_atual]
                    tabuleiro[lin_contador][col_atual] = 0
                    col_atual -= 1
                elif tabuleiro[lin_contador][indice] == tabuleiro[lin_contador][col_atual] and indice not in cols_congeladas:
                    tabuleiro[lin_contador][indice] *= 2
                    tabuleiro[lin_contador][col_atual] = 0
                    cols_congeladas.append(indice)
                    break
                else:
                    break
    return None


def direita(tabuleiro):
    '''
        Move os valores de tabuleiro para a direita

        ASSUME QUE o argumento é um tabuleiro válido

        Args:

            tabuleiro (list): Tabuleiro do jogo 
            
        Retorna:

            None
    '''
    
    dim_tabuleiro = len(tabuleiro)
    for lin_contador in range(dim_tabuleiro):
        cols_congeladas = list() 
        for col_contador in range(dim_tabuleiro - 1, -1, -1):
            col_atual = col_contador
            for indice in range(col_contador + 1, dim_tabuleiro):
                if tabuleiro[lin_contador][col_atual] == 0:
                    break
                if tabuleiro[lin_contador][indice] == 0:
                    tabuleiro[lin_contador][indice] = tabuleiro[lin_contador][col_atual]
                    tabuleiro[lin_contador][col_atual] = 0
                    col_atual += 1
                elif tabuleiro[lin_contador][indice] == tabuleiro[lin_contador][col_atual] and indice not in cols_congeladas:
                    tabuleiro[lin_contador][indice] *= 2
                    tabuleiro[lin_contador][col_atual] = 0
                    cols_congeladas.append(indice)
                    break
                else:
                    break
    return None

def cima(tabuleiro):
    '''
        Move os valores do tabuleiro para cima

        ASSUME QUE o tabuleiro é valido: uma matriz 4x4

        Args:

            tabuleiro (list): Tabuleiro do jogo 
            
        Retorna:

            None
    '''
    
    #Cria uma matriz transposta e executa os comandos da esquerda
    tabuleiro[:] = [[tabuleiro[col][linha] for col in range(4)] for linha in range(4)]
    
    for linha in range(4):
        
        #Cria uma lista contendo as linhas onde já ocorreu uma soma
        #A fim de não ocorrerem duas somas consecutivas na mesma linha
        linhas_ja_somadas = list()
        
        for coluna in range(4):

            #Range contendo as linhas que precedem determinada posição
            for indice in range(coluna - 1, -1, -1):
                if tabuleiro[linha][coluna] == 0:
                    break

                if tabuleiro[linha][indice] == 0:
                    tabuleiro[linha][indice] = tabuleiro[linha][coluna]
                    tabuleiro[linha][coluna] = 0
                    coluna-= 1
                              
                elif tabuleiro[linha][indice] == tabuleiro[linha][coluna] and indice not in linhas_ja_somadas:
                    tabuleiro[linha][indice] *= 2
                    tabuleiro[linha][coluna] = 0
                    linhas_ja_somadas.append(indice)
                    break
                else:
                    break

    #Cria a trasnposta novamente, de forma a "desvirar" o tabuleiro
    tabuleiro[:] = [[tabuleiro[col][linha] for col in range(4)] for linha in range(4)]
    return None


def baixo(tabuleiro):
    '''
        Move os valores do tabuleiro para baixo
        
        ASSUME QUE o tabuleiro é valido: uma matriz 4x4

        Args:

            tabuleiro (list): Tabuleiro do jogo 
            
        Retorna:

            None
    '''
    
    #Cria uma matriz transposta e executa os comandos da direita
    tabuleiro[:] = [[tabuleiro[col][linha] for col in range(4)] for linha in range(4)]
    
    for linha in range(4):
        
        #Cria uma lista contendo as linhas onde já ocorreu uma soma
        #A fim de não ocorrerem duas somas consecutivas na mesma linha
        linhas_ja_somadas = list()

        #Range contendo as linhas que precedem determinada posição
        for coluna in range(3, -1, -1):
            
            for indice in range(coluna + 1, 4):
                if tabuleiro[linha][coluna] == 0:
                    break
                if tabuleiro[linha][indice] == 0:
                    tabuleiro[linha][indice] = tabuleiro[linha][coluna]
                    tabuleiro[linha][coluna] = 0
                    coluna+= 1
                elif tabuleiro[linha][indice] == tabuleiro[linha][coluna] and indice not in linhas_ja_somadas:
                    tabuleiro[linha][indice] *= 2
                    tabuleiro[linha][coluna] = 0
                    linhas_ja_somadas.append(indice)
                    break
                else:
                    break

    #Cria a trasnposta novamente, de forma a "desvirar" o tabuleiro
    tabuleiro[:] = [[tabuleiro[col][linha] for col in range(4)] for linha in range(4)]
    return None

def potenciaDeDois():
    """
        Função que cria uma lista de potências de 2 até o 1000
        none -> lista de potencias
        
    """
    potencia = []
    for i in range(0,1000):
        potencia.append(2**i)
    return potencia
        
    
