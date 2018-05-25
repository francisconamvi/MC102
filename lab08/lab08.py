# RA:216028
# Nome: Francisco Namias Vicente
import string
BdD = []


Nmax = int(input()) #numero de dados colocados
#adicionando cada dado
for dados in range (1,Nmax+1):
    BdD.append(input())

#dividindo cada dado, de forma a transformar em uma matriz
for dados in range (0,Nmax):
    BdD[dados] = str.split(BdD[dados])

#calculando o M, e adicionando à quarta coluna da matriz
for dados in range (0,Nmax):
    M = int(BdD[dados][2]) / int(BdD[dados][1])
    BdD[dados].append(M)

__BdD__  = BdD #BdB servirá para manipulação, a partir de agora
LdM = [] #Lista das Médias. coluna 0 = especie. Coluna 1 = Média
vez = 1
deuruim = False

#print("PRINTANDOOOO", BdD[41])

#Criando Lista das Médias
for dados in range (0,Nmax):
    especie = BdD[dados][0] #especie sendo analisada
    if vez != 1:
        for a in range (0, len(LdM)):
            if especie == LdM[a][0]:
                deuruim = True
    #se especie ja esta na lista, nao faz o resto do for
    if deuruim == True:
        deuruim = False
        continue

    vez = 2
    SoM = BdD[dados][3]
    Me = 1
    if dados+1 == Nmax:
        MeM = SoM/Me
        LdM.append([especie, MeM])
    else:
        for a in range (dados + 1, Nmax):
            if especie == BdD[a][0]:
                SoM = SoM + BdD[a][3]
                Me += 1
            if a == (Nmax-1):
                MeM = SoM/Me
                LdM.append([especie, MeM])
                SoM = 0
                Me = 1

while True:
    cons = input() #consulta
    if cons == "0 0":
        break
    cons = str.split(cons)
    for a in range(0, len(LdM)):
        if cons[0] == LdM[a][0]:
            print((int(int(cons[1]) * float(LdM[a][1])))+1)
