from random import randint
from time import sleep

numRandint = randint(1, 3)
rpsPC = ''
rpsUser = ''

if numRandint == 1:
    rpsPC = 'Pedra'
elif numRandint == 2:
    rpsPC = 'Papel'
elif numRandint == 3:
    rpsPC = 'Tesoura'

print(
    '\n-=============-'
    '\n| [1] PEDRA   |'
    '\n| [2] PAPEL   |'
    '\n| [3] TESOURA |'
    '\n-=============-'
    '\n'
    '\nESCOLHA UM NÚMERO!'
)

userMethod = str(input('\nDigite o número: ')).strip()

while userMethod not in '1 2 3': #Obs.: Até essa aula ele ainda não ensinou o "while", porém usei para ficar mais completo

    print('\n[ERRO] Valor inválido! Verifique os dados e tente novamente.')

    print(
        '\n-=============-'
        '\n| [1] PEDRA   |'
        '\n| [2] PAPEL   |'
        '\n| [3] TESOURA |'
        '\n-=============-'
        '\n'
        '\nESCOLHA UM NÚMERO!'
    )

    userMethod = str(input('\nDigite o número: ')).strip()

if userMethod == '1':
    rpsUser = 'Pedra'
elif userMethod == '2':
    rpsUser = 'Papel'
elif userMethod == '3':
    rpsUser = 'Tesoura'

print(
    f'\nVocê escolheu: {rpsUser}'
    f'\nEu escolhi: {rpsPC}'
)

sleep(0.3)
print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

print(
    '\n-=====================-'
    f'\nVocê escolheu: {rpsUser}'
    f'\nEu escolhi: {rpsPC}'
    '\n-=====================-'
)

#PEDRA
if rpsUser == 'Pedra' and rpsPC == 'Pedra': #PEDRA + PEDRA // EMPATE
    print(f'\nEmpate! Eu e você escolhemos Pedra.\n')

elif rpsUser == 'Pedra' and rpsPC == 'Papel': #PEDRA + PAPEL // PERDEU
    print(f'\nHAHAHA, você perdeu, eu escolhi {rpsPC} e você {rpsUser}!\n')

elif rpsUser == 'Pedra' and rpsPC == 'Tesoura': #PEDRA + TESOURA // VENCEU
    print(f'\nParabéns! Você ganhou, eu escolhi {rpsPC} e você {rpsUser}.\n')

#PAPEL
elif rpsUser == 'Papel' and rpsPC == 'Papel': #PAPEL + PAPEL // EMPATE
    print(f'\nEmpate! Eu e você escolhemos Papel.\n')

elif rpsUser == 'Papel' and rpsPC == 'Tesoura': #PAPEL + TESOURA // PERDEU
    print(f'\nHAHAHA, você perdeu, eu escolhi {rpsPC} e você {rpsUser}!\n')

elif rpsUser == 'Papel' and rpsPC == 'Pedra': #PAPEL + PEDRA // VENCEU
    print(f'\nParabéns! Você ganhou, eu escolhi {rpsPC} e você {rpsUser}.\n')

#TESOURA
elif rpsUser == 'Tesoura' and rpsPC == 'Tesoura': #TESOURA + TESOURA // EMPATE
    print(f'\nEmpate! Eu e você escolhemos Papel.\n')

elif rpsUser == 'Tesoura' and rpsPC == 'Pedra': #TESOURA + PEDRA // PERDEU
    print(f'\nHAHAHA, você perdeu, eu escolhi {rpsPC} e você {rpsUser}!\n')

elif rpsUser == 'Tesoura' and rpsPC == 'Papel': #TESOURA + PAPEL // VENCEU
    print(f'\nParabéns! Você ganhou, eu escolhi {rpsPC} e você {rpsUser}.\n')