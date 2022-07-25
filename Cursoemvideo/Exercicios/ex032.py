# Desafio 032
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#Caso 1) É um número divisível por 4, mas não é divisível por 100.
#Caso 2) É um número divisível por 4, por 100 e por 400.
ano = int(input('Que ano você quer analisar? Coloque 0 para analizar o ano atual. '))
from datetime import date
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
print('')

ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'{ano} é bissexto')
        else:
            print(f'{ano} não é bissexto')
    else:
        print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')

print('')
import calendar
date = int(input('Digite um ano: '))
if calendar.isleap(date) == True:
    print('O ano {} é bissexto: '.format(date))
else:
    print('O ano {} nao é bissexto.'.format(date))

print('')
a = int(input('ANO: '))
c = a % 4
d = a % 100
e = a % 400
if d > c == 0 or e == 0:
    print('É BISSEXTO!')
else:
    print('Não é BISSEXTO!')