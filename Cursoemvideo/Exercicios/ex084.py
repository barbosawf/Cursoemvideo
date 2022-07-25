"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

pessoas = []
individuo = []
maiorpeso = menorpeso = 0

print('=' * 50)
while True:
    resp1 = False
    nome = str(input('Nome: '))
    while not resp1:
        peso = input('Qual o seu peso? [Kg]: ')
        if peso.isnumeric():
            resp1 = True
    individuo.append(nome)
    individuo.append(float(peso))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = individuo[1]
    else:
        if individuo[1] > maiorpeso:
            maiorpeso = individuo[1]
        if individuo[1] < menorpeso:
            menorpeso = individuo[1]
    pessoas.append(individuo[:])
    individuo.clear()
    resp2 = ' '
    while resp2 not in 'SN':
        resp2 = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('=' * 50)
    if resp2 == 'N':
        break

p_pesadas = []
p_leves = []

for p in pessoas:
    if p[1] == maiorpeso:
        p_pesadas.append(p[0])
    if p[1] == menorpeso:
        p_leves.append(p[0])

if len(pessoas) > 0:
    print(f'{len(pessoas)} pessoas foram cadastradas.')
    print(f'O maior peso foi {maiorpeso} que são das seguintes pessoas: {p_pesadas}.')
    print(f'O menor peso foi {menorpeso} que são das seguintes pessoas: {p_leves}.')
else:
    print(f'Apenas uma pessoa foi cadastrada: {pessoas[0][0]} com {pessoas[0][1]} Kg.')
print('=' * 50)
