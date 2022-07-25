"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

p = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
     'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
     'PROGRAMADOR', 'FUTURO', 'WAGNER', 'MIRAGEM', 'LIBERDADE')

for a in range(0, len(p)):
     print(f'Na palavra {p[a]} temos: ', end='')
     for b in range(0, len(p[a])):
          if str(p[a][b]) in "AEIOU":
               print(str(p[a][b]), end=' ')
     print('')
print(' ')
print('='*50)
tupla = ('Palavra','Casa','Apartamento','Rua')

vogal = ('a','e','i','o','u')

print()
for x in tupla:
     print(f'Na palavra {x}, existem as vogais:', end='')
     for y in vogal:
          if y in x:
               print (f' {y}', end='')
     print('.')

print(' ')
print('~' * 50)
palavras = ('aprender', 'esforço', 'foco', 'força de vontade', 'trabalho duro', 'prática', 'java', 'python')

for palavra in palavras:
     print('Na palavra ' + palavra.upper(), end=' ')
     vogais = ''
     for letra in palavra:
          if letra.lower() in 'aeiou':
               vogais += letra + ' '

     print('temos:  {}'.format(vogais))
print('~' * 50)



