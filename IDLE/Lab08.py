# Nome: Yurih Santos de Oliveira
# DRE: 121056855

#1 - Não delete nem modifique esta linha
def qtd_ele(x,k):
  '''
  Recebe um valor iterável qualquer e um possível elemento. A função
  vai verificar quantas vezes o elemento aparece no valor.
  '''
  q = 0
  for n in x:
    if n == k: q += 1
  return q

#Casos de teste da questão 1 - Não delete nem modifique esta linha
'''
>>> qtd_ele('o rato roeu a roupa do rei de roma', 'r')
>>> 5

>>> qtd_ele([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5], 3)
>>>3

>>> qtd_ele((1,2,3),4)
>>>0
'''

#2 - Não delete nem modifique esta linha
def ele_fat(x, k, ini, fim):
  '''
  Recebe um valor iterável qualquer. Analisa a condição de existência
  do fatiamento, ou seja, 0 <= ini e fim <= len(x). Caso não satisfaça
  a condição, será usado o menor valor possível que satisfaça a condição.
  E posteriormente analisa se há o elemento k no item fatiado.
  '''
  t0 = 0; tf = len(x)
  if ini < t0: ini = t0
  if fim > tf: fim = tf

  f = qtd_ele(x[ini:fim], k)
  return f
  

#Casos de teste da questão - Não delete nem modifique esta linha
'''
>>> ele_fat('abcdefghijklmnopqrstuvwxyz', 'i', 5,25)
>>> 1

>>> ele_fat('abcdefghijklmnopqrstuvwxyz', 'i', -5,25)
>>> 1

>>> ele_fat('abcdefghijklmnopqrstuvwxyz', 'i', 15,35)
>>> 0
'''

#3 - Não delete nem modifique esta linha
def atualiza_mascara(palavra, mascara, letra):
  '''
  Recebe uma palavra secreta, uma máscara e uma letra. Verifica se a letra está
  na palavra e se estiver, modifica a máscara no índice que a letra está
  '''
  i = -1
  for l in palavra:
    i += 1
    if l == letra: mascara[i] = letra  

#Casos de teste da questão - Não delete nem modifique esta linha
'''
Coloquei um retorno nos casos de teste para facilitar a visualização dos resultados.

>>> m = ['', '', '', '', '']

>>> atualiza_mascara('carta', m, 'a')
>>>['', 'a', '', '', 'a']

>>> atualiza_mascara('carta', m, 't')
>>> ['', 'a', '', 't', 'a']

>>> atualiza_mascara('carta', m, 'c')
>>> ['c', 'a', '', 't', 'a']
'''

#4a - Não delete nem modifique esta linha
def soma(n):
  '''
  Recebe um valor n e calcula a expressão sigma usando for
  '''
  k = 0; s = 0
  while k <= n:
    e = ((-1)**k)/((2*k)+1)
    s += e; k += 1 
  return s

#Casos de teste da questão - Não delete nem modifique esta linha
'''
>>> soma(0)
>>> 1.0

>>> soma(1)
>>> 0.6666666666666667

>>> soma(10)
>>> 0.8080789523513985
'''

#4b - Não delete nem modifique esta linha
from math import*

def margem_erro():
  '''
  Define n como o enésimo termo da sequência. Define o resultado de n sendo r.
  Define a constante de convergência dada por pi ÷ 4. E por fim define uma margem
  de erro que deve ser menor que 0,01
  '''
  n = 0; r = 0; k = (pi)/4; e = 1
  
  while e>=0.01:
    n += 1
    r = soma(n)
    e = fabs(r - k)
    
  return (n, e)
  




























#Casos de teste da questão - Não delete nem modifique esta linha
'Insira aqui seus testes - Pode deletar esta linha'
