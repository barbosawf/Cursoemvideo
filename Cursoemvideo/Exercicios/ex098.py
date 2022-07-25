"""
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep


def contador(a, b, c):
    if c == 0:
        c = 1
    if b > a:
        k = 1
        if c < 0:
            c = c * (-1)
    elif b < a:
        k = -1
        if c > 0:
            c = c * (-1)
    print(f'Contagem de {a} até {b}, de {abs(c)} em {abs(c)}:')
    for d in range(a, b + k, c):
        print(d, end=' ')
        sleep(0.5)
    print('FIM!')
    print('=' * 40)


print('=' * 40)
contador(1, 10, 1)
contador(10, 0, 2)
a = int(input('Digite o valor inicial: '))
b = int(input('Digite o valor final: '))
c = int(input('Digite o valor do passo: '))
contador(a, b, c)

print()
print('Outro Aluno')


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
        fim -= 2
    for c in range(inicio, fim + 1, passo):
        print(c, end=' ')
        sleep(0.5)
    print()


contador(1, 10, 0)
contador(10, 0, 2)
contador(int(input('Digite o ínicio: ')), int(input('Ditite o fim: ')), int(input('Digite o passo: ')))
