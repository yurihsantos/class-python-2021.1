# 1 - Matriz Quadrada
def eh_quadrada(matriz):
    '''
    Recebe uma lista de listas. 
    Se não houver colunas, será quadrada (e vazia);
    Se nº colunas for igual ao nº linhas, será quadrada;
    Se nº colunas diferir do nº linhas, não será quadrada.    
    '''
    if len(matriz) == 0: return True
    if len(matriz) == len(matriz[0]): return True
    if len(matriz) != len(matriz[0]): return False

# 2 - Buscando na Matriz
def conta_numero(n, matriz):
    '''
    Inicia um contador. Varre as listas da matriz e
    verifica se nestas listas existe o elemento pedido.
    Caso exista, ele entra pra conta e retorna a soma.
    '''
    k = 0
    for x in matriz:
        k += x.count(n)

    return k

# 3 - Média da Matriz
def media_matriz(matriz):
    '''
    Inicia 3 variáveis: uma pra soma (s), outra para 
    média (m) e outra para contagem de elementos (k).
    Varre as linhas e depois varre as colunas, analisando
        cada elemento. Ele soma todos os elementos em s e soma
    um elemento em k. Depois efetua a média e arredonda.
    '''
    s = 0
    m = 0
    k = 0
    for i in matriz:
        for j in i:
            s += j
            k += 1
    m = s/k
    m = round(m, 2)
    return m

# 4 - Melhor Volta
def melhor_volta(matriz):
    '''
    Abre duas listas vazias para os melhores tempos
    e melhores corredores. Varre a matriz inicial e
    procura o melhor tempo do corredor (x) e a corrida 
    do melhor tempo (y). Posteriormente adiciona esses
    valores em listas de melhores tempos e suas respec-
    tivas corridas.

    Pega o menor tempo e coloca na variável de melhor 
    tempo (MT); Pega a posição do melhor tempo para achar
    a melhor volta e insere em MV; Pega a posição do melhor
    corredor em função do melhor tempo e acha a melhor corrida.

    Feito isso, retorna a tupla com os valores pedidos
    e uma soma (+1) para fins de compensação do índice.    
    '''
    LT = []
    LC = []
    for i in matriz:
        x = min(i)
        y = i.index(x)
        LT.append(x)
        LC.append(y)

    MT = min(LT)
    MV = LT.index(MT)
    MC = LC[MV]
    return (MV + 1, MT, MC + 1)

# 5 - Busca de Funcionários
def busca(setor, matriz):
    '''
    Inicia uma lista vazia e tira uma cópia da matriz inicial
    para não apagar os dados originais. Varre as sub listas
    de M e verifica se a coluna "setor" corresponde ao setor
    pedido. Caso sim, exclui essa coluna e insere a sub lista
    modificada na nova lista. Depois retorna a nova lista.
    '''
    L = []
    M = matriz.copy()

    for x in M:
        if x[2] == setor:
            del x[2]
            L.append(x)
        return L