print('PROGRESSÃO ARITMÉTICA')
a1 = int(input('Digite o valor do primeiro termo da PA: '))
r = int(input('Digite o valor da razão da PA: '))
an = a1 + 9*r
for c in range(a1,an+1,r):
    print(c,end=' ')


