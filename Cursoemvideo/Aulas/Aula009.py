frase = 'Curso em Video Python'
print(len(frase))
print(frase[3])
print(frase.count('o'))
print(frase.count('o', 0, 13)) # último valor sempre ignorado pelo Python
print(frase.find('deo')) # Mostra onde começa o deo
print(frase.replace('Python', 'Android'))
print(frase)
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase2 = '   Aprenda Python   '
print(frase2)
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
print(frase.split())
print('-'.join(frase))
print("""Feliz é o homem que 
não anda no caminho dos ímpios,
nem se detém no caminho dos pecadores.""")

print('Curso' in frase)
print(frase.find('video'))
print(frase.lower().find('video'))

dividido = frase.split()
print(dividido[0])
print(dividido[2])
print(dividido[2][2])