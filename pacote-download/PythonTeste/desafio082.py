r = 's'
l = []
l1 = []
l2 = []
while r == 's':
    n = int(input('Digite um valor: '))
    l.append(n)
    if n%2==0:
        l2.append(n)
    else:
        l1.append(n)
    r = input('[S/N] Deseja continuar? ').strip().lower()[0]
    while r not in 'sn':
        r = input('Resposta inválida. [S/N] Deseja continuar? ')
print(f'{l}\n{l1}\n{l2}')


