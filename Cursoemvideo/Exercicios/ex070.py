"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) aual é o nome do produto mais barato.
"""
c = count = tot = valorbarato = 0
nomebarato = ' '

print(f'{5*"="} {"LOJA BARATÃO"} {5*"="}')
while True:
    nome = str(input('Nome do produto: ')).strip()
    valor = float(input('Valor do produto: R$ '))
    tot += valor
    count += 1
    if valor > 1000:
        c += 1
    if count == 1 or valor < valorbarato:
        nomebarato = nome
        valorbarato = valor
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print(f'{25*"="}')
    if resp == 'N':
        print(f'{25*"="}')
        break
print(f'Valor total da compra: R$ {tot}')
print(f'{c} produto(s) custa(m) mais de R$ 1000,00.')
print(f'{nomebarato} é o produto mais barato e custa R$ {valorbarato}.')