#Nome: Francisco Namias Vicente
#RA: 216028

def removePalavras(s, vs):
    s = s.split() #divide the string into a list
    for x in range(len(vs)): #remove all the words(vs) in s
        while vs[x] in s:
            s.remove(vs[x]) 
    s = " ".join(s) #transform s in a string
    return s

def pagsResposta(palavrasPagina, termosBusca):
    res,zero = [], False
    for x in range(len(palavrasPagina)):
        for y in range(len(termosBusca)):
            if termosBusca[y] not in palavrasPagina[x]:
                res.append(0)
                zero = True
                break
        if zero == False: 
            res.append(1)
        zero = False
    print(res)
    return res
	

#  Funcao: linksResposta
#
# Parametros:
#   links: matriz quadrada binária representando links entre as paginas 
#   resp: lista obtido apos execucao de pagsResposta
#
# Descricao:
#   Deve-se preencher uma lista numLinks da seguinte maneira: para cada
#   posicao i (0 <= i < numPags), se resp[i] == 1, então numLinks[i] deve conter
#   o numero de links de outras paginas resposta para i. Caso resp[i] == 0,
#   entao numLinks[i] deve ser -1.
#
# Retorno
#   lista numLinks a ser preenchida como resposta, de tamanho numPag

def linksResposta(links,resp):
	return []
