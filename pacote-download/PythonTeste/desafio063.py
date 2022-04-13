n = int(input('Digite um valor: '))
s = 1
x0 = 0
x1 = 1
p = 0

print(x0,end=' ')
while s < n:
    p = x1
    print(x1,end=' ')
    x1 += x0
    x0 = p
    s += 1
