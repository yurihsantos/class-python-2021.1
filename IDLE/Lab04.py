# Nome: Yurih Santos de Oliveira
# DRE: 121056855

#1  - Não delete nem modifique esta linha
def SIGA(nome, nota1, nota2, nota3):
    '''Recebe o nome e as 3 notas e retorna uma tupla com o nome, a situação e uma mensagem.
    Recebe o nome entre aspas. | str, int, int, int - > tupla(str, float, str)'''
    media = (nota1 + nota2 + nota3)/3
    if media >= 7:
        return (nome, media, "Aprovado", "Parabéns")
    elif media >=5:
        return (nome, media, "Aprovado")
    else:
        return (nome, media, "Reprovado")
    
#Casos de teste da questão 1 - Não delete nem modifique esta linha
'''Valor Recebido: Yurih, 7,3,5
Valor Esperado: (Yurih, 5.0, Aprovado)
Valor Retornado: (Yurih, 5.0, Aprovado)'''


#2  - Não delete nem modifique esta linha
def zodiaco(ano):
     '''Recebe o ano de nascimento e retorna o signo chinês correspondente'''
     resto = ano % 12
     animais = ('Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro')
     return animais[resto]

#Casos de teste da questão 2 - Não delete nem modifique esta linha
'''
Valor Recebido: 2002
Valor Esperado: Cavalo
Valor Retornado: Cavalo
'''

#3  - Não delete nem modifique esta linha
def telefone(numero):
    '''Recebe o número de telefone. Verifica se está entre os tipos telefônicos
    válidos e retorna uma tupla com DDD e o número |str -> tupla'''
    numero = str(numero)
    if len(numero)==8 or len(numero)==9:
        return ("",numero)    
    elif len(numero)==10 or len(numero)==11:
        return (numero[0:2],numero[2:len(numero)])
    else:
        return ("", "")

#Casos de teste da questão 1 - Não delete nem modifique esta linha
'''
Valor Recebido: 21985578127
Valor Esperado: (21, 985578127)
Valor Retornado: (21, 985578127)
'''

#4  - Não delete nem modifique esta linha
def formatacao(data):
    '''Recebe as datas em formato cronológico (xx/yy/zz). Portanto, use as barras para sinalizar.
    Ele irá apontar todas as formas possíveis para organizar essa data | str -> tuple'''
    data = str(data)
    xx = int(data[0:2]) 
    yy = int(data[3:5]) 
    zz = int(data[6:])
    lista = []

    if 0 < xx <= 31 and 0 < yy <= 12: lista.append('dd/mm/yy')
    if (0 < xx <= 12 and 0 < zz <= 31) or (0 < yy <= 31 and 0 < xx <= 12): lista.append('mm/dd/yy')
    if 0 < yy <= 12 and 0 < zz <= 31: lista.append('yy/mm/dd')
    return tuple(lista)

#Casos de teste da questão 4 - Não delete nem modifique esta linha
'''
Valor Recebido: "12/08/02"
Valor Esperado: ('dd/mm/yy', 'mm/dd/yy', 'yy/mm/dd')
Valor Retornado: ('dd/mm/yy', 'mm/dd/yy', 'yy/mm/dd')
'''
