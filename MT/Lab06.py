#1 - Quantidade de Palavras
def quant_palavras(frase):
    """
    Função que recebe uma frase qualquer. Separa a frase em 
    elementos de uma lista com o termo divisor sendo o espaço.
    Após isso, retorna a quantidade de elementos desta lista.
    Cada elemento é uma palavra da frase.
    str -> int
    """
    return len(frase.split())

#2 - Contar Frases
def conta_frases(f):
    '''
    Ele recebe um conjunto qualquer de frases. Feito isso, ele conta
    todos os possíveis pontos que fazem as separações das frases.
    Recebe e para exclamações; Recebe i para interrogações;
    Recebe r para reticências; Recebe p para pontos e subtrai das
    vezes que ocorreram reticências. Ou seja, se apareceram duas vezes,
    serão 6 pontos que não deverão ser contados. E retorna a soma.
    str -> int
    '''
    e = f.count('!')
    i = f.count('?')
    r = f.count('...')
    p = f.count('.')-(r*3)
    
    return e + i + r + p


#3 - Retira Pontuação
def retira_pontuacao(f):
    '''
    Recebe uma frase em uma string e vai substituindo todos os 
    possíveis casos de pontuação por um espaço simples.
    str -> str
    '''
    
    f = f.replace('-', ' '); f = f.replace(',', ' ')
    f = f.replace(':', ' '); f = f.replace(';', ' ')
    f = f.replace('!', ' '); f = f.replace('?', ' ')
    f = f.replace('.', ' ')
    
    return f

#4 - Inverter
def inverte(f):
    '''
    Recebe uma frase f, retira toda a pontuação dada a função anterior.
    Após isso, torna todas minúsculas, transforma em uma lista dado
    o limitador /espaço/. Inverte a ordem da lista e concatena com os
    espaços com o uso da função join
    str -> str
    '''
    r = retira_pontuacao(f)
    r = r.lower()
    r = r.split(); r = r[::-1]
    r = ' '.join(r)
    return r

#5 - Insere Ordenado
def insere(lista_numero, n):
    '''
    Recebe uma lista numérica qualquer e mais um número n qualquer.
    Insere a lista prévia em uma variável m. Insere o número n 
    em uma lista e esta lista na mesma variável n. Efetua a soma das
    listas e coloca elas em uma variável o. Por conseguinte, organiza
    a lista com a função sort. E retorna a lista organizada.
    list, int -> list
    '''
    m = lista_numero; n = [n]
    o = m + n
    list.sort(o)
    return o

#6 - Maiores
def maiores(l,n):
    '''
    Recebe uma lista l e um número n. Adiciona n nessa lista, depois
    ordena a lista de forma crescente. Pega a posição inicial de n 
    e quantas vezes ele apareceu. Depois deleta todos os números até
    n, ou seja, menores ou iguais a n.
    list, int -> list
    '''
    l.append(n); l.sort()
    k = l.index(n); c = l.count(n)
    del l[0:k+c]	
    return l

#7 - Acima da Média
def acima_da_media(l):
    '''
    Efetua a soma (s) dos argumentos da lista. Mede o tamanho (t)
    da lista. Efetua a média (m). Chama a função maiores e recebe
    o resultado (r). Posteriormente retorna o resultado r.
    list -> list
    '''
    s = sum(l); t = len(l); m = s/t
    r = maiores(l,m)
    return r
