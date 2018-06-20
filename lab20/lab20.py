#Nome: Francisco Namias Vicente
#RA: 216028
#!/usr/bin/env python3

from lab20_main import print_sudoku

############################################################
# FUNCOES PARA BURILAR AS POSSIBILIDADES DISPONIVEIS       #
# NA ANALISE                                               #
############################################################
#Remove possibilidades na mesma linha
def remove_linha(disponiveis,matriz,i):
    for num in matriz[i]:
        if num in disponiveis:
            disponiveis.remove(num)

#Remove possibilidades na mesma coluna
def remove_coluna(disponiveis,matriz,j):
    for linha in matriz:
        for num in disponiveis:
            if num == linha[j]: disponiveis.remove(num)

#Remove as possivilidades no mesmo "quadrante"(quadrado)
def remove_quadrado(disponiveis,matriz,i,j):
    qx,qy = i//3, j//3
    quadrado = list()
    for x in range(3):
        for y in range(3):
            quadrado.append(matriz[x+3*qx][y+3*qy])
    for num in quadrado:
        if num in disponiveis: disponiveis.remove(num)
############################################################

#Verifica se nao há nenhum zero na matriz
def nenhum_zero(matriz):
    linhas = len(matriz) #Numero de Linhas
    colunas = len(matriz[1]) #Numero de colunas
    for x in range(linhas):
        for y in range(colunas):
            if matriz[x][y]==0: return False #retorna falso se há
    return True #retorna True se nao há

#Analisa as cordenadas x,y da matriz
#Gera os disponiveis para aquela posicao
#E testa cada disponivel, percorrendo a matriz novamente depois disso
def analisa(matriz,x,y):
    disponiveis = [1,2,3,4,5,6,7,8,9] #Todas as possibilidades, até as nao permitidas
    remove_linha(disponiveis,matriz,x) #Tira as repetidas pela linha
    remove_coluna(disponiveis,matriz,y) #Tira as repetidas pela coluna
    remove_quadrado(disponiveis,matriz,x,y) #Tira as repetidas pelo quadrado
    #Aqui eu tenho disponiveis com todas as possibilidades possiveis
    
    if disponiveis == list(): #Se nao houver disponiveis, return e testa o proximo teste da coordenada anterior
        return

    for teste in disponiveis:
        if nenhum_zero(matriz): return #Se matriz ja estiver completa, nao mexer nela
        matriz[x][y] = teste #coloca o teste na cordenada
        percorre(matriz) #percorre de novo
    if nenhum_zero(matriz): return #Se matriz ja estiver completa, nao mexe
    matriz[x][y] = 0 #Se nao estiver completa, zera aquela posição a faz novos testes
    return

#Percorre a matriz completa, procurando 0's.
def percorre(matriz):
    linhas = len(matriz) #Numero de Linhas
    colunas = len(matriz[1]) #Numero de colunas
    for x in range(linhas):
        for y in range(colunas):
            if matriz[x][y] != 0: continue #Se for diferente de 0, ta no caminho certo
            else:
                analisa(matriz,x,y) #Se for igual a 0, analisa essa cordenada porque tem que colocar algum numero
                return
#Funcao para resolver Sudoko
def resolve(resposta):
    percorre(resposta) #Percorre a resposta, do inicio ao fim 
    print_sudoku(resposta)
    return True
