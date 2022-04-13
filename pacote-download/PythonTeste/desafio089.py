ld = []
lf = []
r = x = 's'
while r == 's':
    ld.append(str(input('Nome do Aluno: ')))
    ld.append(float(input('Nota 1: ')))
    ld.append(float(input('Nota 2: ')))
    lf.append(ld[:])
    ld.clear()
    r = input('[S/N] Deseja continuar? ').strip().lower()[0]
    while r not in 'sn':
        r = input('Resposta inválida. [S/N] Deseja continuar? ').strip().lower()[0]

for c in lf:
    print(f'\nNome: {c[0]} \nMédia: {(c[1]+c[2])/2:.1f}')
    x = input('[S/N] Gostaria de ver as notas do Aluno? ').strip().lower()[0]
    while x not in 'sn':
        x = input('Resposta inválida. [S/N] Gostaria de ver as notas do Aluno? ').strip().lower()[0]
    if x in 's':
        print(f'Nota 1: {c[1]:.1f} \nNota 2: {c[2]:.1f}')



