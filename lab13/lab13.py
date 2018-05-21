#!/usr/bin/env python3
#*******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.
def atualizaTabela(tabela, jogo):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
	empate = False
	jogo_dividido = jogo.split()
	if int(jogo_dividido[1]) > int(jogo_dividido[3]): #esquerda ganhou
		vencedor = jogo_dividido[0]
		perdedor = jogo_dividido[4]
		gols_vencedor = int(jogo_dividido[1])
		gols_perdedor = int(jogo_dividido[3])
	elif int(jogo_dividido[1]) < int(jogo_dividido[3]): #direita ganhou
		vencedor = jogo_dividido[4]
		perdedor = jogo_dividido[0]
		gols_vencedor = int(jogo_dividido[3])
		gols_perdedor = int(jogo_dividido[1])
	else: #empatou
		empate = True
		empatante1 = jogo_dividido[0]
		empatante2 = jogo_dividido[4]
		gols_empatante1 = int(jogo_dividido[1])
		gols_empatante2 = int(jogo_dividido[3])
	if empate:
		for linha in tabela:
			if linha[0] == empatante1:
				linha[1] += 1
				linha[2] += 0
				linha[3] += (gols_empatante1 - gols_empatante2)
				linha[4] += gols_empatante1
		for linha in tabela:
			if linha [0] == empatante2:
				linha[1] += 1
				linha[2] += 0
				linha[3] += (gols_empatante2 - gols_empatante1)
				linha[4] += gols_empatante2
	else:
		#att vencedor
		for linha in tabela:
			if linha[0] == vencedor:
				linha[1] += 3
				linha[2] += 1
				linha[3] += (gols_vencedor - gols_perdedor)
				linha[4] += gols_vencedor
		#att perdedor
		for linha in tabela:
			if linha[0] == perdedor:
				linha[1] += 0
				linha[2] += 0
				linha[3] += (gols_perdedor - gols_vencedor)
				linha[4] += gols_perdedor
	#print(tabela)

#*******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
def comparaTimes(time1, time2):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
	for x in range(1,5):
		if time1[x]>time2[x]: return 1
		elif time1[x]<time2[x]: return -1
		else: continue
	return 0
#*******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
	n = len(tabela)
	melhor = {}
	for t in range (n):
		for u in range (n):
			time1 = tabela[t]
			time2 = tabela[u]
			#print(time1, time2, comparaTimes(time1, time2))
			melhor[tabela[t][0]] = melhor.get(tabela[t][0],0) + comparaTimes(time1,time2)
	#print(melhor)
	#print(max(melhor, key=melhor.get))
	nova_tabela = []
	for m in range (len(tabela)):
		for l in range (len(tabela)):
			linha = tabela[l]
			if linha[0] == max(melhor, key=melhor.get):
				show = tabela[l]
				del melhor[max(melhor, key=melhor.get)]
				break
		nova_tabela.append(show)
	for x in range(len(nova_tabela)):
		tabela.pop()
	for x in range(len(nova_tabela)):
		tabela.append(nova_tabela[x])
	#print(nova_tabela)

#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):
#  -- INSIRA SEU CÓDIGO AQUI -- #
#*******************************************************************************
	for tam in range(len(tabela)):
		linha = tabela[tam]
		print("%s, %s, %s, %s, %s" %(linha[0], linha[1], linha[2], linha[3], linha[4]))