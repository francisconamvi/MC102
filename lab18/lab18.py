import sys

#Abrir os dois arquivos
Img = open(sys.argv[1],"r")
Eft = open(sys.argv[2],"r")

#Ler linhas da primeira entrada e salvar coluna, linha, matriz da imagem
print(Img.readline(), end="")
col, lin = Img.readline().split()
print(col, lin)
print(Img.readline(), end="")
imagem = [Img.readline().split() for x in range(int(lin))]

#Gerar nova matriz que sera a nova imagem
newimage = [[0 for x in range(int(col))] for y in range(int(lin))]

#Ler linhas da segunda entrada e salvar o divisor e matriz de efeito
D = int(Eft.readline())
efeito = [Eft.readline().split() for x in range(3)]

#Fazendo a convulução para pixels dentro da bordar
for x in range(1,int(lin)-1):
    for y in range(1,int(col)-1):
        for nx in [x-1,x,x+1]:
            for ny in [y-1,y,y+1]:
                #print(x,y)
                newimage[x][y] = int(newimage[x][y]) + int(imagem[nx][ny])*int(efeito[nx-x+1][ny-y+1])
        newimage[x][y] = (newimage[x][y])//int(D)
        if newimage[x][y] < 0: newimage[x][y] = 0
        if newimage[x][y] > 255: newimage[x][y] = 255

#Copiando pixels da borda
newimage[0] = imagem[0]
newimage[int(lin)-1] = imagem[int(lin)-1]
for i in range(int(lin)):
    newimage[i][0] = imagem[i][0]
for i in range(int(lin)):
    newimage[i][int(col)-1] = imagem[i][int(col)-1]

for i in range(len(newimage)):
    for j in range(len(newimage[0])):
        print(newimage[i][j], end = " ")
        if j==len(newimage[0])-1 and i != len(newimage)-1 :  print(" ")
        if j==len(newimage[0])-1 and i == len(newimage)-1 :  print(" ", end="")
print("\n", end="")

#Fechando arquivos
Img.close()
Eft.close()
