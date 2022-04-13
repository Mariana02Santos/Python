ld = []
lf = []
spar = s2 = s3 = 0
n = int(input('Dimensão da Matriz: '))
for l in range(1,n+1):
    for c in range(1,n+1):
        ld.append(int(input(f'[{l}][{c}]: ')))
    lf.append(ld[:])
    ld.clear()
print('\n')
for l in range(0,n):
    for c in range(0,n):
        if lf[l][c]%2==0:
            spar += lf[l][c]
        if c==2:
            s3 += lf[l][c]
        if l==1:
            s2 += lf[l][c]

        print(f'[\033[34m{lf[l][c]}\033[m]', end=' ')
    print()
print('\nSoma dos valores pares da Matriz:',spar)
if n >= 3:
    print('Soma dos valores da terceira coluna da Matriz:',s3)
if n >= 2:
    print('Maior valor da segunda linha da Matriz:',s2)

'''matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(1,4):
    for c in range(1,4):
        matriz[l-1][c-1] = int(input(f'[{l}][{c}]: '))
print('\n')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end=' ')
    print()'''



