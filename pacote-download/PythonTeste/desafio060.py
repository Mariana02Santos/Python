n = int(input('Digite um valor inteiro e eu calcularei o fatorial desse número: '))
x = n
m = n
while n > 1:
    m = m * (n-1)
    n = n - 1
print('{}! = {}'.format(x,m))
