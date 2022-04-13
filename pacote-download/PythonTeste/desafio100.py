from random import randint
from time import sleep
def sorteio(l):
    for c in range(0,5):
        x = randint(0,9)
        l.append(x)
    print('Valores sorteados:',end=' ')
    for c in range(0,5):
        sleep(0.5)
        print(l[c],end=' ')
def soma(l):
    s = 0
    for c in range(0,5):
        if l[c]%2==0:
            s += l[c]
    print('\nSoma dos valores pares:',s)

numero = []
sorteio(numero)
soma(numero)
