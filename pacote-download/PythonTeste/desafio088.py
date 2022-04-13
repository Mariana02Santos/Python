from random import randint
from time import sleep

cor = {'limpa':'\033[m','ciano':'\033[1;36m','amare':'\033[1;33m'}
ld = []
lf = []

print('{}+=+=+=+=+=+=+=+=+=+=+=+=+=+{}'.format(cor['amare'],cor['limpa']))
print('    {}PROGRAMA MEGA SENA{}'.format(cor['ciano'],cor['limpa']))
print('{}+=+=+=+=+=+=+=+=+=+=+=+=+=+{}'.format(cor['amare'],cor['limpa']))
n = int(input('Quantos jogos? '))

for c in range(0,n):
    for i in range(0,6):
        ld.append(randint(1,60))
    lf.append(ld[:])
    ld.clear()

for c in range(0,n):
    if c%2!=0:
        cor['ciano'] = '\033[1;33m'
    else:
        cor['ciano'] = '\033[1;36m'
    sleep(1)
    print('Jogo {}: {}{}{}'.format((c+1),cor['ciano'],lf[c],cor['limpa']))
