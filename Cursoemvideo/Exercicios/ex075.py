"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
b = ''
print('='*40)
for c in range(1, 5):
    while True:
        if c == 1:
            a = int(input('Digite um número: [0 - 10] '))
        else:
            a = int(input('Digite outro número: [0 - 10] '))
        if 0 <= a <= 10:
            b += str(a)
            break
        print('Tente novamente. ', end='')


b = tuple(b)

print('='*40)
print(f'O número 9 apareceu {b.count("9")} vez(es).')

print('='*40)
if b.count("3") > 0:
    print(f'O número 3 está na {b.index("3") + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')

print('='*40)

i = 0
for k in range(0, 4):
    if int(b[k]) % 2 == 0:
        i += 1
if i > 0:
    print(f'{i} números pares foram digitados.')
else:
    print('Nenhum número par foi digitado.')
print('='*40)
print(' ')

num = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite outro número: '))
    )

print('='*40)
print(f'O número 9 apareceu {num.count(9)} vez(es).')

print('='*40)
if b.count(3) > 0:
    print(f'O número 3 está na {num.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')

print('='*40)

i = 0
for k in range(0, 4):
    if int(num[k]) % 2 == 0:
        i += 1
if i > 0:
    print(f'{i} números pares foram digitados.')
else:
    print('Nenhum número par foi digitado.')

print('='*40)
if 3 in num:
    print(f'O número 3 está na {num.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')

