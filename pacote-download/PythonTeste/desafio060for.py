n = int(input('Digite um valor inteiro e eu calcularei o fatorial desse número: '))
x = n
m = n
for n in range (n,1,-1):
    m = m * (n-1)
print('{}! = {}'.format(x,m))
