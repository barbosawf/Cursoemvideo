"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o susuário quer ou não continuar. No final mostre:
a) Quantas pessoas tem amsis de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
"""


p = 1
tot18 = 0
totH = 0
totM20 = 0
while True:
    print(f'========== {p}° PESSOA ==========')
    idade = -3.2
    while idade < 0:
        idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    else:
        p += 1
print('================================== \nACABOU!\n')
print(f'Total de pessoas com ou mais de 18 anos: {tot18}')
print(f'Total de pessoas do sexo masculino: {totH}')
print(f'Total de mulheres com menos de 20 anos: {totM20}')
