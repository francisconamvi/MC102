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
            if termosBusca[y] not in (palavrasPagina[x]).split(): #if any word from termosBusca isn't at palavrasPagina,
                res.append(0)                                      #add 0 to the list
                zero = True
                break
        if zero == False:  #if there are all words,
            res.append(1)  #add 1
        zero = False
    return res


def linksResposta(links,resp):
    numLinks = [ 0 for i in range(len(resp))]
    for x in range(len(resp)):
        if resp[x] == 0: numLinks[x] = -1 #if "resp" of the page[x] was 0, the out should be -1
        else:
            for i in range(len(resp)):
                if resp[i] != 0: numLinks[x] += links[i][x] #if "resp" of the page[x] was 1, should add every "reference"
    return numLinks
