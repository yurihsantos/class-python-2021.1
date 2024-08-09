## (*) Exercício

def nome():
  return "Yurih Santos de Oliveira"

def dre():
  return "121056855"

def quantas_vezes():
    x = 'x'; y = 'y'; c = 0
    while(x!=y):
        x,y = dados()
        c += 1
    return [(x,y), c]
    
def dados():
    import random
    x = random.randint(1,6)
    y = random.randint(1,6)
    return x,y

#Casos de Teste
'''
>>> quantas_vezes()
[(6, 6), 1]
>>> quantas_vezes()
[(6, 6), 11]
>>> quantas_vezes()
[(3, 3), 1]
>>> quantas_vezes()
[(5, 5), 21]
>>> quantas_vezes()
[(2, 2), 7]
>>> quantas_vezes()
[(3, 3), 8]
>>> quantas_vezes()
[(6, 6), 10]
>>> quantas_vezes()
[(5, 5), 7]
'''
