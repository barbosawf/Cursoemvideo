print('Desafio 039')
"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

sexo = str(input("""Você é homem ou mulher?
Digite h para homem e m para mulher: """))

if sexo == 'm':
    print('Você não precisa se alistar.')
else:
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    if idade == 18:
        print('Você precisa se alistar IMEDIATAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem 18 anos. Ainda falta(m) {} ano(s) para o alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}.'. format(ano))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Você deveria ter se alistado em {}.'. format(ano))