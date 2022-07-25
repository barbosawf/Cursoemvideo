"""
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
dados = dict()
lista = list()
print('=' * 60)
while True:
    dados['Nome'] = str(input('Nome: ')).strip()
    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['Sexo'] not in 'MF':
            print("ERRO! Digite o sexo corretamente!")
            del dados['Sexo']
        else:
            break
    dados['Idade'] = int(input('Idade: '))
    lista.append(dados.copy())
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] '))
        if resp not in 'SN':
            print("ERRO! Digite a resposta corretamente!")
    if resp == 'S':
        print('=' * 60)
    else:
        print('=' * 60)
        break
if len(lista) == 1:
    print('A) Apenas uma pessoa foi cadastrada.')
else:
    print(f'A) {len(lista)} pessoas foram cadastradas.')
tot = 0  # para somar a idade
for a in lista:
    tot += a['Idade']
media = tot / len(lista)
print(f'B) A média de idade foi {media:.2f} anos.')
totF = 0  # Conta o total de mulheres
for a in lista:
    if a['Sexo'] == 'F':
        totF += 1
if totF > 0:
    if totF == 1:
        print('C) Uma mulher foi cadastrada que foi a ', end='')
    else:
        print(f'C) As mulheres cadastradas foram: ', end='')
    for c, d in enumerate(lista):
        if d['Sexo'] == 'F':
            print(f'{d["Nome"]}', end='')
        if c < totF - 2:
            print(', ', end='')
        elif c == totF - 2:
            print(' e ', end='')
    print('.')
else:
    print('C) Nenhuma mulher foi cadastrada.')
totAcimaMedia = 0
for a in lista:
    if a['Idade'] > media:
        totAcimaMedia += 1
if totAcimaMedia > 0:
    print('D) Listas das pessoas que estão acima da média:')
    for a in lista:
        if a['Idade'] > media:
            print(f'   Nome = {a["Nome"]}; Sexo = {a["Sexo"]}; Idade = {a["Idade"]};')
else:
    print(f'D) Nenhuma pessoa está acima da média.')
print('=' * 60)
