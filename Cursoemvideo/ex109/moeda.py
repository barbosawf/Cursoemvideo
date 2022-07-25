"""
Modifique as funções que foram criadas no desafio 107 para elas aceitarem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""


def moeda2(p=0, m='R$'):
    return f'{m} {p:.2f}'.replace('.', ',')


def aumentar(n=100, porc=10, formatada=False):
    res = n + (porc / 100) * n
    return res if formatada is False else moeda2(res)


def diminuir(n=100, porc=10, formatada=False):
    res = n - (porc / 100) * n
    return res if formatada is False else moeda2(res)


def dobro(n=100, formatada=False):
    res = 2 * n
    return res if formatada is False else moeda2(res)


def metade(n=100, formatada=False):
    res = 0.5 * n
    return res if formatada is False else moeda2(res)


def moeda(n=100):
    n = f'{n:.2f}'
    k = ''
    for c in n:
        if c == '.':
            c = ','
        k += c
    resp = f'R$ {k}'
    return resp
