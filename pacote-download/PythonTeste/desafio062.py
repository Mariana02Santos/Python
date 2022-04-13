a1 = int(input('Digite um valor inteiro para o 1º termo de uma PA: '))
x = a1
r = int(input('Digite um valor para a razão dessa PA: '))
s = 0
n = 1
while s < 10:
    print(x,end=' ')
    x = x + r
    s += 1
s = 0

while n != 0:
    n = int(input('\nQuantos mais termos você gostaria de ver nessa PA? '))
    x = a1
    while s < 10+n:
        print(x,end=' ')
        x = x + r
        s += 1




