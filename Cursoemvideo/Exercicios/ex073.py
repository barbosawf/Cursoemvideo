"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthias',
         'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
         'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print('='*85)
print('Lista de times: ')
for t in times:
    print(t)

print('='*85)
print('Os 5 primeiros colocados são: ')
for c in range(0, 5):
    print(f'{times[c]}')

print('='*85)
print(f'Os 5 primeiros colocados são:\n{times[0:6]}')

print('='*85)
print(f'Os 4 últimos colocados são:\n{times[20:15:-1]}')

print('='*85)
print(f'Os 4 últimos colocados são:\n{times[-4:]}')

print('='*85)
print(f'Times em ordem alfabética:\n{sorted(times)}.')

print('='*85)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')

