q = n = maior = menor = s = 0
c = 'S'

while c == 'S':
    n = int(input('Digite um número: '))
    q += 1
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = menor = n
        elif n < menor:
            menor = n
    c = input('Deseja continuar (S/N)? ').strip().upper()
    while c not in 'SsNn':
        c = input('Resposta inválida. Tente novamente (S/N): ').strip().upper()
    s += n
print('Média entre os valores digitados: {:.2f}'.format(s/q))
print('Maior valor:',maior)
print('Menor valor:',menor)
