# AS TUPLAS SÃO IMUTÁVEIS
#           ACEITAM TIPOS PRIMITIVOS DIFERENTE
# del nome_da_tupla
grignoter = ('hamburguer','jus','pizza','pudding')
print(grignoter[-1])
print(grignoter[-2:])
for aliments in grignoter:
    print('Je vais manger',aliments)
print('Jai trop mangé!')

for pos, aliments in enumerate(grignoter):
    print('Je vais manger',aliments,'en position',pos)

x = sorted(grignoter)
print(x)

a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
print(c.index(2))
print(c.count(5))
print(c.index(2,3))

