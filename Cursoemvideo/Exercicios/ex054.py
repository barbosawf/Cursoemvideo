"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
print('Desafio 054')
from datetime import date

atual = date.today().year
n1 = 0
n2 = 0
for c in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    if atual - nasc >= 21:
        n1 += 1
    else:
        n2 += 1

print(f'\n{n1} pessoas atingiram a maioridade.')
print(f'{n2} pessoas NÃO atingiram a maioridade.\n')

# De um aluno do curso:
from datetime import date
menores = 0
for c in range(1, 8):
    pessoa = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if date.today().year - pessoa < 21:
        menores += 1
print('\n{} são Maiores e {}são menores.'.format(7 - menores, menores))


