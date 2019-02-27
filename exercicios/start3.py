# exercicios de 9-11

print('prog 9 Farenheit em Celsius\n')

f = float(input('Digite a temperatura em Farenheit: '))
c = (5 * (f-32) / 9)

print('A temperatura em celsius é: %.2f' %(c))

print('\nprog 10 voltando C em F\n')
c = float(input('digite a temperatura em celsius: '))
f = (c*9/5) + 32

print('A temperatura em F: %.2f' %(f))

print('\nprog 11\n')
int1 = int(input('int 1: '))
int2 = int(input('int 2: '))
fl1 = float(input('float1: '))

print('result one: %.2f' %((2*int1) * (int2/2)))
print('result two: %.2f' %(int1*3 + fl1))
print('result three: %.2f' %(fl1*fl1*fl1)) 

