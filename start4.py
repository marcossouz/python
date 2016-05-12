#exercicios 12 e 13

print('prog 12\n')
alt = float(input('entre com a altura: '))
pesoi = (72.7*alt) - 58
print('peso ideal: %.2f' %(pesoi))

print('\nprog 13\n')
altura = float(input('entre com a altura: '))
sexo = input('M ou F: ')

#print('%s' %(type (sexo)))

if sexo == 'M':
    print('alt ideal: %.2f' %((72.7*altura) - 58))
else:
    if sexo == 'F':
        print('alt ideal: %.2f' %((62.1*altura) - 44.7))
