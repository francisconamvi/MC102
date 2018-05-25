'''
Nome: Francisco Namias Vicente
RA: 216028

O objetivo do programa abaixo é controlar o fluxo de veículos em um estacionamento, sendo que inicialmente será informada a capacidade total
e postariormente será informado os valores do veículos que sairam. Véiculos com valor maior que zero são veículos que estão entrando
e veículos com valores negativos são veículos que estão saindo. O módulo do valor é o tamanho do veículo, quanto maior o modulo, maior o
veiculo. Se um veículo quiser entrar e não houver capacidade, este valor não será computado.
'''

C = int(input()) #capacidade total do estacionamento
while True: #loop infinito
    V = int(input()) #veiculo entrou ou saiu
    if (V > 0) and (C >= V): #entrada de veiculo e Capacidade Total é maior ou igual que o veículo
        C = C - V
        print("Seja bem-vindo! Capacidade restante: %d" %C )
    elif (V > 0) and (C < V): #entrada de veiculo e Capacidade Total é menor que o veículo
        print("Veiculo muito grande! Capacidade restante: %d" %C)
    elif V < 0: #saiu veiculo
        C = C - V
        print("Volte sempre! Capacidade restante: %d" %C)
    else:
        break #quebrar loop e finalizar programa
