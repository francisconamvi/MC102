'''
Nome: Francisco Namias Vicente
RA: 216028

O objetivo do programa abaixo é calcular a Média das Provas, quanto a Média do antes Exame e a Média após o Exame,
tudo isso através do valor da P1, P2 e Média dos Laboratórios. Os cálculos feitos estão explicitos em:
http://www.ic.unicamp.br/%7Ebit/mc102/pdd.pdf
'''

P1 = float(input()) #Prova 1
P2 = float(input()) #Prova 2
Ml = float(input()) #Média dos Laboratórios

Mp = (2 * P1 + 3 * P2)/5 #Calculo Média das Provas
print ("%.1f" %Mp)
if (Mp < 5.0 or Ml < 5.0): #Se média das provas ou média dos laboratórios for menor que 5
    M = min(Mp,4.9) #Média antes do Exame será a menor entre a Média das Provas e 4,9
else: #Se média das provas ou média dos laboratórios for maior ou igual a 5
    M = (3 * Mp + 2 * Ml)/5 #Calculo da Média antes do Exame
print ("%.1f" %M)
if (M < 5 and M >= 2.5): #Se média antes do Exame estiver entre 2,5 e 5
    E = float(input()) #Exame
    F = (M + E) / 2 #Cálculo da nota final após exame
else:
    F = M #Cálculo da nota final
print ("%.1f" %F)
