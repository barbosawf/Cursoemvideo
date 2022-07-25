"""
Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior
"""
from time import sleep


def maior(*n):
    print('Analisando os valores passados:')
    if len(n) > 0:
        print(f'Foram informados {len(n)} valores ao todo: ', end='')
        for c, k in enumerate(n):
            sleep(0.4)
            print(k, end='')
            if c < len(n) - 2:
                print(', ', end='')
            if c == len(n) - 2:
                print(' e ', end='')
        print('.')
        print(f'O maior número é o {max(n)}.')
    else:
        print(f'Nenhum valor foi informado.')
    print('=' * 70)


print('=' * 70)
maior(5, 3, 5, 6, 7, 3, 1)

maior(5, 3, 5, 100, 232)

maior(3)

maior()

