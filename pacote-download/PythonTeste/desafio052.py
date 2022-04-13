n = int(input(('Digite um número inteiro: ')))
s = 0
for c in range(1,n+1):
    if n%c==0:
        s += 1
if s==2:
    print(n,'é um número primo.')
else:
    print(n,'não é um número primo.')
