# RA:216028
# Nome: Francisco Namias Vicente

n = 0
tam = int(input())

for linha in range(1, tam+1):
    for coluna in range(1, tam+1):
        if linha/coluna == linha//coluna or coluna/linha == coluna//linha:
            print ("*", end="")
            n += 1
        else:
            print ("-", end="")
    #if linha != tam:
    print()
print(n)
