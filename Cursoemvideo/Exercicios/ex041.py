print('Desafio 041\n')
""" A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos : Sênior
- Acima: Master
"""

from datetime import date
atual = date.today().year
ano = int(input('E que ano você nasceu? '))
idade = atual - ano
if idade <= 9:
    print('Você tem {} ano(s) e está na categoria MIRIM da natação.'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e está na categoria INFANTIL da natação.'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e está na categoria JÚNIOR da natação.'.format(idade))
elif idade <= 20:
    print('Você tem {} anos e está na categoria SÊNIOR da natação.'.format(idade))
else:
    print('Você tem {} anos e está na categoria MASTER da natação.'.format(idade))
