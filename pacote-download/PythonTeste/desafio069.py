c = 1
q = h = m = 0

while True:
    i = int(input(f'\nDigite a idade da {c}ª pessoa: '))
    if i > 18:
        q += 1
    s = input(f'[M/F] Digite o sexo da {c}ª pessoa: ').strip().upper()[0]
    if s == 'M':
        h += 1
    if s == 'F' and i < 20:
        m += 1
    c += 1
    while s not in 'MF':
        s = input('Resposta inválida. Tente novamente [M/F]: ').strip().upper()[0]
    r = input('\033[35m[S/N] Deseja continuar?\033[m ').strip().upper()[0]
    while r not in 'SN':
        r = input('[S/N] Resposta inválida. Deseja continuar? ').strip().upper()[0]
    if r == 'N':
        break
print('\nQuantidade de pessoas que têm mais de 18 anos:',q)
print('Quantidade de homens cadastrados:',h)
print('Quantidade de mulheres menores de 20 anos:',m)
