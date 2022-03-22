lista_vendedores = ["Emily", "Larissa", "Rafael", "Milena"]

vendas = []
c = 0
while c < 4:
	venda = float(input(f'Quanto foi vendido por {lista_vendedores[c]}'))
	vendas.append(venda)
	c+= 1

b = 0
while b < 4 :
    if (venda<5000.00):
        salario = 1000.00 + 0.01*venda
        print(f'Salário de {lista_vendedores[c]}: R$ {salario}')
    if (5000.00<=venda<=10000.00):
        salario = 1000.00 + 0.015*venda
        print(f'Salário de {lista_vendedores[c]}: R$ {salario}')
    if (venda>10000.00):
        salario = 1000.00 + 0.02*venda
        print(f'Salário de {lista_vendedores[c]}: R$ {salario}')
    b+=1
