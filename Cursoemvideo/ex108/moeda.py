"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções
"""


def aumentar(n=100, porc=10):
    res = n + (porc / 100) * n
    return res


def diminuir(n=100, porc=10):
    res = n - (porc / 100) * n
    return res


def dobro(n=100):
    res = 2 * n
    return res


def metade(n=100):
    res = 0.5 * n
    return res


def moeda(n=100):
    n = f'{n:.2f}'
    k = ''
    for c in n:
        if c == '.':
            c = ','
        k += c
    resp = f'R$ {k}'
    return resp


def moeda2(p=0, m='R$'):
    return f'{m} {p:.2f}'.replace('.', ',')
