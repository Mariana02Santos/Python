l = []
lpar = []
limp = []
for c in range(0,7):
    n = int(input('Digite um valor: '))
    if n%2==0:
        lpar.append(n)
    else:
        limp.append(n)
lpar.sort()
limp.sort()
l.append(lpar)
l.append(limp)
print(l)


