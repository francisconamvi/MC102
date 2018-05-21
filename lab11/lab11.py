def Main():
	iteracao = 0
	formato = input()
	formato = formato.split()
	linha = int(formato[0])
	coluna = int(formato[1])
	dias= int(input())
	matriz = Gerar_Matriz(linha,coluna)
	matriz_aux = Clonar_Matriz(matriz)
	matriz2str = Juntar_Colunas(matriz_aux)
	Print_Matriz(matriz2str,iteracao)

	for x in range(dias):
		iteracao += 1
		matriz = Transformar_Matriz(matriz,linha,coluna)
		matriz_aux = Clonar_Matriz(matriz)
		matriz2str = Juntar_Colunas(matriz_aux)
		Print_Matriz(matriz2str,iteracao)

def Clonar_Matriz(matriz):
	new_matriz = matriz[:]
	for x in range (len(matriz)):
		new_matriz[x] = matriz[x][:]
	return(new_matriz)

def Juntar_Colunas(matriz):
	for x in range (len(matriz)):
		matriz[x] = "".join(matriz[x])
	return(matriz)

def Print_Matriz(matriz,iteracao):
	print("iteracao %d" %iteracao)
	for x in range(1,len(matriz)-1):
		print(matriz[x][1:-1])

def Gerar_Matriz(linha,coluna):
	matriz = [['0' for x in range(coluna+2)]]
	#print(matriz[-1])
	for x in range(linha):
		matriz.append(input())
		matriz[-1] = matriz[-1].split()
		matriz[-1].insert(0, '0')
		matriz[-1].append('0')
		#print(matriz[-1])
	matriz.append(['0' for x in range(coluna+2)])
	#print(matriz[-1])
	return(matriz)

def Transformar_Matriz(matriz,linha,coluna):
	arredor_elemento = []
	new_matriz = Clonar_Matriz(matriz)
	for i in range(1,linha+1):
		for j in range(1,coluna+1):
			elemento = matriz[i][j]
			#print("Elemento lido:", elemento,"Posicao do Elemento:", i,j)
			arredor_elemento = []
			for k in [i-1, i, i+1]:
				for l in [j-1, j, j+1]:
					if not(k==i and l==j):
						arredor_elemento.append(int(matriz[k][l]))
			#print(arredor_elemento)
			freq = {}
			for termo in arredor_elemento:
				if termo == 1:
					freq["humanos"] = freq.get("humanos",0)+1
				if termo == 2:
					freq["zombies"] = freq.get("zombies",0)+1
			if "humanos" not in freq: freq["humanos"] = freq.get("humanos",0)
			if "zombies" not in freq: freq["zombies"] = freq.get("zombies",0)
			#print("Frequencia =",freq )
			if elemento == '0':
				if freq["humanos"] == 2: new_matriz[i][j] = '1'
			if elemento == '1':
				if freq["zombies"] >= 1: new_matriz[i][j] = '2'
			if elemento == '2':
				if freq["humanos"] >= 2 or freq["humanos"] == 0: new_matriz[i][j] = '0'
			#print("O_matriz =",matriz)
			#print("N_matriz =",new_matriz)
	return(new_matriz)

Main()

#matriz = [ [(2+y)*x for y in range(4)] for x in range(4)]
#print(matriz)