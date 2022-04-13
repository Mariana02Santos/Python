from random import randint
from time import sleep
d = {}
l = []
x = 0
print('Valores sorteados: ')
for c in range(0,4):
    x = randint(1,6)
    l.append(x)
    sleep(0.5)
    print(f'O jogador {c+1} tirou {x}')
l.sort(reverse=True)
for c in range(0,4):
    d[f'{c+1}º lugar'] = l[c]
print('\nRanking dos jogadores:')
for k,v in d.items():
    sleep(0.7)
    print(f'{k}: {v}')




