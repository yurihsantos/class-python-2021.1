#1 - Concatenação
def concatenacao(a, b):
    '''
    Recebe dois valores (a,b) e concatena no formato abba.
    str, str -> str
    '''
    return a + b + b + a

#2 - Substituição
def substitui(s,x,i):
    '''
    Recebe uma palavra s, uma letra x e um número i.
    Pega a posição (i) da letra que eu quero substituir.
    Quebra a palavra em antes e depois da posição i.
    Concatena o que está antes de i e depois de i.
    Retorna o resultado. 
    str, str, int -> str
    '''
    w = s[0:i]
    y = s[i+1:len(s)]
    return w+x+y
    
#3 - Hashtag
def hashtag(s):
    '''
    Recebe uma variável s com x caracteres.
    Calcula o valor da metade do tamanho da string (m)
    Recebe os valores do começo ao meio (c).
    Recebe os valores do meio ao fim (f).
    Guarda o simbolo "#" que se quer colocar (s) 
    Retorna a concatenação s + c + s + f + s
    str -> srt
    '''
    m = len(s)//2
    c = s[0:m]
    f = s[m:len(s)]
    s = "#"
    return s+c+s+f+s
    
#4 - Filtrar Pares
def filtra_pares(v):
    '''
    Recebe uma tupla com 4 valores inteiros determinados.
    Abre quatro tuplas vazias. Adiciona os valores 
    na ordem, caso eles sejam considerados pares.
    tuple -> tuple
    '''
    a = (); b = (); c = (); d = ()
    
    if v[0] % 2 == 0: a = (v[0],)
    if v[1] % 2 == 0: b = (v[1],)
    if v[2] % 2 == 0: c = (v[2],)
    if v[3] % 2 == 0: d = (v[3],)
    
    return a+b+c+d

#5 - Detectando Colisões
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''

    XIE1, YIE1, XSD1, YSD1 = ret1
    XIE2, YIE2, XSD2, YSD2 = ret2

    if ((XSD1<XIE2) or (YSD2<YIE1)): return False
    else: return True
  
