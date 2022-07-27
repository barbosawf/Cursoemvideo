lista = ["a", "b", "c", "d", "e"]
contador = 1
for letra in lista:
    print(f' {letra * contador}')
    contador += 1

import string

for i in range(1, 12):
    print(string.ascii_lowercase[i - 1] * i)

from string import ascii_uppercase

for i, j in enumerate(ascii_uppercase, 1):
    print(j * i)


def pattern(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i + 1):
            ch = chr(num)
            print(ch, end='')
        num = num + 1
        print('')


n = 12
pattern(n)

for i in range(32,100):
    print(chr(i))