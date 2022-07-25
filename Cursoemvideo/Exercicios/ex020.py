import random
print('Desafio 020')

a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
lista = [a, b, c, d]
random.shuffle(lista)

print('A ordem de apresentação do trabalho será:')
print(lista)
