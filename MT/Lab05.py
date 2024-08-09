#1 - Intercalando Listas
def intercala(L1, L2):
    """
    Recebe duas listas (L1 e L2). Cria uma terceira lista.
    Adiciona em L3, os valores de L1 e L2 de forma intercalada.
    list, list ->  list
    """
    L3 = []
    L3.append(L1[0])
    L3.append(L2[0])
    L3.append(L1[1])
    L3.append(L2[1])
    L3.append(L1[2])
    L3.append(L2[2])
    return L3

#2 - Pontos por Time
def pontos_por_time(informacoes):
    '''
    Recebe a lista com todas as informações dos dois jogos. Essa lista
    contém duas listas no seguinte formato: [T1, T2, [G1, G2]]. Onde:
    T1 e T2 são os times e G1 e G2 são os respectivos gols marcados.
    A função retorna somente os nomes dos times e a pontuação final,
    dada pelos critérios do enunciado (3 pontos para vitória e 1 ponto
    para empate). 
    '''
    PT1 = 0; PT2 = 0
    T1 = informacoes[0][0]; T2 = informacoes[0][1]
	GT1J1 = informacoes[0][2][0]; GT2J1 = informacoes[0][2][1]
	GT1J2 = informacoes[1][2][1]; GT2J2 = informacoes[1][2][0]
    
    if GT1J1 > GT2J1: PT1 = PT1+3
    if GT2J1 > GT1J1: PT2 = PT2+3
    if GT1J2 > GT2J2: PT1 = PT1+3
    if GT2J2 > GT1J2: PT2 = PT2+3
    if GT1J1 == GT2J1: PT1 = PT1+1; PT2 = PT2+1
    if GT1J2 == GT2J2: PT1 = PT1+1; PT2 = PT2+1
        
	return {T1:PT1, T2:PT2}

#3 - Colchão
def colchao(medidas, H, L):
    '''
    A função recebe: lista com as dimensões em ordem crescente e as 
    dimensões da porta (altura e largura). Se duas das dimensões forem
    menor que a porta, então o colchão conseguirá passar rotacionado.
    list, int, int -> bool    
    '''
    A = medidas[0]; B = medidas[1]; C = medidas[2]
    if (A<=H and B<=H) or (A<=L and B<=L): return True
    else: return False
