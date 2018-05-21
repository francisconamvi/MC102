#!/usr/bin/env python3

# Laboratorio 12 - Tetris
# Nome: Francisco Namias Vicente
# RA: 216028

ALTURA_TABULEIRO = 10
LARGURA_TABULEIRO = 10

def atualiza_posicao(l, a, x, desl, rot):
	n_a = a
	n_l = l
	if rot == 1: #se rotacionou, atualiza largura e altura
		n_a = l
		n_l = a
	x = x + desl
	if x < 0: x=0
	if (x + n_l) > 10: x = 10 - n_l
	l = n_l
	a = n_a
	#print(l,a,x)

	return l, a, x 

def encontra_y(mat, l, x):

	linha_bloco = []
	soma = []
	for f in range (10):
		if f < (x+l) and f >= x : linha_bloco.append(1)
		else: linha_bloco.append(0)
	#print(mat) OK
	y = 0
	for n_linha in range(len(mat)-1, -1, -1):
		linha = mat[n_linha]
		#print("n_linha =",n_linha)
		#print("oi", linha)
		if 1 in linha:
			soma = [0 for pao1 in range(len(linha))] #
			for pao1 in range(len(linha)):
				#print(linha[pao1], end="")
				#print(linha_bloco[pao1])
				soma[pao1] = linha[pao1]+linha_bloco[pao1]
				#print(soma[pao1])
			#print(soma)
			if 2 in soma:
				y = n_linha+1
				#print(y)
				return y
	#print(y)
	return y

def posicao_final_valida(a, y):
    # Implementar a funcao e trocar o valor de retorno
	if y + a > 10: 
		#print(0)
		return 0
	else: 
		#print(1)
		return 1 

def posiciona_bloco(mat, l, a, x, y):
	#print(mat)
	matriz_bloco =[[0 for pao2 in range (10)] for pao1 in range(10)]
	for z in range (y,y+a):
		for w in range (x,x+l):
			matriz_bloco[z][w] = 1
	#print(matriz_bloco)
	for pao1 in range(len(mat)):
		for pao2 in range(len(mat[pao1])):
			mat[pao2][pao1] = mat[pao2][pao1]+matriz_bloco[pao2][pao1]
	#mat = mat + matriz_bloco
	#print(mat)

def atualiza_matriz(mat):
	pontos = 0
	p = 0
	for x in range (len(mat)):
		linha = mat[x-p]
		#print(mat)
		#print()
		if 0 not in linha:
			#print(linha)
			mat.remove(linha)
			mat.insert(9,[0 for pao1 in range (10)])
			pontos += 1
			p += 1

	return pontos
