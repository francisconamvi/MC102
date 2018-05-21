#!/usr/bin/python3
#Nome: Francisco Namias Vicente
#RA: 216028

def print_RA():
    global data_base
    data_base_print = data_base[:]  #copiando lista para nao comprometer lista original
    for x in range(len(data_base)): data_base_print[x] = str(data_base[x]) #transforma cada RA em strings
    data_base_print = " ".join(data_base_print)  #une a lista de RA's em uma string só
    if data_base_print != "": print(data_base_print+" ") #coloca um espaço no final

def crescente():
    global data_base
    tam = len(data_base)
    #selection sort
    for inic in range (tam-1):
        menor, pos = data_base[inic], inic
        for pont in range(inic,tam):
            if data_base[pont] < menor:
                 menor, pos = data_base[pont], pont
        data_base[inic], data_base[pos] = data_base[pos], data_base[inic]

def decrescente():
    global data_base
    tam = len(data_base)
    #selection sort
    for inic in range (tam-1):
        maior, pos = data_base[inic], inic
        for pont in range(inic,tam):
            if data_base[pont] > maior:
                 maior, pos = data_base[pont], pont
        data_base[inic], data_base[pos] = data_base[pos], data_base[inic]

def busca_bin(ra):
    global data_base
    global mod
    if mod==0:
        print("Vetor nao ordenado!")
        return
    i = 0
    f = len(data_base)-1
    #faz busca binária
    while i<=f:
        m = int(((i+f)/2)//1)
        analise = data_base[m]
        if ra == analise:
            print("%s "%m)
            print("%d esta na posicao: %d"%(ra, m))
            return
        elif ra > analise:
            if data_base[0] < data_base[1]: i = m+1
            else: f = m-1
            print(m, end=" ")
        elif ra < analise:
            if data_base[0] < data_base[1]: f = m-1
            else: i = m+1
            print(m, end=" ")
    print("\n%d nao esta na lista!"%(ra))
    return

def inserir(ra):
    global data_base
    global mod
    if len(data_base)>=150: print("Limite de vagas excedido!")
    elif ra in data_base:
        print("Aluno ja matriculado na turma!")
        return
    else:
        if mod == 0: data_base.append(ra)
        elif mod == 1:
            for pos in range(len(data_base)):
                if ra < data_base[pos]:
                    data_base.insert(pos, ra)
                    return
            data_base.append(ra)
        elif mod == -1:
            for pos in range(len(data_base)):
                if ra > data_base[pos]:
                    data_base.insert(pos, ra)
                    return
            data_base.append(ra)

def remover(ra):
    global data_base
    if len(data_base) == 0:
        print("Nao ha alunos cadastrados na turma!")
        return
    if ra in data_base: data_base.remove(ra)
    else: print("Aluno nao matriculado na turma!")

mod = 0 #mod é a variavel que determina se a funcao está em ordem crescente (1) ou decrescente (-1)
data_base = input()  #base de dados de RAs
data_base = data_base.split()
for x in range(len(data_base)):
    data_base[x] = int(data_base[x]) #transforma todos os RAs em inteiros
while True:
    command = input() #comando do que será feito
    if command == 'p': print_RA() #vai printas listas de RA
    elif command == 'c':  #ordenará em ordem crescente
        crescente()
        mod = 1
    elif command == 'd': #ordenaráem ordem decrescente
        decrescente()
        mod = -1
    elif command[:1] == 'b': busca_bin(int(command[2:])) #fazer buscar binária
    elif command[:1] == 'i': inserir(int(command[2:]))  #inserir RA na lista
    elif command[:1] == 'r': remover(int(command[2:]))  #remover RA da lista
    elif command == 's': quit() #sair do programa
