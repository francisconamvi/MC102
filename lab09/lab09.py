#Nome: Francisco Namias Vicente // RA: 216028

max_LT = max_ac = max_av = max_bc = max_bv = max_cc = max_cv = max_dc = max_dv = 0
emp = [[0], [0], [0], [0]]

d = int(input()) #dias de business
#lista de empresas com valor de cada dia
for i in range (len(emp)):
    for a in range(d):
        valor = float(input())
        emp[i].append(valor)

#geração de possibilidade de compras e tratamento de impossibilidades
for ac in emp[0][0:len(emp[0])-1]:
	for bc in emp[1][0:len(emp[1])-1]:
		if (emp[1].index(bc) == emp[0].index(ac)) and (emp[1].index(bc) != 0): continue
		for cc in emp[2][0:len(emp[2])-1]:
			if ((emp[2].index(cc) == emp[1].index(bc)) or (emp[2].index(cc) == emp[0].index(ac))) and (emp[2].index(cc) != 0): continue
			for dc in emp[3][0:len(emp[3])-1]:
				if ((emp[3].index(dc) == emp[2].index(cc)) or (emp[3].index(dc) == emp[1].index(bc)) or (emp[3].index(dc) == emp[0].index(ac))) and (emp[3].index(dc) != 0): continue

				#geração de possibilidade de vendas e tratamento de impossibilidades
				for av in emp[0][(emp[0].index(ac)):]:
					if (emp[0].index(ac) == emp[0].index(av) and av!=0): continue
					elif (av-ac) < 0: continue
					elif av != 0 and ac == 0: continue
					for bv in emp[1][(emp[1].index(bc)):]:
						if (emp[1].index(bc) == emp[1].index(bv) and bv!=0): continue
						elif (bv-bc) < 0: continue
						elif bv != 0 and bc == 0: continue
						elif (emp[1].index(bv) == emp[0].index(av)) and (emp[1].index(bv) != 0): continue
						elif (emp[1].index(bc) > emp[0].index(ac)) and (emp[1].index(bv) < emp[0].index(av)): continue
						elif (emp[1].index(bc) < emp[0].index(ac)) and (emp[1].index(bv) > emp[0].index(av)): continue
						elif (emp[1].index(bc) > emp[0].index(ac)) and (emp[1].index(bc) < emp[0].index(av)): continue
						elif (emp[1].index(bv) > emp[0].index(ac)) and (emp[1].index(bv) < emp[0].index(av)): continue
						for cv in emp[2][(emp[2].index(cc)):]:
							if (emp[2].index(cc) == emp[2].index(cv) and cv!=0): continue
							elif (cv-cc) < 0: continue
							elif cv != 0 and cc == 0: continue
							elif ((emp[2].index(cv) == emp[1].index(bv)) or (emp[2].index(cv) == emp[0].index(av))) and (emp[2].index(cv) != 0): continue
							elif (emp[2].index(cc) > emp[1].index(bc)) and (emp[2].index(cv) < emp[1].index(bv)): continue
							elif (emp[2].index(cc) < emp[1].index(bc)) and (emp[2].index(cv) > emp[1].index(bv)): continue
							elif (emp[2].index(cc) > emp[0].index(ac)) and (emp[2].index(cv) < emp[0].index(av)): continue
							elif (emp[2].index(cc) < emp[0].index(ac)) and (emp[2].index(cv) > emp[0].index(av)): continue
							elif (emp[2].index(cc) > emp[1].index(bc)) and (emp[2].index(cc) < emp[1].index(bv)): continue
							elif (emp[2].index(cv) > emp[1].index(bc)) and (emp[2].index(cv) < emp[1].index(bv)): continue
							elif (emp[2].index(cc) > emp[0].index(ac)) and (emp[2].index(cc) < emp[0].index(av)): continue
							elif (emp[2].index(cv) > emp[0].index(ac)) and (emp[2].index(cv) < emp[0].index(av)): continue
							for dv in emp[3][(emp[3].index(dc)):]:
								if (emp[3].index(dc) == emp[3].index(dv) and dv!=0): continue
								elif (dv-dc) < 0: continue
								elif dv != 0 and dc == 0: continue
								elif ((emp[3].index(dv) == emp[2].index(cv)) or (emp[3].index(dv) == emp[1].index(bv)) or (emp[3].index(dv) == emp[0].index(av))) and (emp[3].index(dv) != 0): continue
								elif (emp[3].index(dc) > emp[2].index(cc)) and (emp[3].index(dv) < emp[2].index(cv)): continue
								elif (emp[3].index(dc) < emp[2].index(cc)) and (emp[3].index(dv) > emp[2].index(cv)): continue
								elif (emp[3].index(dc) > emp[1].index(bc)) and (emp[3].index(dv) < emp[1].index(bv)): continue
								elif (emp[3].index(dc) < emp[1].index(bc)) and (emp[3].index(dv) > emp[1].index(bv)): continue
								elif (emp[3].index(dc) > emp[0].index(ac)) and (emp[3].index(dv) < emp[0].index(av)): continue
								elif (emp[3].index(dc) < emp[0].index(ac)) and (emp[3].index(dv) > emp[0].index(av)): continue
								elif (emp[3].index(dc) > emp[2].index(cc)) and (emp[3].index(dc) < emp[2].index(cv)): continue
								elif (emp[3].index(dv) > emp[2].index(cc)) and (emp[3].index(dv) < emp[2].index(cv)): continue
								elif (emp[3].index(dc) > emp[1].index(bc)) and (emp[3].index(dc) < emp[1].index(bv)): continue
								elif (emp[3].index(dv) > emp[1].index(bc)) and (emp[3].index(dv) < emp[1].index(bv)): continue
								elif (emp[3].index(dc) > emp[0].index(ac)) and (emp[3].index(dc) < emp[0].index(av)): continue
								elif (emp[3].index(dv) > emp[0].index(ac)) and (emp[3].index(dv) < emp[0].index(av)): continue

								LT = av - ac + bv - bc + cv - cc + dv - dc
								if LT > max_LT:
									max_LT = LT
									maxi = [ac,av,bc,bv,cc,cv,dc,dv]
									pos_maxi = [emp[0].index(ac), emp[0].index(av), emp[1].index(bc), emp[1].index(bv), emp[2].index(cc), emp[2].index(cv), emp[3].index(dc), emp[3].index(dv)]

if maxi[0] != 0:
    print("acao 1: compra %d, venda %d, lucro %.2f" %(pos_maxi[0], pos_maxi[1], maxi[1] - maxi[0]))
if maxi[2] != 0:
    print("acao 2: compra %d, venda %d, lucro %.2f" %(pos_maxi[2], pos_maxi[3], maxi[3] - maxi[2]))
if maxi[4] != 0:
    print("acao 3: compra %d, venda %d, lucro %.2f" %(pos_maxi[4], pos_maxi[5], maxi[5] - maxi[4]))
if maxi[6] != 0:
    print("acao 4: compra %d, venda %d, lucro %.2f" %(pos_maxi[6], pos_maxi[7], maxi[7] - maxi[6]))
print("Lucro: %.2f" %max_LT)