#coding: utf-8
#19 Faça um programa que peça o tamanho de um arquivo para download (em MB)
#e a velocidade de um link de Internet (em Mbps), calcule e informe o
#tempo aproximado de download do arquivo usando este link (em minutos). 

mb = float(input('tamanho do arquivo em MB: '))
veloc = float(input('velocidade do link de internet em Mbps: '))

tempo_em_segundos = (int)(mb/veloc)

tempo_em_minutos = 0

while tempo_em_segundos > 60:
	tempo_em_segundos = tempo_em_segundos - 60
	tempo_em_minutos = tempo_em_minutos + 1

print ('\nduracao do download {:d} min e {:d} seg\n'.format(tempo_em_minutos,tempo_em_segundos))
