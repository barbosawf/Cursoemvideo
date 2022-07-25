n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma vale {}.'.format(n1 + n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}.'.format(s, m, d))
print('A divisão inteira é {} e a potência é {}.'.format(di, e))

print('A soma é {}.'.format(s), end=' ')
print('A divisão inteira é {}.'.format(di))

print('A soma é {} e \n a divisão é {}.'.format(s, d))

print('A soma é {}.'.format(s), end=' >>>>> ')
print('A divisão inteira é {}.'.format(di))
