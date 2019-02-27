#exercicio 15

print('prog 15\n\n')

vHoras = float(input('Quanto você ganha por hora?: '))
nHoras = int(input('Quantas horas trabalha no mês?: '))

salarioInicial = vHoras * nHoras
print('\n+ Salário bruto: R$ %.2f' %(salarioInicial))

INSS = salarioInicial*0.08
IR = salarioInicial*0.11
sindicato = salarioInicial*0.05

salarioLiquido = salarioInicial - (INSS + IR + sindicato)

print('- IR (11%%): R$ %.2f' %(IR))
print('- INSS (8%%): R$ %.2f' %(INSS))
print('- Sindicato (5%%): R$ %.2f' %(sindicato))
print('= Salario Líquido: R$ %.2f' %(salarioLiquido))



