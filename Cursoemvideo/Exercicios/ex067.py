"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""


while True:
    n = int(input('Digite um número: '))
    if n > 0:
        print(f'A tabuada de {n} é: ')
        for c in range(0, 11):
            print('{} x {:2} = {}'.format(n, c, n * c))
    else:
        print('PROGRAMA ENCERRADO!')
        break

