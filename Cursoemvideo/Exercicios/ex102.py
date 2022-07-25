"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    c = ''
    while n != 0:
        f *= n
        c = c + str(n)
        n -= 1
        if n > 0:
            c = c + ' x '
        if n == 0:
            c = c + ' = ' + str(f)
    if not show:
        return f
    else:
        return c


def fatorial2(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    while n > 0:
        if show:
            print(n, end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= n
        n -= 1
    return f


def fatorial3(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

num = int(input('De qual número você quer o fatorial? '))
print(fatorial(num, show=False))
print(fatorial2(num, show=False))
print(fatorial3(num, show=False))
