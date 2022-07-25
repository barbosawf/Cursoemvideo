"""
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

dados = {}
lista = []
print('='*60)
while True:
    dados['Nome'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input('Partidas: '))
    if partidas > 0:
        gols = list()
        for c in range(1, partidas + 1):
            gols.append(int(input(f'Número de gols da {c}ª partida: ')))
        dados['Gols'] = gols
        dados['Total'] = sum(gols)
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp not in 'SN':
            print('ERRO! Digite corretamente S ou N.')
        else:
            break
    lista.append(dados.copy())
    dados.clear()
    if resp == 'S':
        print('='*60)
    else:
        break

print('='*60)

print(f'{"Cod":<4}{"Nome":<18}{"Gols":<32}{"Total":>5}')
print('-'*60)
for a, b in enumerate(lista):
    print(f'{a:<4}', end='')
    print(f'{b["Nome"]:<18}{str(b["Gols"]):<32}{b["Total"]:>5}')
print('-'*60)

while True:
    while True:
        n = int(input('Mostrar dados de qual jogador? (Parar: 999) '))
        if n not in range(0, len(lista)) and n != 999:
            print(f'ERRO! Não existe jogador com o código {n}')
            print('-'*60)
        elif n in range(0, len(lista)) or n == 999:
            break
    if n != 999:
        print(f' -- Levantamento do jogador {lista[n]["Nome"].upper()}:')
        for c, v in enumerate(lista[n]["Gols"]):
            print(f'    No {c + 1}º jogo, fez {v} gols.')
    elif n == 999:
        break
    print('-'*60)
print('='*60)
print(f'{"VOLTE SEMPRE":^60}')
print('='*60)



