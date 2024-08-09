#1 - Positivo, Negativo ou Zero
def PosNegZero(x):
    x = int(x)
    """int --> str"""
    if x > 0:
        return str(x) + " e positivo"
    elif x == 0:
        return str(x) + " e zero"
    else:
        return str(x) + " e negativo"

#2 - Futebol
def classificacao(cv, ce, cs, fv, fe, fs):
    PtC = (cv*3)+ce
    PtF = (fv*3)+fe

    if PtC == PtF:
        if cs == fs:
            return "Empate"
        elif cs > fs:
            return "Cormengo"
        else:
            return "Flaminthians"
        
    elif PtC > PtF:
        return "Cormengo"
    else:
        return "Flaminthians"

#3 - Aviões de Papel
def avioes(c, p_compr, p_compet):
    papelnecessario = c*p_compet
    if p_compr >= papelnecessario:
        return "Suficiente"
    else:
        return "Insuficiente"
