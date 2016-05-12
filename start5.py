print('prog 14\n\n')

peso = float(input('peso: '))

if(peso > 50):
    exced = peso - 50
    multa = exced * 4
else:
    exced = 0
    multa = 0
print('excedeu %.2f Kg\nMulta total: R$ %.2f'%(exced, multa))