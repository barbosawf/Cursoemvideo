"""
Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
"""

n = int(input('Digite o número de termos: '))
a = 0
b = 1
c = 0
d = 0

while d < n:
    print(f'{c} ', end='➡ ')
    d += 1
    c = a + b
    if d > 1:
        a = b
        b = c
print('FIM!')

#
print('')
Nant = 1
Fibonacci = 0

n = int(input('Digite um número:(Este vai ser o nº de elementos da sequência) '))

while n != 0:
    print('{}'.format(Fibonacci), end=' ➡ ')
    Fibonacci = Fibonacci + Nant
    Nant = Fibonacci - Nant
    n -= 1
print('FIM')

print('')
n = int(input('Digite um valor: '))
a = 0
b = 1
while n != 0:
    print(a, end=' ➡ ')
    c = a + b
    a = b
    b = c
    n -= 1
print('FIM!')

print('')

print('-'*25 + '\nSequência de Fibonacci\n' + '-'*25)
t = int(input('Digite quantos termos você quer saber: '))
n = 2
l = [0, 1, 1, 2]
print(f'{l[0]} -> {l[1]} -> {l[2]} -> {l[3]} -> ', end='')
for c in range(1, t-3):
    l.append(n)
    n = n + l[l.index(n)-1]
    print(f'{n} ➡ ', end='')
print(f'FIM')

print('')

print('\033[1mSequência de Fibonacci\033[0m')
termos = int(input('Quantos termos você quer mostrar? '))
a = 0
b = 1
for i in range(termos):
    print(a, end=" ➡ ")
    soma = a + b # novo termo
    a = b # a recebe o maior anterior
    b = soma # b recebe o novo termo
print('FIM')


print('')

n = int(input('Digite a quantidade de elementos de Fibonacci: '))
cont = 1
elemento_anterior = 0
elemento = 0
elemento_novo = 0
while cont <= n:
    print(elemento, end=' ➡ ')
    if elemento == 0:
        elemento_novo = 1
    else:
        elemento_novo = elemento + elemento_anterior
    elemento_anterior = elemento
    elemento = elemento_novo
    cont += 1
print('Acabou')

print('')

pri = 0
seg = 1
ter = 0
count = 0
lim = int(input('Sequência de Fibonacci - Quantos termos você quer?'))
print(f'{pri} - {seg} - ', end='')
while count < lim-2:
    count += 1
    ter = pri + seg
    print(f'{ter}', end=' - ')
    pri = seg
    seg = ter

print('FIM')


print('')

N = int(input('Quantos números da seq. de Fibonacci você gostaria ?'))
C = 0
A = 0
S = 1
D = 0
print(A)
while C == N:
    C += 1
    D = S + A
    print(D, end=' ')
    S = D
    A = S

print('')
print('-='*20)
print('         Sequência de Fibonacci')
print('-='*20)
termos = int(input('Quantos termos deseja saber ?\n'))
contador, sequencia = 2, 0
t1, t2 = 0, 1
print('0  ➡  1  ➡  ', end='')
while contador != termos:
    print(t1+t2, end='  ➡  ')
    contador += 1
    t1, t2 = t2, t1 + t2
print('FIM')



print('')
#Usei a fórmula de fibonacci '-'

from math import sqrt
v = int(input('Digite o número de termos da sequência: '))
n = 0
while n < v:
    n1 = (1 / sqrt(5)) * (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n)
    print('{:.0f} ...'.format(n1), end='')
    n += 1
print('FIM')

print('')
print('Sequência Fibonacci')
N = int(input('Quantos termos você quer ver ?: '))
print('Os {} primeiros termos da sequência Fibonacci São: '.format(N), end='')
n1 = 0
n2 = 1
termo = 0
i = 1
while i <= N :
    n1 = n2
    n2 = termo
    print('{} '.format(termo), end='')
    termo = n1 + n2
    i+=1
print('\nFim do Programa')

print('')
n = int(input('===Sequência de Fibonnaci===\nQuantos termos você quer mostrar? '))
contador = 0
termo = 0
anterior = 1
while contador < n:
    print(f'{termo} ➡ ', end="")
    termoa = termo
    termo += anterior
    anterior = termoa
    contador += 1
print('FIM')