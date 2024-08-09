# Nome: Yurih Santos de Oliveira
# DRE: 121056855

#1a - Não delete nem modifique esta linha
def CriarContato(Nome, Telefone='',Email='', Instagram=''):
    '''
    Recebe os dados e monta uma lista com todos os dados e uma lista só com o telefone.
    Retorna a lista com todos os dados.
    str, str, str, str ->  list
    '''
    ListaTelefonica = [Telefone]
    Contato = [Nome, ListaTelefonica, Email, Instagram]
    return Contato

#Casos de teste da questão 1a - Não delete nem modifique esta linha

#Dados Informados: 'Yurih', '21985578127', 'yurihsantos@ufrj.br', '@yuriholiveira_'
#Retorno Esperado: ['Yurih', ['21985578127'], 'yurihsantos@ufrj.br', '@yuriholiveira_']
#Retorno Obtido: ['Yurih', ['21985578127'], 'yurihsantos@ufrj.br', '@yuriholiveira_']

#Dados Informados: 'Yurih'
#Retorno Esperado: ['Yurih', [''], '', '']
#Retorno Obtido: ['Yurih', [''], '', '']

#1b - Não delete nem modifique esta linha
def AtualizarContato(Contato, Indice, Dado):
    '''
    Recebe uma lista contendo os dados, o índice para a substituição e o dado para ser alterado.
    Cria uma lista do número de telefone e o dado que quer ser alterado. Caso seja o telefone,
    se o telefone for diferente, concatena as listas. Caso seja qualquer outro índice, será substituído.
    list, int, str -> list
     '''
    Contato[1] = [Contato[1]]
    if Indice == 1 and (Contato[1] != Dado): Dado = [Dado]; Contato[1]+=Dado        
    else: Contato[Indice] = Dado
    return Contato

#Casos de teste da questão 1b - Não delete nem modifique esta linha

#Dados Informados: ['Yurih', '21985578127', 'yurihsantos@ufrj.br', '@yuriholiveira_'], 1, '2138331950'
#Retorno Esperado: ['Yurih', ['21985578127', '2138331950'], 'yurihsantos@ufrj.br', '@yuriholiveira_']
#Retorno Obtido: ['Yurih', ['21985578127', '2138331950'], 'yurihsantos@ufrj.br', '@yuriholiveira_']

#Dados Informados: 'Yurih', '21985578127', 'yurihsantos@ufrj.br', '@yuriholiveira_'], 1, '21985578127'
#Retorno Esperado: ['Yurih', ['21985578127'], 'yurihsantos@ufrj.br', '@yuriholiveira_']
#Retorno Obtido: ['Yurih', ['21985578127'], 'yurihsantos@ufrj.br', '@yuriholiveira_']

#2  - Não delete nem modifique esta linha
def codificacaoRNA(molecula):
    '''
    Recebe a cadeia de RNA, cria um dicionário e faz a devida substituição, retornando a tradução.
    str -> str
    '''
    Trinca = {'UUU':'Phe', 'CUU':'Leu','UUA':'Leu','AAG':'Lisina','UCU':'Ser','UAU':'Tyr', 'CAA':'Gln'}
    
    RNA1 = molecula[0:3]
    RNA2 = molecula[3:6]
    RNA3 = molecula[6:9]

    Amino1 = Trinca[RNA1]
    Amino2 = Trinca[RNA2]
    Amino3 = Trinca[RNA3]
    Aminoacido = Amino1 + '-' + Amino2+  '-'  + Amino3

    return Aminoacido

#Casos de teste da questão 2 - Não delete nem modifique esta linha

#Dados Informados: UUUUUAUCU
#Retorno Esperado: Phe-Leu-Ser
#Retorno Obtido: Phe-Leu-Ser

#Dados Informados: UAUCAAAAG
#Retorno Esperado: Tyr-Gln-Lisina
#Retorno Obtido: Tyr-Gln-Lisina
