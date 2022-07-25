"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

lista = []
par = []
impar = []

resp1 = False
while resp1 != True:
    n = input('Digite um valor: ')
    if n.isnumeric():
        resp1 = True


print(f'{25*"="}')
while True:
    resp1 = False
    while resp1 != True:
        n = input('Digite um valor: ')
        resp1 = n.isnumeric()
    lista.append(int(n))
    resp2 = ' '
    while resp2 not in 'SN':
        resp2 = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print(f'{25*"="}')
    if resp2 == 'N':
        break

for a in lista:
    if a % 2 == 0:
        par.append(a)
    else:
        impar.append(a)

print(f'A lista completa de números digitados é: {lista}')
if len(par) > 0:
    print(f'Os números pares digitados foram: {par}')
else:
    print('Nenhum número par foi digitado.')
if len(impar) > 0:
    print(f'Os números ímpares digitados foram: {impar}')
else:
    print('Nenhum número ímpar foi digitado.')

