n = int(input('Digite um número (0 a 9999): '))
#print('Unidade:', n[3])
#print('Dezena:', n[2])
#print('Centena:', n[1])
#print('Milhar:', n[0])
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade:', u)
print('Dezena:', d)
print('Centena:', c)
print('Milhar:', m)


