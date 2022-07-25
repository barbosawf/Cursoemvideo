# Desafio 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao sem considerar espaços
# Quantas letras tem o primeiro nome

nome = str(input('Qual é o seu nome todo? ')).strip()
print("Nome com todas as letras maiúsculas: \n{}.".format(nome.upper()))
print('')
print("Nome com todas as letras minúscula: \n{}.".format(nome.lower()))
print('')
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
print('')

print('Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))
