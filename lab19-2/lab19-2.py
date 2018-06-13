#Nome: Francisco Namias Vicente
#Ra: 216028

#Numero de Linhas e Colunas em cada tabuleiro 
L,C = input().split('x')
L,C = int(L), int(C)

#funcao que verifica se tabuleiro está não vazio(com navios) ou vazio (só '-')
def tab_nao_vazio(tab):
    for l in range(L):
        if '@' in tab[l]: return True
    else: return False
    
#função ataca o ponto e se houver navios, destoi aquele ponto e faz a varredura em volta,
#destruindo o navio inteiro
def destruir(tab,x,y):
    x,y = x-1,y-1 #lista começa no 0, mas tabuleiro começa no 1
    if tab[x][y] == "@":
        tab[x][y] = "-"
        for nx in [x-1,x,x+1]:
            if nx < 0: continue #previnir erros
            elif nx >= L: continue #previnir erros
            if tab[nx][y] == "@": destruir(tab,nx+1,y+1)
        for ny in [y-1,y,y+1]:
            if ny < 0: continue #previnir erros
            elif ny >= C: continue #previnir erros
            if tab[x][ny] == "@": destruir(tab,x+1,ny+1)

#Função que printa o tabuleiro da forma requisitada 
def print_tabuleiro(tab):
    for i in range(L):
        for j in range(C): 
            print(tab[i][j], end="")
        print()

tab1 = [list(input()) for i in range(L)] #tabuleiro do jogador 1
tab2 = [list(input()) for i in range(L)] #tabuleiro do jogador 2

while tab_nao_vazio(tab1):
    x,y = input().split(',') #coordenadas do ataque
    x,y = int(x), int(y)
    print("Ataque em (%d,%d) do jogador 1" %(x,y))
    destruir(tab2,x,y)
    print_tabuleiro(tab2)
    if tab_nao_vazio(tab2): pass
    else: break
    x,y = input().split(',')
    x,y = int(x), int(y)
    print("Ataque em (%d,%d) do jogador 2" %(x,y))
    destruir(tab1,x,y)
    print_tabuleiro(tab1)
