l1 = []
l2 = []
n1 = []
n2 = []
r = '0'
maior = menor = 0

while r not in 'n':
    l2.append(str(input('Nome: ')))
    l2.append(str(input('Peso: ')))
    if r == '0':
        maior = menor = l2[1]
        n1.append(l2[0])
        n2.append(l2[0])
    else:
        if l2[1] > maior:
            maior = l2[1]
            n1.clear()
            n1.append(l2[0])
        elif l2[1] < menor:
            menor = l2[1]
            n2.clear()
            n2.append(l2[0])
        elif l2[1] == maior:
            n1.append(l2[0])
        elif l2[1] == menor:
            n2.append(l2[0])

    #l1.append(l2[:])
    l2.clear()
    r = input('[S/N] Deseja continuar? ').strip().lower()[0]
    while r not in 'sn':
        r = input('Resposta inválida. [S/N] Deseja continuar? ')

print('\nQuantidade de pessoas cadastradas:',len(l1))
print(f'Maior peso: {maior}.',end=' ')
for c in n1:
    print(f'[{c}]',end=' ')
print(f'\nMenor peso: {menor}.',end=' ')
for c in n2:
    print(f'[{c}]',end=' ')


