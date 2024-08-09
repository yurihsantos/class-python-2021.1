# Nome: Yurih Santos de Oliveira
# DRE: 121056855

#1a - Não delete nem modifique esta linha
def excluir(contato, tel_apagar):
    telefones = contato[1]
    if tel_apagar in telefones:
        indexescolhido = telefones.index(tel_apagar)
        del telefones[indexescolhido]
        return True
    else:
        return False

#Casos de teste da questão 1a - Não delete nem modifique esta linha
'Insira aqui seus testes - Pode deletar esta linha'

#2 - Não delete nem modifique esta linha
dados = [{'Flamengo': 10}, {'Vasco': 8}, {'Fluminense': 16}, {'São Paulo': 4}, {'Botafogo': 2}, {'Criciúma': 0}]

def times(listagem):
    nomes = []; ponto = []

    for i in listagem:
        for j in i:
            nomes.append(j)
            ponto.append(i[j])

    ponto_max = max(ponto)
    time_venc = nomes[ponto.index(ponto_max)]

    soma = sum(ponto)
    qtde = len(nomes)
    media = soma / qtde

    return {'Time campeão': time_venc,
            'Média de pontuação': media,
            'Times': nomes}      
        
'''
#Casos de teste da questão 1b - Não delete nem modifique esta linha
