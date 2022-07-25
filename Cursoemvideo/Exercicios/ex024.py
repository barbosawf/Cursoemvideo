# Desafio 24
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"
cidade = str(input('Digite o nome de uma cidade: ')).strip()
cidade_upper = cidade.upper()
if 'SANTO' in cidade_upper:
    print('Sua cidade começa com a palavra Santo.')
else:
    print('Sua cidade não começa com a palavra Santo.')

print('')
cid = str(input('Em que cidade você nasceu? ')).strip()
print('É {} que o nome da sua cidade começa com a palavra Santo.'.format(cid[:5].upper() == 'SANTO'))
