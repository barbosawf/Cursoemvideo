"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = 'A'
while sexo not in 'MF':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if sexo not in 'MF':
        print('Digite corretamente o sexo, por favor: ')
if sexo == 'M':
    print('O sexo é masculino.')
else:
    print('O sexo é feminino.')

print('')
sexo = 'A'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    if sexo not in 'MF':
        print('Digite corretamente o sexo, por favor: ')
if sexo == 'M':
    print('O sexo é masculino.')
else:
    print('O sexo é feminino.')
