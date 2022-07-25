# Desafio 25
# Crie um programa que leia o nome de uma pessoa e diga se ele tem "Silva" no nome
nome = str(input('Digite seu nome completo: ')).strip()
nome_upper = nome.upper()
if 'SILVA' in nome_upper:
    print('Você tem Silva no nome.')
else:
    print('Você não tem Silva no nome.')

print('')
nome = str(input('Digite seu nome completo: ')).strip().upper()
print('Seu nome tem silva? {}'.format('SILVA' in nome))
