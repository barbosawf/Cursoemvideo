"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

dados = {}

dados['Nome'] = str(input('Nome do jogador: ')).strip()
partidas = int(input('Partidas: '))
if partidas > 0:
    gols = list()
    total = 0
    for c in range(1, partidas + 1):
        n = int(input(f'Número de gols da {c}ª partida: '))
        total += n
        gols.append(n)
    dados['Gols'] = gols
    dados['Total'] = total
print('='*70)
print(dados)
print('='*70)
if partidas > 0:
    for k, v in dados.items():
        print(f'O campo {k} tem o valor {v}.')
    print('='*70)
    print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
    for c, v in enumerate(dados['Gols']):
        print(f'     => Na {c + 1}ª partida, fez {v} gols.')
    print(f'Foi um total de {dados["Total"]} gols.')
    print('='*70)
else:
    print(f'O jogador {dados["Nome"]} não jogou.')

