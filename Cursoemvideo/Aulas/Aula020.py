def lin():
    print('=' * 50)


def mensagem(msg):
    print('=' * 50)
    print(f'{msg:^50}')
    print('=' * 50)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são {tam} números.')


def dobra(lst):  # uso de lista
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


def soma_val(* val):  # uso de desempacotamento
    s = sum(val)
    print(s)


soma(b=4, a=5)

lin()

mensagem('Wagner')

contador(2, 3, 4)
contador(3, 4, 7, 2, 6)

valores = [7, 2, 5, 0, 4]

dobra(valores)
print(valores)

soma_val(4, 3, 4, 5, 5)
