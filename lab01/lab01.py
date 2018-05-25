#Nome:Francisco Namias Vicente
#RA: 216028

# O objetivo é, com a distancia de uma cidade à outra em estadios e com o angulo formado
#entre a estaca e a hipotenusa até o final da sombra, calcular a circunferencia da Terra,
#tanto em estadios, como em kilometros.

#ENTRADAS
D = float(input()) #distancia em estadios
A = float(input()) #angulo

R = 360 / A #relação
Ce = D * R  #Circunferencia em estadios
Ckm = Ce * 0.1764

#SAIDAS
print("%.1f" %Ce)
print("%.1f" %Ckm)
