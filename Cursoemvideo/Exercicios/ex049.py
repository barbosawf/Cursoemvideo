"""
Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for
"""
print('Desafio 049')

n = int(input('Digite um número inteiro: '))
print('TABUADA DE {}:'.format(n))
print('='*15)
for c in range(0, 11):
    print(f'{n} x {c} = {n * c}')
print('='*15)
