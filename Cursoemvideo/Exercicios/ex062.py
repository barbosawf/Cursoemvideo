"""
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = int(input('Número de termos: '))
c = 0

while c < d + 1:
    print('{} '.format(p), end='➡ ')
    p += r
    c += 1
    if c == d:
        print('ACABOU!\n')
        d = int(input('Você quer adicionar mais alguns termos? Quantos? '))
        if d > 0:
            c = 0
        elif d == 0:
            c += 1
print('ACABOU!')
print(f'Progressão finalizada com {c} termos mostrados.')

print('')

print('Gerador de PA')
print('=-'*6)
pro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
max = 10
cont = 0
while cont < max:
    print(pro_termo, end=' → ')
    pro_termo += razao
    cont += 1
    if cont == max:
        print('Pausa')
        continuar = int(input('Quantos termos você quer mostrar a mais? '))
        if continuar > 0:
            max += continuar
        else:
            print(f'Progressão finalizada com {cont} termos mostrados')
            break

print('')


an = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
n = 10
while n != 0:
    print(an, end=' ')
    an += r
    if n == 1:
        n += int(input('\nDeseja mais quantos termos? '))
    n -= 1
print('')


print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = int(input('Digite quantos termos você quer: '))

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} ->', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')

print('')
###########

from time import sleep
print("-=" * 20)
print("{:=^50}".format("\033[1;30mTermos de uma PA\033[m"))
print("-=" * 20)
p1 = int(input("\033[1;35mPrimeiro Termo:\033[m "))
r = int(input("\033[1;34mRazao da PA:\033[m "))
a1 =[]
a1.append(p1)
fim = False
count = 0
print("\n\033[1;4;36m10 Primeiros termos da PA:\033[m")
for c in range(1,11):
    print(f"\033[30m{a1[c-1]} ->",end=" ")
    a1.append(a1[c-1] + r)
    count+=1
print("PAUSA\033[m")
sleep(0.5)
while not fim:
    op = str(input(f"""
\033[1;33m===========================
[ 1 ] + 10 Termos Desta PA
[ 2 ] + x Termos Desta PA
[ 3 ] Trocar o primeiro termo e a razão
[ 4 ] Achar Termo Desta PA ex: (a11= {a1[10]})
[ 5 ] Limpar Termos
[ 0 ] Sair do programa

\033[1;35mPrimeiro Termo = \033[m \033[1;30m{p1}\033[m
\033[1;34mRazão =\033[m \033[1;30m{r}\033[m
\033[1;36mTermos mostrados = \033[1;30m{count}\033[m
\033[1;33m===========================\033[m 
\033[1;32m>>>> Opção:\033[m """)).strip()
    if op == '1':
        for x in range(1,11):
            count += 1
            print(f"{a1[count-1]} ->",end=" ")
            a1.append(a1[count-1] + r)
        print("PAUSA")
        sleep(0.5)
    elif op == '2':
        qtd = int(input("Quantos termos mais voce quer? "))
        print("\nProgressão Aritimetrica: ")
        for x in range(1,qtd+1):
            count += 1
            print(f"{a1[count -1]} ->",end=" ")
            a1.append(a1[count - 1] + r)
        print("PAUSA")
        sleep(0.5)
    elif op =='3':
        p1 = int(input("\033[1;35mPrimeiro Termo:\033[m "))
        a1 = []
        a1.append(p1)
        r = int(input("\033[1;34mRazão da PA:\033[m "))
        count = 0
        for x in range(1,11):
            count+=1
            print(f"{a1[count -1]} ->",end=" ")
            a1.append(a1[count-1]+r)
        print("PAUSA")
        sleep(0.5)
    elif op == '4':
        loc = int(input("Qual termo que voce quer encontrar ?"))
        if loc <= count:
            print(f"O termo \033[1;31ma{loc} = {a1[loc-1]}\033[m")
            sleep(0.5)
        else:
            dif = loc - count
            for x in range(1, dif+1):
                count += 1
                a1.append(a1[count - 1] + r)
            print(f"O termo \033[1;31ma{loc} = {a1[loc-1]}\033[m")
            sleep(0.5)
    elif op =='5':
        a1=[]
        a1.append(p1)
        count = 0
        for x in range(1, 11):
            count += 1
            print(f"{a1[count - 1]} ->", end=" ")
            a1.append(a1[count - 1] + r)
        print("PAUSA")
        sleep(0.5)
    elif op == '0':
        fim = True
    else:
        print("Opção Invalida. Digite outra opção")
        sleep(0.5)
print(f"\033[1;4;31mFIM DO PROGRAMA. Ao total {count} Termos foram mostrados\033[m")

print('')
