"""
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá conseguir mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(nome='', g=''):
    nome = nome.strip()
    g = g.strip()
    if g.isnumeric():
        g = abs(int(g))
        if nome == '':
            status = f'Jogador NÃO informado fez {g} gols.'
        elif nome != '':
            status = f'O jogador {nome.upper()} fez {g} gols.'
    else:
        g = ''
        if g == '':
            if nome == '':
                status = 'Nome e número de gols NÃO informados.'
            elif nome != '':
                status = f'Jogador {nome.upper()} informado. Número de gols NÃO informado.'
    return status


jogador = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))

print(ficha(jogador, gols))


# solução do professor


#def ficha2(n='', g=''):

