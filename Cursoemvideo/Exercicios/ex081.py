"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

lista = []
print(f'{25*"="}')
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print(f'{25*"="}')
    if resp == 'N':
        break
print(f'{len(lista)} números foram digitados.')
print(f'Os números digitados em ordem decrescente são: {sorted(lista, reverse=True)}.')
if lista.count(5) > 0:
    print('O valor cinco está na lista.')
else:
    print(f'O valor cinco NÃO está na lista.')
