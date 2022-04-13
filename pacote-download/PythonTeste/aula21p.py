#FATORIAL
def fat(n):
    f = 1
    while n >= 1:
        f *= n
        n -= 1
    return f

x = int(input('Digite um valor: '))
print(f'{x}! = {fat(x)}')

#retorno valor lógico
def par(k):
    if k%2==0:
        return True
    else:
        return False

y = int(input('Digite um valor: '))
if par(y):
    print('É par')
else:
    print('É ímpar')

