print('Desafio 019a')
import random
a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))

e = random.randint(1, 4)

if e == 1:
    print('{} irá apagar o quadro, pois o número sorteado foi o {}.'.format(a, e))
elif e == 2:
    print('{} irá apagar o quadro, pois o número sorteado foi o {}.'.format(b, e))
elif e == 3:
    print('{} irá apagar o quadro, pois o número sorteado foi o {}.'.format(c, e))
else:
    print('{} irá apagar o quadro, pois o número sorteado foi o {}.'.format(d, e))

print('Desafio 019b')

a = str(input('Digite o nome do primeiro aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
lista = [a, b, c, d]

print('O aluno escolhido para apagar o quadro foi o(a) {}.'.format(random.choice(lista)))
