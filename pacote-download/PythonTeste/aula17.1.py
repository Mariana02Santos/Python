lista = ['a','b','c']
lista.append('d')
lista.insert(0,'e')

print(lista)

del lista[3]
lista.pop(3)
lista.pop()
lista.remove('a') #remove apenas o primeiro elemento que aparece

print(lista)

valeurs = list(range(4,11))
print(valeurs)

l = [8,3,6,9,2,0,4,6,1]
l.sort()
print(l)

l.sort(reverse=True)
print(l)

print(len(l))

l[2] = 3
print(l)

for c, v in enumerate(l):
    print(f'En position {c+1} jai trouvé la valeur {v}')

a = [2,4,1,5]
b = a #lien entre les listes
b[2] = 8
print(a)
print(b)
c = a[:] #copie de la liste
c[1] = 9
print(a)
print(c)
