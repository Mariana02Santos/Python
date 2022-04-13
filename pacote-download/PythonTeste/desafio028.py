from random import randint
x = randint(1,5)
print('-=-'*20)
n = int(input('Tente adivinhar em qual número de 1 a 5 eu pensei: '))
print('-=-'*20)
if n == x:
    print('Você ACERTOU! Eu pensei no número',x)
else:
    print('Você ERROU! Eu pensei no número',x)



