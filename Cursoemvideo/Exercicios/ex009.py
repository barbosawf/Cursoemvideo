n = int(input('Digite um número: '))
print('A tabuada do número {} é:\n____________\n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n'
      '{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}\n____________'.format(n,
                                                                                                           n, n * 1,
                                                                                                           n, n * 2,
                                                                                                           n, n * 3,
                                                                                                           n, n * 4,
                                                                                                           n, n * 5,
                                                                                                           n, n * 6,
                                                                                                           n, n * 7,
                                                                                                           n, n * 8,
                                                                                                           n, n * 9,
                                                                                                           n, n * 10))
# -------------------------------------------------------------------------------------#
valor = int(input('Qual tabuada você deseja? '))
contador = 0
res = 0
while contador <= 10:
    res = valor * contador
    print(f'{valor} x {contador} = {res}')
    contador = contador + 1
# -------------------------------------------------------------------------------------#
val = int(input('Digite o numero para calcular a tabuada:\n'))
for contar in range(0, 11):
    print('{} x {:2} = {}'.format(val, contar, val * contar))

# -------------------------------------------------------------------------------------#
n = int(input('Digite um número inteiro: '))
tab = 0
while (tab <= 10):
    print('{} x {} = {}'.format(n, tab, n * tab))
    tab = tab + 1
