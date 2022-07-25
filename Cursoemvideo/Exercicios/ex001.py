print('Olá, Mundo!')
msg = 'Olá Wagner!'
print(msg)

print('#' * 20)
print('\033[0:33mOlá, Mundo!\033[m')

l = {'preto': '\033[30m',
     'vermelho': '\033[31m',
     'verde': '\033[32m',
     'amarelo': '\033[33m',
     'azul': '\033[34m',
     'lilas': '\033[35m',
     'cyan': '\033[36m',
     'cinza': '\033[37m',
     'branco': '\033[97m'
     }

b = {'preto': '\033[40m',
     'vermelho': '\033[41m',
     'verde': '\033[42m',
     'amarelo': '\033[43m',
     'azul': '\033[44m',
     'lilas': '\033[45m',
     'cyan': '\033[46m',
     'cinza': '\033[47m',
     'branco': '\033[97m'
     }

f = {'nada': '\033[0m',
     'negrito': '\033[1m',
     'sublinhado': '\033[4m',
     'inverte': '\033[7m',
     'finaliza': '\033[m'
     }

print('{}Olá, Mundo!{}'.format(l['verde'], f['finaliza']))
print('{}{}Olá, Mundo!{}'.format(l['amarelo'], b['preto'], f['finaliza']))
print('{}{}{}Olá, Mundo!{}'.format(l['vermelho'], b['preto'], f['inverte'], f['finaliza']))

print('{}{}{}Olá, Mundo!{}'.format(l['vermelho'], b['branco'], f['inverte'], f['finaliza']))

print('{}{}{}Olá, Mundo!{} Tchau, Mundo!'.format(f['negrito'], l['verde'], f['inverte'], f['finaliza']))

print('{}{}{}Olá, Mundo!{} Tchau, Mundo!'.format(l['azul'], l['verde'], f['sublinhado'], f['finaliza']))

print('{}Olá, Mundo!{} Tchau, Mundo!'.format(l['preto'], f['finaliza']))