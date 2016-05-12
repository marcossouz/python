print ('16. loja de tintas\n')

tam = float(input('metros quadrados a ser pintado: '))

litro = tam/3
metroPintado = 0
#1 metro pintado consome 1/3 de de um litro
#1 litro equivale a 3 de metro pintado

# 18 litro formam 1 lata
# 1 lata custa 80
lata = 1
while litro > 0:
    metroPintado = metroPintado + 1
    if metroPintado%3 == 0:
        litro = litro - 1
    if metroPintado%55 == 0:
        lata = lata + 1
        
print('latas necessarias: %d' %(lata))  

print('17. loja de tinta - versao 2')      