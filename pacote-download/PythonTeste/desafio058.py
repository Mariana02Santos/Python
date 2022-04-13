from random import randint
x = randint(1,5)
s = 1
n = int(input('Eu vou pensar em um número de 1 a 5. Tente acertar: '))
while n != x:
    s += 1
    n = int(input('Errou. Eu pensei no número {}. Tente novamente: '.format(x)))
    x = randint(1, 5)
print('Parabéns! Depois de {} tentativas, você acertou!'.format(s))
