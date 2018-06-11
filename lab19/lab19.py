#Nome: Francisco Namias Vicente
#RA: 216028

def add(lista, num): #funcao que adiciona os numeros na lista no lugar certo, pra nao precisar do sort
    if len(lista) == 0: lista.append(num) #se lista vazia, só adiciona
    elif num < lista[0]: lista.insert(0,num) #se é o menor da lista, adiciona no começo
    elif num > lista[-1]: lista.append(num) #Se é o maior, adiciona no final
    else: #Se nao cumprir nenhuma das acima, procura o intervalo em que é maior que o numeor anterior 
        for i in range(len(lista)): #e menor que o numero posterior
            if num > lista[i] and num < lista[i+1]:
                lista.insert(i+1, num)

def hierarquia(p): #funcao que faz a hierarquia, procurando "pessoas subordinadas" na linha p da matriz
    for x in range(len(matriz[p])):
        if matriz[p][x] == "1":
            add(lista,x)  #adiciona atravez dessa nova funcao implementada
            hierarquia(x) #caso achar, roda novamente a função, pra achar os subordinados do subordinado


n,k = input().split() #n é a ordem da matriz e k é a primeira pessoa analisada
n,k = int(n), int(k)
matriz = [input().split() for x in range(n)]
lista = list()
hierarquia(k) #Roda a função pra achar subordinados
lista.insert(0, k) #Como o k deve ser o primeiro da lista, é adicionado no final 
for x in lista: #printa adequando os espaços após cada ponto
    if x!=lista[-1]: print(x,end=" ")
    else: print(x)
