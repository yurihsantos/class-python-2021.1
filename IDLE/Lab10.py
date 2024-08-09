# Nome: Yurih Santos de Oliveira
# DRE: 121056855

#1 - Não delete nem modifique esta linha
def series(lancamentos):
  '''
  Recebe a lista com os lançamentos dos dados. Inicia as variáveis de cálculo.
  i para index; t para tamanho da lista; k para o contador; s para o somatório
  das sequências. Enquanto o índice for menor que o tamanho, vai verificar se o
  número de índice i é igual ao posterior. Caso seja, enquanto for igual, vai
  realizar a contagem. Se for igual 3 vezes, vai somar 3 ao contador e 3 ao índi-
  ce (para não passar mais por esses números. Se o contador for diferente de 0,
  é pq existe uma sequência. Então zera o contador e soma 1 a variável de sequên-
  cias. Caso não seja igual ao posterior, avança de índice na lista e retorna a soma.
  '''
  i = 0; t = len(lancamentos)-1; k = 0; s = 0

  while i < t:
    if lancamentos[i] == lancamentos[i+1]:
      while lancamentos[i] == lancamentos[i+1]:
        k += 1; i += 1
        if i >= t: break
      if k != 0: k = 0; s += 1
    else: i += 1
  return s


#Casos de teste da questão 1 - Não delete nem modifique esta linha
'Insira aqui seus testes - Pode deletar esta linha'

#2 - Não delete nem modifique esta linha
def valores(i,a,b,c):
  '''
  Recebe 4 valores inteiros positivos. Sendo 1 <= i <= 4, ou seja i ∈ [1,2,3,4].
  E também recebe outros 3 valores (a,b,c) inteiros positivos sendo a < b.
  '''

  if i == 1: x = caso1(a,b,c)
  if i == 2: x = caso2(a,b,c)
  if i == 3: x = caso3(a,b,c)
  if i == 4: x = caso4(a,b,c)
  return x
  
def caso1(a,b,c):
  area = ((b+a)*c)/2
  return area

def caso2(a,b,c):
  quad_a = a * a
  quad_b = b * b
  quad_c = c * c

  return {a:quad_a, b:quad_b, c:quad_c}

def caso3(a,b,c):
  media = (a+b+c)/3
  return (a,b,c, media)

def caso4(a,b,c):
  s = a; ls = [s]
  while s <= b:
    if (s+c) > b: return sum(ls)
    else: s += c; ls.append(s)


#Casos de teste da questão - Não delete nem modifique esta linha
'''
>>> valores(1,3,13,2)
>>> 16.0

>>> valores(2,3,13,2)
>>> {3: 9, 13: 169, 2: 4}

>>> valores(3,3,13,2)
>>> (3, 13, 2, 6.0)

>>> valores(4,3,13,2)
>>> 48
'''

#3 - Não delete nem modifique esta linha
def matriz():
  return \
[
['Adalberto Ferreira',   '010919820', 'Contabilidade',    '(21)99281 − 2983'],
['Juliana Vasconcelos',  '011117220', 'Recursos Humanos', '(21)99848 − 1902'],
['Flavia Amorim',        '011289380', 'Contabilidade',    '(22)99273 − 9404'],
]

def lista_funcionarios():
  '''
  Pergunta ao usuário quantos usuários ele quer cadastrar. Em seguida ele pergunta
  ao usuário cada dado necessário (nome, registro, setor e telefone). Faz isso em
  todas as linhas até que se tenha chegado ao número fornecido. No fim, retorna
  a lista total de funcionários.
  '''
  funcionarios = []; linha = 1
  quantidade = int(input('Insira quantos funcionários quer cadastrar: '))

  while linha <= quantidade:
    ls = []
    ls.append(input('Insira o nome do ' + str(linha) + 'º funcionário:     '))
    ls.append(input('Insira o registro do ' + str(linha) + 'º funcionário: '))
    ls.append(input('Insira o setor do ' + str(linha) + 'º funcionário:    '))
    ls.append(input('Insira o telefone do ' + str(linha) + 'º funcionário: '))
    print('-------------------------------------------')
    funcionarios.append(ls); linha += 1
  return funcionarios

def busca_setor(matriz, setor):
  busca = []
  for funcionario in matriz:
    if funcionario[2] == setor: busca.append(funcionario)
    
  if busca == []: return 'Nenhum registro encontrado'
  if busca != []: return busca


#Casos de teste da questão - Não delete nem modifique esta linha
'''
Como já fizemos o exercício anteriormente, não julguei necessário os casos de
teste da função busca_setor. O foco aqui é na função lista_funcionarios.
Tanto é assim que foi a única função da questão 3 que está documentada.
Coloquei os prints dessas linhas de hífens pois deixam o texto impresso na tela
bem menos massivo. Poderia fazer uma quebra de página também, mas preferi isto.
A função matriz foi só pra guardar os dados para me auxiliar no momento do trabalho.


>>> lista_funcionarios()
Insira quantos funcionários quer cadastrar: 5
Insira o nome do 1º funcionário: 11
Insira o registro do 1º funcionário: 12
Insira o setor do 1º funcionário: 13
Insira o telefone do 1º funcionário: 14
-------------------------------------------
Insira o nome do 2º funcionário: 21
Insira o registro do 2º funcionário: 22
Insira o setor do 2º funcionário: 23
Insira o telefone do 2º funcionário: 24
-------------------------------------------
Insira o nome do 3º funcionário: 31
Insira o registro do 3º funcionário: 32
Insira o setor do 3º funcionário: 33
Insira o telefone do 3º funcionário: 34
-------------------------------------------
Insira o nome do 4º funcionário: 41
Insira o registro do 4º funcionário: 42
Insira o setor do 4º funcionário: 43
Insira o telefone do 4º funcionário: 44
-------------------------------------------
Insira o nome do 5º funcionário: 51
Insira o registro do 5º funcionário: 52
Insira o setor do 5º funcionário: 53
Insira o telefone do 5º funcionário: 54
-------------------------------------------
[['11', '12', '13', '14'], ['21', '22', '23', '24'], ['31', '32', '33', '34'], ['41', '42', '43', '44'], ['51', '52', '53', '54']]
'''
