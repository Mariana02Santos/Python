r = 's'
l = []
while r == 's':
    n = int(input('Digite um valor: '))
    l.append(n)
    r = input('[S/N] Deseja continuar? ').strip().lower()[0]
    while r not in 'sn':
        r = input('Resposta inválida. [S/N] Deseja continuar? ')

print('Número de elementos da lista:',len(l))
l.sort(reverse=True)
print('Lista organizada de modo decrescente:',l)
if 5 in l:
    print('O número 5 está na lista')
else:
    print('O número não 5 está na lista')