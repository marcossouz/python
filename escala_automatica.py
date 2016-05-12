#
# Gera uma escala automatica para a banda da igreja
#

import random
print('Gerador de Escalas Ministerio de louvor\n')

#integrantes

vocais = ['Marcos', 'Juninho', 'Joyce', 'Raquel', 'Elly', 'Witalla', 'Mary 2']
backVocal = ['Geivison', 'Lindines', 'Luciano', 'Neidinha']

#print(len(vocais)) #Quantidade de vocais
guitarra = ['Marcos', 'Juninho', 'Bruninho']
violao = ['Natalia', 'Elly', 'Raquel']
baixo = ['Marcos', 'Bruninho']
teclado = ['Esequiel', 'Marcos']
bateria = ['Gabriel']

f = open("escala.txt", "w")
voc = random.sample(vocais,2)
print('-->Vocais: ')
f.write('-->Vocais:\n')

for x in voc:
    print('%s' %(x))
    f.write('%s\n' %(x))

print('\n-->Back:')
f.write('\n-->Back:\n')

back = random.sample(backVocal,1)
for x in back:
    print('%s' %(x))
    f.write('%s\n' %(x))
    
#print('Back: %s' %(back))
print('\n-->Guitarra:')
f.write('\n-->Guitarra:\n')

g = random.sample(guitarra,1)
s = 1
while s:
    for x in voc:
        if x == g[0]:
            g = random.sample(guitarra,1)
            s = 1
        else:
            s = 0
print ('%s' %(g[0]))
f.write('%s\n' %(g[0]))

print('\n-->Violao:')
f.write('\n--Violao:\n')

viol = random.sample(violao,1)
s = 1
while s:
    for x in voc:
        if x == viol[0]:
            viol = random.sample(violao,1)
            s = 1
        else:
            s = 0
print ('%s' %(viol[0]))
f.write('%s\n' %(viol[0]))

print('\n-->Baixo:')
f.write('\n-->Baixo:\n')

baix = random.sample(baixo,1)
s = 1
z = 1
cont = 0
while s==1 or z==1 and cont < 50:
    for x in voc:
        if x == baix[0]:
            baix = random.sample(baixo,1)
            s = 1
        else:
            s = 0
    
    for y in g:
        if y == baix[0]:
            baix = random.sample(baixo,1)
            z = 1
        else:
            z = 0
    x = 0
    y = 0
    cont = cont + 1

print ('%s' %(baix[0]))
f.write('%s\n' %(baix[0]))

print('\n-->Teclado:')
f.write('\n-->Teclado:\n')

tecl = random.sample(teclado,1)
s = 1
z = 1
w = 1
cont = 0

while s==1 or z==1 or w==1 and cont < 50:
    for x in voc:
        if x == tecl[0]:
            tecl = random.sample(teclado,1)
            s = 1
        else:
            s = 0
            
    for y in g:
        if y == tecl[0]:
            tecl = random.sample(teclado,1)
            z = 1
        else:
            z = 0   

    for k in baix:
        if k == tecl[0]:
            tecl = random.sample(teclado,1)
            w = 1
        else:
            w = 0
    x = 0
    y = 0
    k = 0
    cont = cont + 1

print ('%s' %(tecl[0]))
f.write('%s\n' %(tecl[0]))

print('\nBateria:')
f.write('\n-->Bateria:\n')

bat = random.sample(bateria,1)
print ('%s' %(bat[0]))
f.write('%s\n' %(bat[0]))

f.close()

#print ('Vocais: %s' %(random.sample(vocais,2)))
#print ('Back: %s' %(random.sample(backVocal,1)))
