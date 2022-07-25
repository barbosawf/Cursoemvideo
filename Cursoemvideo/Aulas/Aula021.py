print(input.__doc__)


def soma(a, b, c=0):  # c parâmetros opcionais.
    """

    :param a: Indica primeiro termo.
    :param b: Indica segundo termo.
    :param c: Indica terceiro termo.
    :return: sem retorno.
    """
    s = a + b + c
    print(f'A soma vale {s}.')


soma(1, 2, 3)
soma(2, 3)


def teste():
    x = 8  # x tem um escopo local, pois está na função
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')


n = 2  # n tem um escopo global, pois está foram da função.
print(f'No programa principal, n vale {n}.')
teste()


#  print(f'No programa principal, x vale {x}.')


def teste2(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}.')
    print(f'B dentro vale {b}.')
    print(f'C dentro vale {c}.')


a = 5
teste2(a)
print(f'A fora vale {a}.')


def somar2(a=0, b=0, c=0):
    s = a + b + c
    return s


resp1 = somar2(2, 2, 4)
resp2 = somar2(3, 4)
resp3 = somar2(2)

print(f'Minhas somas são: {resp1}, {resp2} e {resp3}.')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))

print(par(num))

if par(num):
    print('É par!')
else:
    print('Não é par!')
