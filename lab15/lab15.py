#!/usr/bin/env python3

# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    if num in conj: return True
    return False

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    for num in conj1:
        if num not in conj2: return False
    return True

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    if num not in conj: conj.append(num)
    return

def subtracao(conj, num):
    if num in conj: conj.remove(num)
    return

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    newconj = conj1[:]
    for num in conj2:
        if num not in conj1:
            newconj.append(num)
    return newconj

def intersecao(conj1, conj2):   
    newconj = []
    for num in conj1:
        if num in conj2:
            newconj.append(num)
    return newconj

def diferenca(conj1, conj2): 
    newconj = conj1[:]
    for num in conj1:
        if num in conj2:
            newconj.remove(num)
    return newconj

def uniao_disjunta(conj1, conj2):
    newconj = []
    for num in conj1:
        if num not in conj2:
            newconj.append(num)
    for num in conj2:
        if num not in conj1:
            newconj.append(num)
    return newconj
