f = input('Digite uma frase: ').strip()
e = f.count(' ')
r = (f.replace(" ","")).lower()

x = len(r)
s = 0
y = 1
for c in range(0,x):
    if r[c]==r[x-y]:
        s += 1
    y += 1
if s==x:
    print('A frase "' + f + '" é um palíndromo')
else:
    print('A frase "' + f + '" não é um palíndromo')




