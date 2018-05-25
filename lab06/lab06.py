'''
Nome: Francisco Namias Vicente
RA: 216028

O objetivo do programa abaixo é controlar o fluxo de veículos em um estacionamento, sendo que inicialmente será informada a capacidade total
e postariormente será informado os valores do veículos que sairam. Véiculos com valor maior que zero são veículos que estão entrando
e veículos com valores negativos são veículos que estão saindo. O módulo do valor é o tamanho do veículo, quanto maior o modulo, maior o
veiculo. Se um veículo quiser entrar e não houver capacidade, este valor não será computado.
'''

from math import sqrt

#Funções
def propriedade(num):
    negativo = False
    if num < 0:
        num = num * -1
        negativo = True
    def triang(num):
        n = (-1 + sqrt(1+8*num))/2
        if (n - n//1) == 0:
            num = num * 2
        return(num)

    def perfeito(num):
        x = 0
        for a in range(1, (num//2) + 1):
            r = num / a
            if (r - r//1) == 0:  #a é um divisor
                x = x + a
        if num == x:
            num = num * 3
        return (num)

    if num != perfeito(num):
        num = perfeito(num)
    else:
        num = triang(num)
    if negativo == True:
        num = num * -1
    return(num)



#Eu sou o Ryu
HP_Ryu = Flag_HP_Ryu = 2000
HP_Ken = Flag_HP_Ken =  2000
seq_apanhei = 0
seq_bati = 0
apanhei = 2
R = K = 0

while (Flag_HP_Ryu > 0 and Flag_HP_Ken > 0):
    acao = propriedade(int(input()))


    #parte que cuida de acabar com o jogo
    if acao < 0:
        Flag_HP_Ryu = Flag_HP_Ryu + acao
    else:
        Flag_HP_Ken = Flag_HP_Ken - acao

    #parte que cuida dos prints
    if acao < 0: #Ryu apanhando
        if apanhei == 1: #continuando sequencia
            seq_apanhei = seq_apanhei + -1*acao #soma acao à sequencia
        else: #nova sequencia
            if apanhei != 2: #nao é a primeira entrada
                Novo_HP_Ken = HP_Ken - seq_bati #atualiza HP Ken
                print ("Ken: %d - %d = %d" %(HP_Ken, seq_bati, Novo_HP_Ken))
                HP_Ken = Novo_HP_Ken
            seq_apanhei = 0 #zera a sequencia 
            seq_apanhei = seq_apanhei + -1*acao #soma acao à sequencia
        apanhei = 1

    elif acao > 0: #Ryu batendo
        if apanhei == 0: #continuando sequencia
            seq_bati = seq_bati + acao
        else: #nova sequencia
            if apanhei != 2: #nao é a primeira vez
                Novo_HP_Ryu = HP_Ryu - seq_apanhei #atualiza HP Ryu
                print ("Ryu: %d - %d = %d" %(HP_Ryu, seq_apanhei, Novo_HP_Ryu))
                HP_Ryu = Novo_HP_Ryu
            seq_bati = 0
            seq_bati = seq_bati + acao
        apanhei = 0

if Flag_HP_Ken <= 0: #Ryu ganhou
    Novo_HP_Ken = HP_Ken - seq_bati #atualiza HP Ken
    print ("Ken: %d - %d = %d" %(HP_Ken, seq_bati, Novo_HP_Ken))
    R += 1
elif Flag_HP_Ryu <= 0: #Ken ganhou
    Novo_HP_Ryu = HP_Ryu - seq_apanhei #atualiza HP Ryu
    print ("Ryu: %d - %d = %d" %(HP_Ryu, seq_apanhei, Novo_HP_Ryu))
    K += 1

#---------------------------------------------------------------------------------------#

HP_Ryu = Flag_HP_Ryu = 2000
HP_Ken = Flag_HP_Ken =  2000
seq_apanhei = 0
seq_bati = 0
apanhei = 2

while (Flag_HP_Ryu > 0 and Flag_HP_Ken > 0):
    acao = propriedade(int(input()))

    #parte que cuida de acabar com o jogo
    if acao < 0:
        Flag_HP_Ryu = Flag_HP_Ryu + acao
    else:
        Flag_HP_Ken = Flag_HP_Ken - acao

    #parte que cuida dos prints
    if acao < 0: #Ryu apanhando
        if apanhei == 1: #continuando sequencia
            seq_apanhei = seq_apanhei + -1*acao #soma acao à sequencia
        else: #nova sequencia
            if apanhei != 2: #nao é a primeira entrada
                Novo_HP_Ken = HP_Ken - seq_bati #atualiza HP Ken
                print ("Ken: %d - %d = %d" %(HP_Ken, seq_bati, Novo_HP_Ken))
                HP_Ken = Novo_HP_Ken
            seq_apanhei = 0 #zera a sequencia 
            seq_apanhei = seq_apanhei + -1*acao #soma acao à sequencia
        apanhei = 1

    elif acao > 0: #Ryu batendo
        if apanhei == 0: #continuando sequencia
            seq_bati = seq_bati + acao
        else: #nova sequencia
            if apanhei != 2: #nao é a primeira vez
                Novo_HP_Ryu = HP_Ryu - seq_apanhei #atualiza HP Ryu
                print ("Ryu: %d - %d = %d" %(HP_Ryu, seq_apanhei, Novo_HP_Ryu))
                HP_Ryu = Novo_HP_Ryu
            seq_bati = 0
            seq_bati = seq_bati + acao
        apanhei = 0

if Flag_HP_Ken <= 0: #Ryu ganhou
    Novo_HP_Ken = HP_Ken - seq_bati #atualiza HP Ken
    print ("Ken: %d - %d = %d" %(HP_Ken, seq_bati, Novo_HP_Ken))
    R += 1
elif Flag_HP_Ryu <= 0: #Ken ganhou
    Novo_HP_Ryu = HP_Ryu - seq_apanhei #atualiza HP Ryu
    print ("Ryu: %d - %d = %d" %(HP_Ryu, seq_apanhei, Novo_HP_Ryu))
    K += 1

if K > R:
    print("Ken venceu")
elif R > K:
    print("Ryu venceu")
else:
    print("empatou")