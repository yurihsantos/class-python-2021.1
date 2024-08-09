def nome():
  """Redija, por gentileza, seu nome na string de retorno."""
  return "Yurih Santos de Oliveira"

def dre():
  """Redija, por gentileza, seu DRE também como uma /string/."""
  return "121056855"


## (*) Questão 2

def mat_vezes_numero(mat, n):
  '''
  Recebe uma matriz qualquer e um número pelo qual a matriz será multiplicada.
  Assim abre uma lista de retorno e copia a matriz inicial para não alterá-la.
  Varre as linhas da matriz e dentro das linhas abre uma lista para colocar os
  produtos de cada linha. Posteriormente varre cada elemento realizando o pro-
  duto. Ao término das multiplicações, joga os resultados para a primeira li-
  nha da lista de retorno e repete o processo.
  '''
  ret = []
  for i in mat:
    l = []
    for j in i:
      l.append(j*n)
    ret.append(l)
  return ret
   
## Casos de Teste

'''
>>> m = [[-0.5, -0.5, -0.5], [-1.0, -1.0, -1.0], [-1.5, -1.5, -0.0]]
>>> mat_vezes_numero(m, -2)
>>> [[1.0, 1.0, 1.0], [2.0, 2.0, 2.0], [3.0, 3.0, 0.0]]

>>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> mat_vezes_numero(m, 11)
>>> [[11, 22, 33], [44, 55, 66], [77, 88, 99]]

>>> mat_vezes_numero([], 10)
>>> []
'''

## (*) Questão 2

def afinidades():
  return \
{
'Leo'    : ['Sofia', 'Andrea', 'Bia'],
'Marcos' : ['Andrea', 'Bia', 'Leo'],
'Sofia'  : ['Leo', 'Marcos'],
'Alex'   : ['Andrea', 'Marcos'],
'Andrea' : ['Marcos'],
'Bia'    : ['Sofia']
}

def deu_match_v1(d):
  '''
  Recebe um dicionário de afinidades. Abre duas listas.
  Verifica os nomes dentro do dicionário e adiciona na
  lista de forma que os flertes apareçam fora do dicionário.

  O segundo for serve para verificar se há algum match inverso,
  ou seja, um match recíproco. Caso haja, insere-o na lista
  de matchs e exclui o match inverso para não entrar na lista.
  '''
  casais = []; matchs = []
  for i in d:
    flertes = d[i]
    for nome in flertes:
      casais.append((i,nome))

  for semi_matchs in casais:
    for semi_matchs2 in casais:
      if semi_matchs == semi_matchs2[::-1]:
        del casais[casais.index(semi_matchs2)]
        matchs.append(semi_matchs)
  return matchs

## (*) Questão 3

def telefones():
  return \
[
['Bruno Campos',['21988881122', '2133992211'], 'b@c.com', '@bruno91'], 
['John Smith',  ['21988883344'], 'j@s.com', '@js92'],
['Bombeiros', ['193'], '', '']
]

def quem_ligou(agenda, tel):
  ret = []
  for contato in agenda:
    if tel in contato[1]:
      ret = contato
  return ret

## (*) Questão 4
##
  
## Renomeie o nome do seu arquivo (que neste momento se chama lab9.py)
## para o nome determinado pelo procedimento meu_arquivo() ---
## execute-o em seu IDLE para saber.

def meu_arquivo():
  ls = ["lab9", str(dre()), str(nome())]
  s1 = str.join(" ", ls)
  s2 = str.replace(s1, " ", "_")
  return s2 + ".py"



















