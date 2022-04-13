l = []
x = 0
for c in range(0,5):
    n = int(input('Digite um número: '))
    l.append(n)
for c in range (1,5):
    for i in range(0,c):
        if l[c] < l[i]:
            x = l[c]
            l[c] = l[i]
            l[i] = x
print(l)
