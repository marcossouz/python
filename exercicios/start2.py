# exercicios de 5 a 8

print('programa5\n')
print('Conversor de metros em centimetros')
mt = float(input('metros: '))
cm = mt*100

print('%.2f metros equivale a %.2f centimetros' %(mt, cm))

print('\nprograma6\n')

r = float(input('digite o raio da circunferencia desejada: '))
area = 3.1415 * (r*r)

print('a area do circulo é: %.2f'%(area))

print('\nprog7 dobro da area de um quadrado\n')
l = float(input('lado do quadrado: '))
areaQ = l*l
print('dobro da area desse quadrado: %.2f' %(areaQ*areaQ))

print('\nprog8 salario no mes\n')

vHora = float(input('valor da hora trabalhada: '))
nHoras = int(input('numero de horas trabalhadas: '))

salario = vHora * nHoras
print('Seu salario será: R$%.2f' %(salario))

