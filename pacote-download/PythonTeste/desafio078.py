l = []
maior = menor = p1 = p2 = 0
for c in range(0,4):
    n = int(input('entrer une valeur: '))
    l.append(n)
    if c == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
            p1 = c
        elif n < menor:
            menor = n
            p2 = c

print(f'Le plus gros élément de la liste est le chiffres {maior} en position {p1+1}')
print(f'Le plus petit élément de la liste est le chiffres {menor} en position {p2+1}')
