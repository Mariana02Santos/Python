d = {}
l = []
lm = []
ln = []
s = c = 0
while True:
    d.clear()
    d['nome'] = input('Nome: ')
    d['sexo'] = input('[F/M] Sexo: ').strip().upper()[0]
    while d['sexo'] not in 'FM':
        d['sexo'] = input('[F/M] Resposta inválida. Sexo: ').strip().upper()[0]
    d['idade'] = int(input('Idade: '))
    s += d['idade']
    l.append(d.copy())
    r = input('[S/N] Deseja continuar? ').strip().upper()[0]
    while r not in 'SN':
        r = input('Resposta inválida. [S/N] Deseja continuar? ').strip().upper()[0]
    if r in 'N':
        break

print('\nNº de pessoas cadastradas:',len(l))
print(f'Média de idade do grupo: {s/len(l):.2f}')
for c in l:
    if c['sexo'] == 'F':
        lm.append(c['nome'])
    if c['idade'] > (s/len(l)):
        ln.append(c)

print('Lista de mulheres:',end=' ')
for c in lm:
    if c == lm[len(lm)-1]:
        print(c)
    else:
        print(c,end=', ')
print('Lista de pessoas mais velhas que a média de idade:',end=' ')
for c in ln:
    if c != ln[len(ln)-1]:
        print(f'{c["nome"]}, com {c["idade"]} anos',end=', ')
    else:
        print(f'{c["nome"]}, com {c["idade"]} anos')
