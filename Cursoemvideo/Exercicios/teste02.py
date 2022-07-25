# random numbers
from random import randint, sample

# empty lists....
train_labels = []
train_samples = []

pop = 4200
youngmin = 13
youngmax = 64
oldmin = youngmax + 1
oldmax = 100
for i in range(int((pop / 2) * 0.10)):
    # The 10% of younger individuals who did experience side effects
    random_younger = randint(youngmin, youngmax)
    train_samples.append(random_younger)
    train_labels.append(1)

for i in range(int((pop / 2) * 0.90)):
    # The 90% of younger individuals who did not experience side effects
    random_younger = randint(youngmin, youngmax)
    train_samples.append(random_younger)
    train_labels.append(0)

for i in range(int((pop / 2) * 0.97)):
    # The 97% of older individuals who did experience side effects
    random_older = randint(oldmin, oldmax)
    train_samples.append(random_older)
    train_labels.append(1)

for i in range(int((pop / 2) * 0.03)):
    # The 3% of older individuals who did not experience side effects
    random_older = randint(oldmin, oldmax)
    train_samples.append(random_older)
    train_labels.append(0)

print(len(train_samples))


# Criar uma função que recebe as duas listas de treinamento (lista de idades e lista de "efeitos") como paramêtros.
# A função deve imprimir os 10 pacientes em posições aleatórias da lista com a idade e se tem ou não o efeito colateral

def show_firth_10(t_samples, t_labels):
    s = sample(range(0, len(t_samples)), 10)
    for c, v in enumerate(s):
        if t_labels[v] == 1:
            resp = "tem"
        elif t_labels[v] == 0:
            resp = "não tem"
        print(f'O {c + 1}º indivíduo amostrado com {t_samples[v]} anos {resp} efeito colateral.')


show_firth_10(train_samples, train_labels)
