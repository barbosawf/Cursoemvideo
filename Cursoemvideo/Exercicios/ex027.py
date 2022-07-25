# Desafio 27
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome.
nome = str(input('Digite seu nome completo: ')).strip()
nome_sep = nome.split()

print('Seu primeiro nome é {} e seu último é {}.'.format(nome_sep[0], nome_sep[len(nome_sep) - 1]))
