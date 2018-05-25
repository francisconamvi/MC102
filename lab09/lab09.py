max_LT = max_ac = max_av = max_bc = max_bv = max_cc = max_cv = max_dc = max_dv = 0
emp = [[0], [0], [0], [0]]

d = int(input()) #dias de business
#lista de empresas com valor de cada dia
for i in range (len(emp)):
    for a in range(d):
        valor = float(input())
        emp[i].append(valor)

#print(emp)

for ac in emp[0][0:len(emp[0])-1]:
	for bc in emp[1][0:len(emp[1])-1]:
		if (emp[1].index(bc) == emp[0].index(ac)) and (emp[1].index(bc) != 0): continue
		for cc in emp[2][0:len(emp[2])-1]:
			if ((emp[2].index(cc) == emp[1].index(bc)) or (emp[2].index(cc) == emp[0].index(ac))) and (emp[2].index(cc) != 0): continue
			for dc in emp[3][0:len(emp[3])-1]:
				if ((emp[3].index(dc) == emp[2].index(cc)) or (emp[3].index(dc) == emp[1].index(bc)) or (emp[3].index(dc) == emp[0].index(ac))) and (emp[3].index(dc) != 0): continue

				#aqui começa o role das venda
				for av in emp[0][(emp[0].index(ac)):]:
					if (emp[0].index(ac) == emp[0].index(av) and av!=0): continue
					if (av-ac) < 0: continue
					if av != 0 and ac == 0: continue
					for bv in emp[1][(emp[1].index(bc)):]:
						if (emp[1].index(bc) == emp[1].index(bv) and bv!=0): continue
						if (bv-bc) < 0: continue
						if bv != 0 and bc == 0: continue
						if (emp[1].index(bv) == emp[0].index(av)) and (emp[1].index(bv) != 0): continue
						if (emp[1].index(bc) > emp[0].index(ac)) and (emp[1].index(bv) < emp[0].index(av)): continue
						if (emp[1].index(bc) < emp[0].index(ac)) and (emp[1].index(bv) > emp[0].index(av)): continue
						if (emp[1].index(bc) > emp[0].index(ac)) and (emp[1].index(bc) < emp[0].index(av)): continue
						if (emp[1].index(bv) > emp[0].index(ac)) and (emp[1].index(bv) < emp[0].index(av)): continue
						for cv in emp[2][(emp[2].index(cc)):]:
							if (emp[2].index(cc) == emp[2].index(cv) and cv!=0): continue
							if (cv-cc) < 0: continue
							if cv != 0 and cc == 0: continue
							if ((emp[2].index(cv) == emp[1].index(bv)) or (emp[2].index(cv) == emp[0].index(av))) and (emp[2].index(cv) != 0): continue
							if (emp[2].index(cc) > emp[1].index(bc)) and (emp[2].index(cv) < emp[1].index(bv)): continue
							if (emp[2].index(cc) < emp[1].index(bc)) and (emp[2].index(cv) > emp[1].index(bv)): continue
							if (emp[2].index(cc) > emp[0].index(ac)) and (emp[2].index(cv) < emp[0].index(av)): continue
							if (emp[2].index(cc) < emp[0].index(ac)) and (emp[2].index(cv) > emp[0].index(av)): continue
							if (emp[2].index(cc) > emp[1].index(bc)) and (emp[2].index(cc) < emp[1].index(bv)): continue
							if (emp[2].index(cv) > emp[1].index(bc)) and (emp[2].index(cv) < emp[1].index(bv)): continue
							if (emp[2].index(cc) > emp[0].index(ac)) and (emp[2].index(cc) < emp[0].index(av)): continue
							if (emp[2].index(cv) > emp[0].index(ac)) and (emp[2].index(cv) < emp[0].index(av)): continue
							for dv in emp[3][(emp[3].index(dc)):]:
								if (emp[3].index(dc) == emp[3].index(dv) and dv!=0): continue
								if (dv-dc) < 0: continue
								if dv != 0 and dc == 0: continue
								if ((emp[3].index(dv) == emp[2].index(cv)) or (emp[3].index(dv) == emp[1].index(bv)) or (emp[3].index(dv) == emp[0].index(av))) and (emp[3].index(dv) != 0): continue
								if (emp[3].index(dc) > emp[2].index(cc)) and (emp[3].index(dv) < emp[2].index(cv)): continue
								if (emp[3].index(dc) < emp[2].index(cc)) and (emp[3].index(dv) > emp[2].index(cv)): continue
								if (emp[3].index(dc) > emp[1].index(bc)) and (emp[3].index(dv) < emp[1].index(bv)): continue
								if (emp[3].index(dc) < emp[1].index(bc)) and (emp[3].index(dv) > emp[1].index(bv)): continue
								if (emp[3].index(dc) > emp[0].index(ac)) and (emp[3].index(dv) < emp[0].index(av)): continue
								if (emp[3].index(dc) < emp[0].index(ac)) and (emp[3].index(dv) > emp[0].index(av)): continue
								if (emp[3].index(dc) > emp[2].index(cc)) and (emp[3].index(dc) < emp[2].index(cv)): continue
								if (emp[3].index(dv) > emp[2].index(cc)) and (emp[3].index(dv) < emp[2].index(cv)): continue
								if (emp[3].index(dc) > emp[1].index(bc)) and (emp[3].index(dc) < emp[1].index(bv)): continue
								if (emp[3].index(dv) > emp[1].index(bc)) and (emp[3].index(dv) < emp[1].index(bv)): continue
								if (emp[3].index(dc) > emp[0].index(ac)) and (emp[3].index(dc) < emp[0].index(av)): continue
								if (emp[3].index(dv) > emp[0].index(ac)) and (emp[3].index(dv) < emp[0].index(av)): continue

								LT = av - ac + bv - bc + cv - cc + dv - dc
								if LT > max_LT:
									max_LT = LT
									max_ac = ac
									pos_max_ac = emp[0].index(ac)
									max_av = av
									pos_max_av = emp[0].index(av)
									max_bc = bc
									pos_max_bc = emp[1].index(bc)
									max_bv = bv
									pos_max_bv = emp[1].index(bv)
									max_cc = cc
									pos_max_cc = emp[2].index(cc)
									max_cv = cv
									pos_max_cv = emp[2].index(cv)
									max_dc = dc
									pos_max_dc = emp[3].index(dc)
									max_dv = dv
									pos_max_dv = emp[3].index(dv)
								#print(ac,bc,cc,dc)
								#print (av, bv, cv, dv)

if max_ac != 0:
    print("acao 1: compra %d, venda %d, lucro %.2f" %(pos_max_ac, pos_max_av, max_av - max_ac))
if max_bc != 0:
    print("acao 2: compra %d, venda %d, lucro %.2f" %(pos_max_bc, pos_max_bv, max_bv - max_bc))
if max_cc != 0:
    print("acao 3: compra %d, venda %d, lucro %.2f" %(pos_max_cc, pos_max_cv, max_cv - max_cc))
if max_dc != 0:
    print("acao 4: compra %d, venda %d, lucro %.2f" %(pos_max_dc, pos_max_dv, max_dv - max_dc))
print("Lucro: %.2f" %max_LT)