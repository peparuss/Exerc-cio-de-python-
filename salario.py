from __future__ import barry_as_FLUFL


lista_vendedores = ["Emily", "Larissa", "Rafael", "Milena"]
vendas = []
salarios = []


a = 0
while a < 4:
    venda = float(input(f'Quanto foi vendido por {lista_vendedores[a]}: '))
    vendas.append(venda)
    a+= 1


b = 0
while b < 4 :
    if (vendas[b]<5000.00):
        salario = 1000.00 + 0.01*vendas[b]
        salarios.append(salario)
    if (5000.00<=vendas[b]<=10000.00):
        salario = 1000.00 + 0.015*vendas[b]
        salarios.append(salario)
    if (vendas[b]>10000.00):
        salario = 1000.00 + 0.02*vendas[b]
        salarios.append(salario)
    b+=1
faturamento = sum(vendas)

print(f'Faturamento total: R$ {faturamento}')

c = 0
while c < 4:
  print(f'Salário de {lista_vendedores[c]}: R$ {salarios[c]}')
  c+=1

salario_jessica = 2000.00 + faturamento*0.005
print(f'Salário da Jéssica: R$ {salario_jessica}')

total_salarios = sum(salarios) + salario_jessica
print(f'Total dos salários: R$ {total_salarios}')

