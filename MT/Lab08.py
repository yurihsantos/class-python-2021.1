#1 - Frequência de Palavras
def freq_palavras(f):
    '''
    Recebe uma frase na string f. Transforma essa frase
    em uma lista l. Abre um dicionário. Verifica se a
    palavra p está contida em l. Posteriormente conta a
    quantidade de vezes que aparece e insere em c.
    E por fim adiciona a chave no dicionário.
    '''
    l = f.split(); d = {}
    for p in l:
        c = l.count(p)
        d[p] = c
    return d

#2 - Compras
def total(l,d):
    '''
    Recebe uma lista e um dicionário. Varre a lista e no
    produto p, verifica o valor dele. Insere esse valor
    no somatório e arredonda para duas casas decimais.
    '''
    s = 0
    for p in l:
        v = d[p]
        s += v
        s = round(s,2)
    return s

#3 - Língua do P
def lingua_p(p):
    '''
    Recebe uma palavra (p) qualquer. Torna-a minúscula.
    Declara uma variável com todas as possíveis vogais.
    [Se tem algum método que ele leia as vogais sem ter
    que declarar todos os acentos possíveis, me informe!]
    Declara uma variável (t) com um texto vazio. Corre todas
 	Corre todas as letras (l) de p e verifica se esta letra
    é uma vogal. Se for, repete o texto até essa letra e
    adiciona o "p" e mais essa mesma letra. Por fim, retorna
    a palavra traduzida (t).
    
    '''
    p = p.lower(); v = "aeiouáéíóú"; t = ''
    for l in p:
        if l in v: t = t+l+'p'+l
        else: t = t+l
    return t

#4 - Divisores
def qtd_divisores(n):
    '''
    Recebe um número (n) qualquer. Inicia o contador (c) 
    com o número 1. E abre a lista dos divisores (d).
    Usa o while: caso o resto da divisão de c por n seja 0,
    então adiciona esse número na lista e soma 1 ao contador.
    Repete o processo até que o contador alcance o valor desejado.
    Feito isso, verifica a quantidade (q) de divisores 
    na lista e retorna essa quantidade.
    '''
    c = 1; d = []
    while c <= n:
        if n%c == 0: d.append(c)
        c += 1
	q = len(d)
    return q

#5 - Números Primos
def primo(n):
    '''
    Usando a questão anterior, apenas verifiquei se a
    quantidade de divisores era igual a 2, sendo estes
    obrigatóriamente o número 1 e ele mesmo.
    '''
    d = qtd_divisores(n)
    if d == 2: return True
    else: return False

#6 - Soma H
def inv(x):
    '''
    Recebe um valor x e retorna o inverso 
    multiplicativo do mesmo, ou seja, eleva a -1.
    '''
    return x**-1

def soma_h(n):
    '''
    Recebe um valor n, atribui um contador k e uma soma s.
    Repete até que k seja igual a n. Ele recebe o inverso
    de k e soma este valor em s. Após isso, soma 1 em k.
    Por fim, arredonda o valor e retorna este valor arredondado.
    '''
    k = 1; s = 0
    while k <= n:
        s += inv(k)
        k += 1
        
    return round(s,2)





















